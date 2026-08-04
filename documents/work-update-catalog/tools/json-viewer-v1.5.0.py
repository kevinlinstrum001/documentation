#!/usr/bin/env python3
r"""
Local JSON Explorer v1.5.0

A read-only, standard-library-only browser workbench for a structured JSON
repository. It recursively discovers JSON files beneath a content root,
provides generic tree/raw inspection, document-sidecar previews, chemical-product
previews, and type-aware catalog browsers for catalogs containing an ``entries`` array.

Recommended layout:

    work-update-catalog/
    ├── tools/
    │   └── json-viewer-v1.5.0.py
    ├── catalogs/
    ├── sidecars/
    ├── summaries/
    ├── templates/
    ├── workflows/
    ├── archived/
    └── open-json-viewer-v1.5.0.bat

Recommended launch command from the repository root:

    py -3 "%~dp0tools\json-viewer-v1.5.0.py" --folder "%~dp0"

No third-party packages are required.
"""

from __future__ import annotations

import argparse
import json
import os
import threading
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

APP_TITLE = "Local JSON Explorer"
APP_VERSION = "1.5.0"
BUILD_ID = "2026-08-02-chemical-catalog-renderer"
HOST = "127.0.0.1"

EXCLUDED_DIRECTORY_NAMES = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
}
ARCHIVE_DIRECTORY_NAMES = {"archive", "archived"}


HTML_PAGE = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Local JSON Explorer v1.5.0</title>
  <style>
    :root {
      color-scheme: light dark;
      --bg: #eef2f6;
      --panel: #ffffff;
      --panel-2: #f7f9fb;
      --panel-3: #edf3f8;
      --text: #18212b;
      --muted: #637180;
      --line: #d6dde5;
      --accent: #315f8f;
      --accent-strong: #24496f;
      --accent-soft: #dce8f3;
      --danger: #a33a3a;
      --danger-soft: #fff0f0;
      --warning: #896a15;
      --warning-soft: #fff8df;
      --shadow: 0 8px 26px rgba(23, 50, 77, 0.08);
      --radius: 12px;
      --mono: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
      --sans: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    }

    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #111820;
        --panel: #18222c;
        --panel-2: #202c37;
        --panel-3: #263543;
        --text: #eef5fb;
        --muted: #aab7c3;
        --line: #334352;
        --accent: #83b8e5;
        --accent-strong: #a9d2f2;
        --accent-soft: #213c54;
        --danger: #ff9d9d;
        --danger-soft: #412427;
        --warning: #efd27b;
        --warning-soft: #3b341e;
        --shadow: none;
      }
    }

    * { box-sizing: border-box; }
    html, body {
      width: 100%;
      height: 100%;
      overflow: hidden;
    }
    body {
      margin: 0;
      min-width: 0;
      min-height: 0;
      background: var(--bg);
      color: var(--text);
      font-family: var(--sans);
      overflow: hidden;
    }

    button, input, select { font: inherit; }

    button {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      color: var(--text);
      padding: .48rem .7rem;
      cursor: pointer;
    }
    button:hover { border-color: var(--accent); }
    button:disabled { cursor: not-allowed; opacity: .5; }
    button[aria-pressed="true"] {
      background: var(--accent-soft);
      border-color: var(--accent);
      color: var(--accent-strong);
    }
    button:focus-visible, input:focus-visible, select:focus-visible,
    [tabindex="0"]:focus-visible {
      outline: 3px solid color-mix(in srgb, var(--accent) 35%, transparent);
      outline-offset: 2px;
    }

    .app {
      --preview-width: 470px;
      display: grid;
      grid-template-columns: minmax(270px, 350px) minmax(0, 1fr) 0 0;
      width: 100vw;
      height: 100vh;
      min-width: 0;
      min-height: 0;
      overflow: hidden;
    }
    .app.preview-open {
      grid-template-columns:
        minmax(270px, 350px)
        minmax(0, 1fr)
        6px
        minmax(360px, var(--preview-width));
    }

    .sidebar {
      display: flex;
      flex-direction: column;
      min-width: 0;
      min-height: 0;
      height: 100vh;
      overflow: hidden;
      background: var(--panel);
      border-right: 1px solid var(--line);
    }
    .sidebar-header {
      padding: .9rem;
      border-bottom: 1px solid var(--line);
    }
    h1 {
      margin: 0 0 .2rem;
      color: var(--accent-strong);
      font-size: 1.15rem;
    }
    .subtle {
      margin: 0;
      color: var(--muted);
      font-size: .8rem;
      line-height: 1.4;
    }
    .runtime-info { margin-top: .2rem; }
    .file-controls {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: .45rem;
      margin-top: .8rem;
    }
    .file-controls input, .toolbar input, select, .catalog-controls input {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel-2);
      color: var(--text);
      padding: .5rem .62rem;
    }
    .sort-row {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: .45rem;
      margin-top: .45rem;
      align-items: center;
    }
    .archive-toggle {
      display: flex;
      align-items: center;
      gap: .42rem;
      margin-top: .58rem;
      color: var(--muted);
      font-size: .79rem;
      user-select: none;
    }
    .archive-toggle input { accent-color: var(--accent); }
    .file-tree {
      min-height: 0;
      overflow: auto;
      padding: .5rem;
      scrollbar-gutter: stable;
    }
    .folder-group {
      margin: .12rem 0;
    }
    .folder-group > summary {
      display: flex;
      align-items: center;
      gap: .35rem;
      padding: .38rem .42rem;
      border-radius: 7px;
      color: var(--accent-strong);
      cursor: pointer;
      font-size: .82rem;
      font-weight: 750;
      list-style: none;
      user-select: none;
    }
    .folder-group > summary::-webkit-details-marker { display: none; }
    .folder-group > summary::before {
      content: "▸";
      width: .8rem;
      transition: transform .1s ease;
    }
    .folder-group[open] > summary::before { transform: rotate(90deg); }
    .folder-group > summary:hover { background: var(--panel-2); }
    .folder-count {
      margin-left: auto;
      color: var(--muted);
      font-size: .68rem;
      font-weight: 600;
    }
    .folder-children {
      margin-left: .68rem;
      padding-left: .5rem;
      border-left: 1px dotted var(--line);
    }
    .file-item {
      display: block;
      width: 100%;
      margin: .12rem 0;
      padding: .48rem .55rem;
      text-align: left;
      background: transparent;
      border: 1px solid transparent;
      border-radius: 8px;
    }
    .file-item:hover {
      background: var(--panel-2);
      border-color: var(--line);
    }
    .file-item.active {
      background: var(--accent-soft);
      border-color: var(--accent);
    }
    .file-name {
      display: block;
      overflow-wrap: anywhere;
      font-size: .82rem;
      font-weight: 750;
    }
    .file-meta {
      display: block;
      margin-top: .16rem;
      color: var(--muted);
      font-size: .68rem;
    }
    .file-path-hint {
      display: block;
      margin-top: .1rem;
      overflow: hidden;
      color: var(--muted);
      font-family: var(--mono);
      font-size: .64rem;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .archive-badge {
      display: inline-block;
      margin-left: .3rem;
      padding: .05rem .3rem;
      border-radius: 999px;
      color: var(--warning);
      background: var(--warning-soft);
      font-size: .6rem;
      text-transform: uppercase;
      letter-spacing: .04em;
    }

    .main {
      display: grid;
      grid-template-rows: auto minmax(0, 1fr);
      min-width: 0;
      min-height: 0;
      height: 100vh;
      overflow: hidden;
    }
    .topbar {
      position: relative;
      padding: .68rem .85rem;
      min-width: 0;
      background: var(--panel);
      border-bottom: 1px solid var(--line);
      box-shadow: var(--shadow);
      z-index: 2;
    }
    .current-file {
      display: flex;
      align-items: baseline;
      gap: .55rem;
      min-width: 0;
      margin-bottom: .52rem;
    }
    .current-file strong {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      font-size: .9rem;
    }
    .badge {
      flex: 0 0 auto;
      padding: .14rem .42rem;
      border-radius: 999px;
      background: var(--accent-soft);
      color: var(--accent-strong);
      font-size: .65rem;
      font-weight: 850;
    }
    .toolbar {
      display: grid;
      grid-template-columns: auto auto auto auto auto auto minmax(180px, 1fr) auto;
      gap: .38rem;
      align-items: center;
      max-width: 100%;
      overflow-x: auto;
      padding-bottom: .1rem;
    }
    .toolbar button { padding: .42rem .58rem; }
    .depth-wrap {
      display: flex;
      align-items: center;
      gap: .3rem;
      font-size: .76rem;
    }
    .depth-wrap select { width: auto; padding: .42rem .5rem; }
    .status {
      margin-top: .38rem;
      color: var(--muted);
      font-size: .72rem;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .content {
      min-width: 0;
      min-height: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      overscroll-behavior: contain;
      padding: .8rem;
      scrollbar-gutter: stable both-edges;
      -webkit-overflow-scrolling: touch;
    }
    .empty {
      max-width: 760px;
      margin: 8vh auto 0;
      padding: 1.8rem;
      text-align: center;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }
    .error {
      max-width: 900px;
      margin: 1rem auto;
      padding: 1rem 1.15rem;
      background: var(--danger-soft);
      color: var(--danger);
      border: 1px solid color-mix(in srgb, var(--danger) 45%, var(--line));
      border-left: 6px solid var(--danger);
      border-radius: var(--radius);
      white-space: pre-wrap;
      font-family: var(--mono);
    }

    .tree-shell {
      width: max-content;
      min-width: 100%;
      padding: .7rem .85rem 2rem;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }
    .tree-node {
      margin-left: 1.08rem;
      border-left: 1px dotted var(--line);
      padding-left: .5rem;
    }
    .tree-node.root {
      margin-left: 0;
      border-left: 0;
      padding-left: 0;
    }
    details.tree-node > summary {
      list-style: none;
      cursor: pointer;
      padding: .16rem .28rem;
      border-radius: 5px;
      font-family: var(--mono);
      white-space: normal;
    }
    details.tree-node > summary::-webkit-details-marker { display: none; }
    details.tree-node > summary::before {
      content: "▸";
      display: inline-block;
      width: 1rem;
      color: var(--accent);
      transition: transform .1s ease;
    }
    details.tree-node[open] > summary::before { transform: rotate(90deg); }
    .key { color: var(--accent-strong); font-weight: 750; }
    .type-note { color: var(--muted); font-size: .78em; }
    .leaf {
      display: grid;
      grid-template-columns: minmax(120px, auto) minmax(160px, 1fr) auto;
      gap: .5rem;
      align-items: start;
      padding: .16rem .28rem .16rem 1.1rem;
      border-radius: 5px;
      font-family: var(--mono);
      white-space: normal;
    }
    .leaf:hover, details.tree-node > summary:hover { background: var(--panel-2); }
    .value {
      max-width: 82ch;
      overflow-wrap: anywhere;
      white-space: pre-wrap;
    }
    .string { color: #3a7a43; }
    .number { color: #995f00; }
    .boolean { color: #8051a8; font-weight: 700; }
    .null { color: var(--muted); font-style: italic; }
    @media (prefers-color-scheme: dark) {
      .string { color: #9bd5a4; }
      .number { color: #ffc56e; }
      .boolean { color: #d8a8ff; }
    }
    .copy-button {
      opacity: 0;
      padding: .11rem .3rem;
      font-size: .66rem;
    }
    .leaf:hover .copy-button, details.tree-node > summary:hover .copy-button { opacity: 1; }
    mark {
      color: inherit;
      background: #ffe38a;
      border-radius: 3px;
      padding: 0 .08em;
    }
    .search-match {
      background: color-mix(in srgb, #ffe38a 32%, transparent) !important;
      outline: 1px solid color-mix(in srgb, #d7a900 55%, transparent);
    }
    .source-highlight {
      animation: sourcePulse 1.8s ease;
      background: color-mix(in srgb, #ffe38a 38%, transparent) !important;
      outline: 2px solid color-mix(in srgb, #d7a900 62%, transparent);
    }
    @keyframes sourcePulse {
      0%, 100% { outline-offset: 0; }
      45% { outline-offset: 4px; }
    }
    .raw {
      margin: 0;
      min-height: 100%;
      padding: .9rem;
      overflow: auto;
      color: var(--text);
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      font: .87rem/1.52 var(--mono);
      white-space: pre;
      tab-size: 2;
    }

    .catalog-shell {
      max-width: 1180px;
      margin: 0 auto;
    }
    .catalog-header {
      padding: 1rem 1.1rem;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }
    .catalog-eyebrow {
      margin: 0 0 .25rem;
      color: var(--accent);
      font-size: .68rem;
      font-weight: 850;
      letter-spacing: .1em;
      text-transform: uppercase;
    }
    .catalog-title {
      margin: 0;
      font-size: 1.4rem;
      line-height: 1.2;
    }
    .catalog-description {
      margin: .42rem 0 0;
      color: var(--muted);
      line-height: 1.5;
    }
    .catalog-stats {
      display: flex;
      flex-wrap: wrap;
      gap: .35rem;
      margin-top: .65rem;
    }
    .catalog-controls {
      display: grid;
      grid-template-columns: repeat(4, minmax(130px, 1fr));
      gap: .45rem;
      margin-top: .7rem;
      padding: .7rem;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: var(--radius);
    }
    .catalog-control label {
      display: block;
      margin-bottom: .22rem;
      color: var(--muted);
      font-size: .68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: .04em;
    }
    .catalog-list {
      display: grid;
      gap: .58rem;
      margin-top: .7rem;
      padding-bottom: 2rem;
    }
    .catalog-card {
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: .75rem;
      padding: .85rem .95rem;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 11px;
      box-shadow: var(--shadow);
      cursor: pointer;
    }
    .catalog-card:hover { border-color: var(--accent); }
    .catalog-card.selected {
      background: color-mix(in srgb, var(--accent-soft) 48%, var(--panel));
      border-color: var(--accent);
    }
    .catalog-card-title {
      margin: 0;
      color: var(--text);
      font-size: 1rem;
      line-height: 1.25;
    }
    .catalog-card-headline {
      margin: .28rem 0 0;
      color: var(--muted);
      font-size: .83rem;
      line-height: 1.42;
    }
    .catalog-card-meta {
      display: flex;
      flex-wrap: wrap;
      gap: .3rem;
      margin-top: .5rem;
    }
    .catalog-card-topics {
      display: flex;
      flex-wrap: wrap;
      gap: .25rem;
      margin-top: .48rem;
    }
    .catalog-card-actions {
      display: flex;
      align-items: flex-start;
      gap: .35rem;
    }
    .catalog-source-button { font-size: .7rem; }
    .catalog-empty {
      padding: 2rem;
      text-align: center;
      color: var(--muted);
      background: var(--panel);
      border: 1px dashed var(--line);
      border-radius: var(--radius);
    }

    .chemical-fact-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: .45rem;
      margin-top: .45rem;
    }
    .chemical-fact {
      min-width: 0;
      padding: .55rem .6rem;
      background: var(--panel-2);
      border: 1px solid var(--line);
      border-radius: 8px;
    }
    .chemical-fact-label {
      display: block;
      margin-bottom: .18rem;
      color: var(--muted);
      font-size: .62rem;
      font-weight: 750;
      letter-spacing: .04em;
      text-transform: uppercase;
    }
    .chemical-fact-value {
      display: block;
      overflow-wrap: anywhere;
      color: var(--text);
      font-size: .78rem;
      line-height: 1.38;
    }
    .chemical-source-links {
      display: flex;
      flex-wrap: wrap;
      gap: .35rem;
      margin-top: .55rem;
    }
    .chemical-coverage {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: .42rem;
      margin-top: .5rem;
    }
    .chemical-coverage-item {
      padding: .48rem .52rem;
      text-align: center;
      background: var(--panel-2);
      border: 1px solid var(--line);
      border-radius: 8px;
    }
    .chemical-coverage-item strong {
      display: block;
      color: var(--accent-strong);
      font-size: 1rem;
    }
    .chemical-coverage-item span {
      display: block;
      margin-top: .1rem;
      color: var(--muted);
      font-size: .62rem;
    }
    .chemical-section-list {
      display: grid;
      gap: .3rem;
      margin-top: .5rem;
    }
    .chemical-section-row {
      display: grid;
      grid-template-columns: 2.2rem minmax(0, 1fr) auto;
      gap: .45rem;
      align-items: center;
      padding: .42rem .48rem;
      background: var(--panel-2);
      border: 1px solid var(--line);
      border-radius: 7px;
      font-size: .72rem;
    }
    .chemical-section-number {
      color: var(--accent-strong);
      font-weight: 850;
    }
    .chemical-section-status {
      color: var(--muted);
      font-family: var(--mono);
      font-size: .62rem;
    }

    .preview-resizer {
      display: none;
      width: 6px;
      min-width: 6px;
      height: 100vh;
      cursor: col-resize;
      background: linear-gradient(to right, transparent 0, transparent 2px, var(--line) 2px, var(--line) 4px, transparent 4px);
      touch-action: none;
    }
    .app.preview-open .preview-resizer { display: block; }
    body.resizing-preview, body.resizing-preview * {
      cursor: col-resize !important;
      user-select: none !important;
    }
    .preview-panel {
      display: none;
      min-width: 0;
      min-height: 0;
      height: 100vh;
      overflow: hidden;
      background: var(--panel-2);
      border-left: 1px solid var(--line);
    }
    .app.preview-open .preview-panel {
      display: grid;
      grid-template-rows: auto minmax(0, 1fr);
    }
    .preview-panel-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: .75rem;
      padding: .72rem .8rem;
      background: var(--panel);
      border-bottom: 1px solid var(--line);
    }
    .preview-panel-title { min-width: 0; }
    .preview-panel-title strong {
      display: block;
      color: var(--accent-strong);
      font-size: .88rem;
    }
    .preview-panel-title span {
      display: block;
      margin-top: .1rem;
      overflow: hidden;
      color: var(--muted);
      font-size: .7rem;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .preview-scroll {
      min-width: 0;
      min-height: 0;
      overflow: auto;
      padding: .85rem;
      scrollbar-gutter: stable;
    }
    .preview-document {
      max-width: 760px;
      margin: 0 auto;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 14px;
      box-shadow: var(--shadow);
      overflow: hidden;
    }
    .preview-hero {
      padding: 1.05rem 1.12rem 1rem;
      background: linear-gradient(145deg, color-mix(in srgb, var(--accent-soft) 68%, var(--panel)), var(--panel) 72%);
      border-bottom: 1px solid var(--line);
    }
    .preview-eyebrow {
      margin: 0 0 .38rem;
      color: var(--accent);
      font-size: .65rem;
      font-weight: 850;
      letter-spacing: .1em;
      text-transform: uppercase;
    }
    .preview-title {
      margin: 0;
      color: var(--text);
      font-size: clamp(1.25rem, 2vw, 1.8rem);
      line-height: 1.13;
      text-wrap: balance;
    }
    .preview-subtitle {
      margin: .48rem 0 0;
      color: var(--muted);
      font-size: .9rem;
      line-height: 1.42;
    }
    .preview-meta, .preview-actions, .preview-topic-list {
      display: flex;
      flex-wrap: wrap;
      gap: .32rem;
    }
    .preview-meta { margin-top: .72rem; }
    .preview-actions { margin-top: .72rem; }
    .preview-chip, .preview-topic {
      display: inline-flex;
      align-items: center;
      max-width: 100%;
      padding: .2rem .44rem;
      overflow: hidden;
      border-radius: 999px;
      font-size: .68rem;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .preview-chip {
      color: var(--muted);
      background: color-mix(in srgb, var(--panel) 82%, var(--accent-soft));
      border: 1px solid var(--line);
    }
    .preview-topic {
      color: var(--accent-strong);
      background: var(--accent-soft);
    }
    .preview-link {
      display: inline-flex;
      align-items: center;
      border: 1px solid var(--accent);
      border-radius: 8px;
      background: var(--accent);
      color: var(--panel);
      padding: .43rem .65rem;
      font-size: .78rem;
      font-weight: 750;
      text-decoration: none;
    }
    .preview-summary {
      margin: 0;
      padding: 1rem 1.12rem;
      color: var(--text);
      border-bottom: 1px solid var(--line);
      font-size: .94rem;
      line-height: 1.58;
    }
    .preview-sections { padding: .25rem 1.12rem 1rem; }
    .preview-section {
      padding: .9rem 0;
      border-bottom: 1px solid var(--line);
    }
    .preview-section:last-child { border-bottom: 0; }
    .preview-section.supervisor {
      margin: .65rem -.3rem .05rem;
      padding: .78rem;
      background: color-mix(in srgb, #d8bd67 18%, var(--panel));
      border: 1px solid color-mix(in srgb, #9a7a22 35%, var(--line));
      border-radius: 9px;
    }
    .preview-section-header {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: .55rem;
      margin-bottom: .4rem;
    }
    .preview-section h3 {
      margin: 0;
      color: var(--accent-strong);
      font-size: .78rem;
      letter-spacing: .04em;
      text-transform: uppercase;
    }
    .preview-section p {
      margin: 0;
      color: var(--text);
      font-size: .86rem;
      line-height: 1.54;
      white-space: pre-wrap;
    }
    .preview-section ul, .preview-section ol {
      margin: .12rem 0 0;
      padding-left: 1.15rem;
    }
    .preview-section li {
      margin: .33rem 0;
      color: var(--text);
      font-size: .83rem;
      line-height: 1.44;
    }
    .preview-item-detail {
      display: block;
      margin-top: .1rem;
      color: var(--muted);
      font-size: .77rem;
    }
    .preview-source {
      flex: 0 0 auto;
      padding: .13rem .34rem;
      color: var(--muted);
      background: transparent;
      border-color: transparent;
      font-family: var(--mono);
      font-size: .62rem;
    }
    .preview-source:hover {
      color: var(--accent-strong);
      background: var(--accent-soft);
      border-color: var(--accent);
    }
    .preview-footer {
      padding: .78rem 1.12rem .9rem;
      color: var(--muted);
      background: var(--panel-2);
      border-top: 1px solid var(--line);
      font-size: .7rem;
      line-height: 1.42;
    }
    .preview-notice {
      margin-top: .5rem;
      padding: .5rem .58rem;
      background: var(--panel);
      border: 1px dashed var(--line);
      border-radius: 8px;
    }


    .workflow-overview-line {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: .42rem;
      margin-top: .35rem;
      color: var(--muted);
      font-size: .76rem;
    }

    .workflow-arrow {
      color: var(--accent);
      font-weight: 850;
    }

    .workflow-metrics {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: .45rem;
      margin-top: .45rem;
    }

    .workflow-metric {
      min-width: 0;
      padding: .58rem .62rem;
      background: var(--panel-2);
      border: 1px solid var(--line);
      border-radius: 9px;
    }

    .workflow-metric strong {
      display: block;
      color: var(--accent-strong);
      font-size: 1.02rem;
      line-height: 1.1;
    }

    .workflow-metric span {
      display: block;
      margin-top: .16rem;
      overflow-wrap: anywhere;
      color: var(--muted);
      font-size: .66rem;
      line-height: 1.3;
    }

    .workflow-state-path {
      display: flex;
      flex-wrap: wrap;
      gap: .3rem;
      margin-top: .45rem;
    }

    .workflow-state-chip {
      display: inline-flex;
      align-items: center;
      gap: .28rem;
      max-width: 100%;
      padding: .22rem .42rem;
      overflow-wrap: anywhere;
      color: var(--muted);
      background: var(--panel-2);
      border: 1px solid var(--line);
      border-radius: 7px;
      font-family: var(--mono);
      font-size: .63rem;
      line-height: 1.3;
    }

    .workflow-state-chip.initial,
    .workflow-state-chip.final {
      color: var(--accent-strong);
      background: var(--accent-soft);
      border-color: var(--accent);
      font-weight: 750;
    }

    .workflow-controls {
      display: flex;
      flex-wrap: wrap;
      gap: .35rem;
      margin: .45rem 0 .65rem;
    }

    .workflow-controls button {
      padding: .33rem .5rem;
      font-size: .7rem;
    }

    .workflow-phase-list {
      display: grid;
      gap: .58rem;
      margin-top: .45rem;
    }

    details.workflow-phase {
      overflow: hidden;
      background: var(--panel-2);
      border: 1px solid var(--line);
      border-radius: 10px;
    }

    details.workflow-phase > summary {
      display: grid;
      grid-template-columns: auto minmax(0, 1fr);
      gap: .55rem;
      align-items: start;
      padding: .66rem .72rem;
      cursor: pointer;
      list-style: none;
    }

    details.workflow-phase > summary::-webkit-details-marker,
    details.workflow-step > summary::-webkit-details-marker {
      display: none;
    }

    details.workflow-phase > summary::before,
    details.workflow-step > summary::before {
      content: "▸";
      color: var(--accent);
      font-weight: 850;
      transition: transform .1s ease;
    }

    details.workflow-phase[open] > summary::before,
    details.workflow-step[open] > summary::before {
      transform: rotate(90deg);
    }

    .workflow-phase-heading {
      min-width: 0;
    }

    .workflow-phase-heading strong {
      display: block;
      color: var(--accent-strong);
      font-size: .82rem;
      line-height: 1.3;
    }

    .workflow-phase-heading span {
      display: block;
      margin-top: .16rem;
      color: var(--muted);
      font-size: .69rem;
      line-height: 1.4;
    }

    .workflow-phase-body {
      padding: 0 .68rem .68rem;
      border-top: 1px solid var(--line);
    }

    .workflow-phase-purpose {
      margin: .62rem .08rem;
      color: var(--muted);
      font-size: .75rem;
      line-height: 1.45;
    }

    .workflow-step-list {
      display: grid;
      gap: .4rem;
    }

    details.workflow-step {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
    }

    details.workflow-step > summary {
      display: grid;
      grid-template-columns: auto auto minmax(0, 1fr);
      gap: .45rem;
      align-items: start;
      padding: .55rem .6rem;
      cursor: pointer;
      list-style: none;
    }

    .workflow-step-number {
      display: grid;
      place-items: center;
      min-width: 1.65rem;
      height: 1.65rem;
      padding: 0 .26rem;
      color: var(--panel);
      background: var(--accent);
      border-radius: 999px;
      font-size: .67rem;
      font-weight: 850;
    }

    .workflow-step-heading {
      min-width: 0;
    }

    .workflow-step-title {
      display: block;
      color: var(--text);
      font-size: .77rem;
      font-weight: 780;
      line-height: 1.35;
    }

    .workflow-step-transition {
      display: block;
      margin-top: .12rem;
      overflow-wrap: anywhere;
      color: var(--muted);
      font-family: var(--mono);
      font-size: .61rem;
      line-height: 1.35;
    }

    .workflow-step-tags {
      display: flex;
      flex-wrap: wrap;
      gap: .25rem;
      margin-top: .32rem;
    }

    .workflow-step-tag {
      padding: .12rem .3rem;
      color: var(--muted);
      background: var(--panel-2);
      border: 1px solid var(--line);
      border-radius: 999px;
      font-size: .58rem;
      line-height: 1.2;
    }

    .workflow-step-tag.review {
      color: var(--warning);
      background: var(--warning-soft);
    }

    .workflow-step-body {
      padding: .62rem .68rem .72rem 2.8rem;
      border-top: 1px solid var(--line);
    }

    .workflow-step-purpose {
      margin: 0 0 .62rem;
      color: var(--text);
      font-size: .76rem;
      line-height: 1.48;
    }

    .workflow-detail-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: .5rem;
    }

    .workflow-detail-block {
      min-width: 0;
      padding: .5rem .55rem;
      background: var(--panel-2);
      border: 1px solid var(--line);
      border-radius: 7px;
    }

    .workflow-detail-block h4 {
      margin: 0 0 .3rem;
      color: var(--accent-strong);
      font-size: .64rem;
      letter-spacing: .04em;
      text-transform: uppercase;
    }

    .workflow-detail-block ul {
      margin: 0;
      padding-left: 1rem;
    }

    .workflow-detail-block li {
      margin: .22rem 0;
      color: var(--text);
      font-size: .68rem;
      line-height: 1.4;
    }

    .workflow-next-step {
      margin-top: .5rem;
      color: var(--muted);
      font-family: var(--mono);
      font-size: .63rem;
    }

    .workflow-record-list {
      display: grid;
      gap: .42rem;
      margin-top: .4rem;
    }

    .workflow-record {
      padding: .55rem .6rem;
      background: var(--panel-2);
      border: 1px solid var(--line);
      border-radius: 8px;
    }

    .workflow-record strong {
      display: block;
      color: var(--text);
      font-size: .76rem;
      line-height: 1.35;
    }

    .workflow-record span {
      display: block;
      margin-top: .16rem;
      color: var(--muted);
      font-size: .68rem;
      line-height: 1.4;
    }

    .workflow-record code {
      color: var(--accent-strong);
      font-family: var(--mono);
      font-size: .66rem;
    }

    @media (max-width: 560px) {
      .workflow-metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .workflow-detail-grid { grid-template-columns: 1fr; }
      .workflow-step-body { padding-left: .68rem; }
    }

    .hidden { display: none !important; }

    @media (max-width: 1050px) {
      .app.preview-open {
        grid-template-columns: minmax(250px, 310px) minmax(0, 1fr) 6px minmax(340px, var(--preview-width));
      }
      .catalog-controls { grid-template-columns: repeat(2, minmax(150px, 1fr)); }
    }

    @media (max-width: 800px) {
      .app, .app.preview-open {
        grid-template-columns: 1fr;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
      }
      .preview-resizer { display: none !important; }
      .preview-panel, .app.preview-open .preview-panel {
        position: fixed;
        inset: 0 0 0 auto;
        width: min(92vw, 560px);
        height: 100vh;
        z-index: 12;
        box-shadow: -12px 0 35px rgba(0, 0, 0, .22);
      }
      .sidebar {
        position: fixed;
        inset: 0 auto 0 0;
        width: min(88vw, 350px);
        z-index: 10;
        transform: translateX(-100%);
        transition: transform .18s ease;
      }
      .sidebar.open { transform: translateX(0); }
      .toolbar { grid-template-columns: repeat(6, auto); }
      .toolbar input { grid-column: 1 / -1; }
      #menuButton { display: inline-block !important; }
      .catalog-controls { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
<div class="app" id="app">
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <h1>Local JSON Explorer</h1>
      <p class="subtle">Recursive, read-only repository browser</p>
      <p class="subtle runtime-info" id="runtimeInfo">Version 1.4.0 · loading runtime identity…</p>
      <div class="file-controls">
        <input id="fileFilter" type="search" placeholder="Filter filenames or paths">
        <button id="refreshButton" title="Refresh repository">Refresh</button>
      </div>
      <div class="sort-row">
        <select id="sortSelect" aria-label="Sort files">
          <option value="name">Sort by name</option>
          <option value="modified-desc">Newest first</option>
          <option value="modified-asc">Oldest first</option>
          <option value="size-desc">Largest first</option>
        </select>
        <span id="fileCount" class="subtle"></span>
      </div>
      <label class="archive-toggle">
        <input id="includeArchived" type="checkbox">
        Include archived files
      </label>
    </div>
    <div class="file-tree" id="fileTree"></div>
  </aside>

  <main class="main">
    <div class="topbar">
      <div class="current-file">
        <button id="menuButton" class="hidden" aria-label="Open file tree">Files</button>
        <strong id="currentFileName">Choose a JSON file</strong>
        <span class="badge" id="modeBadge">TREE</span>
      </div>
      <div class="toolbar">
        <button id="treeButton">Tree</button>
        <button id="rawButton">Raw</button>
        <button id="catalogButton" disabled title="Select a catalog file">Catalog</button>
        <button id="previewButton" aria-pressed="false" disabled title="Select a document sidecar or catalog entry">Preview</button>
        <button id="expandButton">Expand all</button>
        <button id="collapseButton">Collapse all</button>
        <input id="searchInput" type="search" placeholder="Search keys, values, or paths">
        <div class="depth-wrap">
          <label for="depthSelect">Depth</label>
          <select id="depthSelect">
            <option value="1">1</option>
            <option value="2" selected>2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="999">All</option>
          </select>
        </div>
      </div>
      <div class="status" id="status">No file loaded.</div>
    </div>

    <section class="content" id="content">
      <div class="empty">
        <h2>Choose a JSON file</h2>
        <p>Select a repository file to inspect its hierarchy, preview a document sidecar, or browse a document catalog.</p>
      </div>
    </section>
  </main>

  <div class="preview-resizer" id="previewResizer" role="separator" aria-label="Resize document preview" aria-orientation="vertical" tabindex="0"></div>

  <aside class="preview-panel" id="previewPanel" aria-label="Document preview" aria-hidden="true">
    <header class="preview-panel-header">
      <div class="preview-panel-title">
        <strong id="previewPanelHeading">Document preview</strong>
        <span id="previewFileName">No preview selected</span>
      </div>
      <button id="closePreviewButton" title="Close preview">Close</button>
    </header>
    <div class="preview-scroll" id="previewContent">
      <div class="empty">
        <h2>No preview available</h2>
        <p>Select a document sidecar or a catalog entry.</p>
      </div>
    </div>
  </aside>
</div>

<script>
(() => {
  const state = {
    files: [],
    currentFile: null,
    currentData: null,
    currentRaw: "",
    view: "tree",
    query: "",
    includeArchived: false,
    initialSelectionApplied: false,
    previewModel: null,
    previewOpen: false,
    previewContext: "document",
    catalogModel: null,
    selectedCatalogIndex: null,
    catalogProject: "",
    catalogType: "",
    catalogYear: "",
    catalogSort: "newest",
  };

  const els = {
    app: document.getElementById("app"),
    sidebar: document.getElementById("sidebar"),
    fileTree: document.getElementById("fileTree"),
    fileFilter: document.getElementById("fileFilter"),
    refreshButton: document.getElementById("refreshButton"),
    sortSelect: document.getElementById("sortSelect"),
    fileCount: document.getElementById("fileCount"),
    includeArchived: document.getElementById("includeArchived"),
    currentFileName: document.getElementById("currentFileName"),
    modeBadge: document.getElementById("modeBadge"),
    treeButton: document.getElementById("treeButton"),
    rawButton: document.getElementById("rawButton"),
    catalogButton: document.getElementById("catalogButton"),
    previewButton: document.getElementById("previewButton"),
    expandButton: document.getElementById("expandButton"),
    collapseButton: document.getElementById("collapseButton"),
    searchInput: document.getElementById("searchInput"),
    depthSelect: document.getElementById("depthSelect"),
    status: document.getElementById("status"),
    content: document.getElementById("content"),
    menuButton: document.getElementById("menuButton"),
    runtimeInfo: document.getElementById("runtimeInfo"),
    previewResizer: document.getElementById("previewResizer"),
    previewPanel: document.getElementById("previewPanel"),
    previewPanelHeading: document.getElementById("previewPanelHeading"),
    previewFileName: document.getElementById("previewFileName"),
    previewContent: document.getElementById("previewContent"),
    closePreviewButton: document.getElementById("closePreviewButton"),
  };

  const escapeHtml = value => String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");

  function formatBytes(bytes) {
    if (bytes < 1024) return `${bytes} B`;
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
    return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
  }

  function formatDate(epochSeconds) {
    return new Date(epochSeconds * 1000).toLocaleString();
  }

  function pathJoin(base, path) {
    if (!base) return path;
    if (!path) return base;
    return path.startsWith("[") ? `${base}${path}` : `${base}.${path}`;
  }

  function childPath(parentPath, key, isArray) {
    if (isArray) return `${parentPath}[${key}]`;
    const safeIdentifier = /^[A-Za-z_$][A-Za-z0-9_$]*$/.test(key);
    if (!parentPath) return safeIdentifier ? key : `[${JSON.stringify(key)}]`;
    return safeIdentifier ? `${parentPath}.${key}` : `${parentPath}[${JSON.stringify(key)}]`;
  }

  function sortFiles(files) {
    const mode = els.sortSelect.value;
    return [...files].sort((a, b) => {
      if (mode === "modified-desc") return b.modified - a.modified;
      if (mode === "modified-asc") return a.modified - b.modified;
      if (mode === "size-desc") return b.size - a.size;
      return a.name.localeCompare(b.name, undefined, { numeric: true, sensitivity: "base" });
    });
  }

  async function loadAbout() {
    try {
      const response = await fetch("/api/about", { cache: "no-store" });
      const about = await response.json();
      els.runtimeInfo.textContent = `v${about.version} · build ${about.buildId} · PID ${about.processId} · port ${about.port}`;
      els.runtimeInfo.title = `Script: ${about.scriptPath}\nRepository: ${about.folder}`;
    } catch {
      els.runtimeInfo.textContent = "Version 1.5.0 · runtime identity unavailable";
    }
  }

  async function loadFileList() {
    els.status.textContent = "Refreshing repository…";
    try {
      const archived = state.includeArchived ? "1" : "0";
      const response = await fetch(`/api/files?includeArchived=${archived}`, { cache: "no-store" });
      const payload = await response.json();
      if (!response.ok) throw new Error(payload.error || "Could not load repository files.");
      state.files = payload.files;
      renderFileTree();
      els.status.textContent = `${payload.files.length} JSON files discovered beneath ${payload.folder}`;

      if (!state.initialSelectionApplied) {
        state.initialSelectionApplied = true;
        const saved = localStorage.getItem("jsonExplorerSelectedPath");
        if (saved && state.files.some(file => file.path === saved)) loadFile(saved);
      }
    } catch (error) {
      showError(error.message);
    }
  }

  function makeFolderNode() {
    return { folders: new Map(), files: [] };
  }

  function buildFolderTree(files) {
    const root = makeFolderNode();
    for (const file of files) {
      const parts = file.path.split("/");
      let node = root;
      for (const part of parts.slice(0, -1)) {
        if (!node.folders.has(part)) node.folders.set(part, makeFolderNode());
        node = node.folders.get(part);
      }
      node.files.push(file);
    }
    return root;
  }

  function countFolderFiles(node) {
    let count = node.files.length;
    for (const child of node.folders.values()) count += countFolderFiles(child);
    return count;
  }

  function renderFileTree() {
    const filter = els.fileFilter.value.trim().toLowerCase();
    const visible = state.files.filter(file => !filter || file.path.toLowerCase().includes(filter));
    els.fileCount.textContent = `${visible.length} file${visible.length === 1 ? "" : "s"}`;
    els.fileTree.innerHTML = "";

    if (!visible.length) {
      els.fileTree.innerHTML = '<p class="subtle" style="padding:.7rem">No matching JSON files.</p>';
      return;
    }

    const tree = buildFolderTree(visible);
    renderFolderContents(tree, els.fileTree, "", 0, Boolean(filter));
  }

  function renderFolderContents(node, container, folderPath, depth, forceOpen) {
    const folderNames = [...node.folders.keys()].sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
    for (const folderName of folderNames) {
      const child = node.folders.get(folderName);
      const relativeFolder = folderPath ? `${folderPath}/${folderName}` : folderName;
      const details = document.createElement("details");
      details.className = "folder-group";
      details.open = forceOpen || depth === 0 || localStorage.getItem(`jsonFolderOpen:${relativeFolder}`) === "1";

      const summary = document.createElement("summary");
      const label = document.createElement("span");
      label.textContent = folderName;
      const count = document.createElement("span");
      count.className = "folder-count";
      count.textContent = countFolderFiles(child);
      summary.append(label, count);
      details.appendChild(summary);

      const children = document.createElement("div");
      children.className = "folder-children";
      details.appendChild(children);
      details.addEventListener("toggle", () => localStorage.setItem(`jsonFolderOpen:${relativeFolder}`, details.open ? "1" : "0"));
      container.appendChild(details);
      renderFolderContents(child, children, relativeFolder, depth + 1, forceOpen);
    }

    for (const file of sortFiles(node.files)) {
      const button = document.createElement("button");
      button.className = "file-item" + (state.currentFile?.path === file.path ? " active" : "");
      const archiveBadge = file.archived ? '<span class="archive-badge">archive</span>' : "";
      button.innerHTML = `
        <span class="file-name">${escapeHtml(file.name)}${archiveBadge}</span>
        <span class="file-meta">${formatBytes(file.size)} · ${escapeHtml(formatDate(file.modified))}</span>
        <span class="file-path-hint">${escapeHtml(file.path)}</span>
      `;
      button.title = file.path;
      button.addEventListener("click", () => loadFile(file.path));
      container.appendChild(button);
    }
  }

  async function loadFile(path) {
    els.status.textContent = `Loading ${path}…`;
    try {
      const response = await fetch(`/api/file?path=${encodeURIComponent(path)}`, { cache: "no-store" });
      const payload = await response.json();
      if (!response.ok) {
        resetLoadedState(path, payload.raw || "");
        showError(payload.error || "Invalid JSON.");
        return;
      }

      state.currentFile = state.files.find(file => file.path === path) || { path, name: payload.name };
      state.currentData = payload.data;
      state.currentRaw = payload.raw;
      state.query = "";
      state.catalogProject = "";
      state.catalogType = "";
      state.catalogYear = "";
      state.catalogSort = "newest";
      state.selectedCatalogIndex = null;
      els.searchInput.value = "";
      els.currentFileName.textContent = path;
      localStorage.setItem("jsonExplorerSelectedPath", path);

      state.catalogModel = buildCatalogModel(state.currentData);
      if (state.catalogModel) {
        state.view = "catalog";
        selectCatalogEntry(state.catalogModel.entries[0]?.index ?? null, false);
      } else {
        state.view = "tree";
        state.previewModel = buildSidecarPreview(state.currentData, "");
        state.previewContext = "document";
      }

      renderFileTree();
      renderCurrentView();
      updateToolbarState();
      setPreviewOpen(Boolean(state.previewModel));
      els.status.textContent = `${payload.nodeCount.toLocaleString()} nodes · ${formatBytes(payload.size)} · ${path}`;
      if (window.innerWidth <= 800) els.sidebar.classList.remove("open");
    } catch (error) {
      resetLoadedState(path, "");
      showError(error.message);
    }
  }

  function resetLoadedState(path, raw) {
    state.currentFile = state.files.find(file => file.path === path) || { path, name: path.split("/").pop() };
    state.currentData = null;
    state.currentRaw = raw;
    state.catalogModel = null;
    state.previewModel = null;
    state.selectedCatalogIndex = null;
    els.currentFileName.textContent = path;
    renderFileTree();
    setPreviewOpen(false);
    updateToolbarState();
  }

  function valueClass(value) {
    if (value === null) return "null";
    if (typeof value === "string") return "string";
    if (typeof value === "number") return "number";
    if (typeof value === "boolean") return "boolean";
    return "";
  }

  function valueText(value) {
    if (value === null) return "null";
    if (typeof value === "string") return value;
    return JSON.stringify(value);
  }

  function makeCopyButton(text, label) {
    const button = document.createElement("button");
    button.className = "copy-button";
    button.textContent = label;
    button.title = `Copy ${label.toLowerCase()}`;
    button.addEventListener("click", async event => {
      event.preventDefault();
      event.stopPropagation();
      await copyText(text, button, label);
    });
    return button;
  }

  async function copyText(text, button = null, restoreLabel = "Copy") {
    try {
      await navigator.clipboard.writeText(text);
      if (button) {
        button.textContent = "Copied";
        setTimeout(() => button.textContent = restoreLabel, 900);
      }
    } catch {
      prompt("Copy:", text);
    }
  }

  function createNode(key, value, path, isRoot = false) {
    const isArray = Array.isArray(value);
    const isObject = value !== null && typeof value === "object";

    if (isObject) {
      const details = document.createElement("details");
      details.className = "tree-node" + (isRoot ? " root" : "");
      details.dataset.path = path;
      details.dataset.search = `${key} ${path}`.toLowerCase();

      const summary = document.createElement("summary");
      const count = isArray ? value.length : Object.keys(value).length;
      summary.innerHTML = `<span class="key">${escapeHtml(key)}</span> <span class="type-note">${isArray ? "Array" : "Object"} · ${count}</span>`;
      summary.appendChild(makeCopyButton(path || "$", "Path"));
      details.appendChild(summary);

      const entries = isArray ? value.map((item, index) => [String(index), item]) : Object.entries(value);
      for (const [childKey, childValue] of entries) {
        details.appendChild(createNode(childKey, childValue, childPath(path, childKey, isArray), false));
      }
      return details;
    }

    const row = document.createElement("div");
    row.className = "leaf tree-node";
    row.dataset.path = path;
    row.dataset.search = `${key} ${path} ${valueText(value)}`.toLowerCase();

    const keySpan = document.createElement("span");
    keySpan.className = "key";
    keySpan.textContent = key;
    const valueSpan = document.createElement("span");
    valueSpan.className = `value ${valueClass(value)}`;
    valueSpan.textContent = valueText(value);
    const controls = document.createElement("span");
    controls.append(makeCopyButton(path, "Path"), makeCopyButton(valueText(value), "Value"));
    row.append(keySpan, valueSpan, controls);
    return row;
  }

  function renderTree() {
    els.content.innerHTML = "";
    const shell = document.createElement("div");
    shell.className = "tree-shell";
    shell.appendChild(createNode("root", state.currentData, "", true));
    els.content.appendChild(shell);
    applyDepth(Number(els.depthSelect.value));
    applySearch();
  }

  function renderRaw() {
    els.content.innerHTML = "";
    const pre = document.createElement("pre");
    pre.className = "raw";
    pre.textContent = state.currentRaw;
    els.content.appendChild(pre);
    applySearch();
  }

  function renderCurrentView() {
    if (state.currentData === null) return;
    els.modeBadge.textContent = state.view.toUpperCase();
    els.searchInput.placeholder = state.view === "catalog"
      ? (state.catalogModel?.searchPlaceholder || "Search catalog entries")
      : "Search keys, values, or paths";

    if (state.view === "raw") renderRaw();
    else if (state.view === "catalog" && state.catalogModel) renderCatalog();
    else renderTree();
    updateToolbarState();
  }

  function setView(view) {
    if (view === "catalog" && !state.catalogModel) return;
    state.view = view;
    renderCurrentView();
  }

  function updateToolbarState() {
    const loaded = state.currentData !== null;
    const treeView = state.view === "tree";
    els.catalogButton.disabled = !state.catalogModel;
    els.catalogButton.setAttribute("aria-pressed", String(state.view === "catalog"));
    els.treeButton.setAttribute("aria-pressed", String(state.view === "tree"));
    els.rawButton.setAttribute("aria-pressed", String(state.view === "raw"));
    els.expandButton.disabled = !loaded || !treeView;
    els.collapseButton.disabled = !loaded || !treeView;
    els.depthSelect.disabled = !loaded || !treeView;
    updatePreviewButton();
  }

  function applyDepth(maxDepth) {
    const details = [...els.content.querySelectorAll("details.tree-node")];
    for (const node of details) {
      let depth = 0;
      let parent = node.parentElement;
      while (parent && parent !== els.content) {
        if (parent.matches?.("details.tree-node")) depth += 1;
        parent = parent.parentElement;
      }
      node.open = depth < maxDepth;
    }
  }

  function clearMarks(root) {
    root.querySelectorAll("mark").forEach(mark => mark.replaceWith(document.createTextNode(mark.textContent || "")));
    root.querySelectorAll(".search-match").forEach(element => element.classList.remove("search-match"));
  }

  function highlightText(node, query) {
    const walker = document.createTreeWalker(node, NodeFilter.SHOW_TEXT);
    const textNodes = [];
    while (walker.nextNode()) textNodes.push(walker.currentNode);
    for (const textNode of textNodes) {
      const text = textNode.nodeValue || "";
      const index = text.toLowerCase().indexOf(query);
      if (index < 0) continue;
      const before = document.createTextNode(text.slice(0, index));
      const mark = document.createElement("mark");
      mark.textContent = text.slice(index, index + query.length);
      const after = document.createTextNode(text.slice(index + query.length));
      textNode.replaceWith(before, mark, after);
    }
  }

  function applySearch() {
    if (!state.currentData && !state.currentRaw) return;
    const query = els.searchInput.value.trim().toLowerCase();
    state.query = query;

    if (state.view === "catalog") {
      renderCatalogResults();
      return;
    }

    clearMarks(els.content);
    if (!query) {
      if (state.view === "raw") renderRawWithoutSearch();
      return;
    }

    if (state.view === "raw") {
      const pre = els.content.querySelector(".raw");
      const text = state.currentRaw;
      const index = text.toLowerCase().indexOf(query);
      if (index >= 0) {
        const before = document.createTextNode(text.slice(0, index));
        const mark = document.createElement("mark");
        mark.textContent = text.slice(index, index + query.length);
        const after = document.createTextNode(text.slice(index + query.length));
        pre.replaceChildren(before, mark, after);
        mark.scrollIntoView({ block: "center" });
        els.status.textContent = "First raw-text match highlighted.";
      } else {
        els.status.textContent = "No matches.";
      }
      return;
    }

    const nodes = [...els.content.querySelectorAll("[data-search]")];
    const matches = nodes.filter(node => node.dataset.search.includes(query));
    for (const node of matches) {
      node.classList.add("search-match");
      highlightText(node.tagName === "DETAILS" ? node.querySelector(":scope > summary") : node, query);
      let parent = node.parentElement;
      while (parent) {
        if (parent.matches?.("details.tree-node")) parent.open = true;
        parent = parent.parentElement;
      }
    }
    if (matches.length) {
      matches[0].scrollIntoView({ block: "center" });
      els.status.textContent = `${matches.length} matching node${matches.length === 1 ? "" : "s"}.`;
    } else {
      els.status.textContent = "No matches.";
    }
  }

  function renderRawWithoutSearch() {
    const pre = els.content.querySelector(".raw");
    if (pre && pre.textContent !== state.currentRaw) pre.textContent = state.currentRaw;
  }

  function isPlainObject(value) {
    return value !== null && typeof value === "object" && !Array.isArray(value);
  }

  function readDataPath(root, path) {
    if (!path) return root;
    return path.split(".").reduce((value, key) => {
      if (value === null || value === undefined || typeof value !== "object") return undefined;
      return Object.prototype.hasOwnProperty.call(value, key) ? value[key] : undefined;
    }, root);
  }

  function isMeaningful(value) {
    if (value === null || value === undefined) return false;
    if (typeof value === "string") return value.trim().length > 0;
    if (Array.isArray(value)) return value.some(isMeaningful);
    if (isPlainObject(value)) return Object.values(value).some(isMeaningful);
    return true;
  }

  function pickPreviewField(data, paths, basePath = "", validator = isMeaningful) {
    for (const path of paths) {
      const value = readDataPath(data, path);
      if (validator(value)) return { value, path: pathJoin(basePath, path) };
    }
    return null;
  }

  function firstObjectValue(object, keys) {
    if (!isPlainObject(object)) return undefined;
    for (const key of keys) {
      if (Object.prototype.hasOwnProperty.call(object, key) && isMeaningful(object[key])) return object[key];
    }
    return undefined;
  }

  function compactText(value, maxLength = 900) {
    let text = "";
    if (value === null || value === undefined) return "";
    if (typeof value === "string") text = value.trim();
    else if (["number", "boolean"].includes(typeof value)) text = String(value);
    else if (Array.isArray(value)) text = value.map(item => compactText(item, 220)).filter(Boolean).join("; ");
    else if (isPlainObject(value)) {
      const preferred = firstObjectValue(value, ["summary", "description", "text", "value", "title", "name", "purpose", "status", "outcome", "result", "currentState"]);
      if (preferred !== undefined) text = compactText(preferred, maxLength);
      else text = Object.entries(value)
        .filter(([, item]) => ["string", "number", "boolean"].includes(typeof item))
        .slice(0, 6)
        .map(([key, item]) => `${humanizeKey(key)}: ${String(item)}`)
        .join(" · ");
    }
    return text.length > maxLength ? `${text.slice(0, maxLength - 1).trim()}…` : text;
  }

  function humanizeKey(key) {
    return String(key)
      .replace(/[_-]+/g, " ")
      .replace(/([a-z0-9])([A-Z])/g, "$1 $2")
      .replace(/\b\w/g, letter => letter.toUpperCase());
  }

  function formatEntity(value) {
    if (!isMeaningful(value)) return "";
    if (typeof value === "string") return value.trim();
    if (Array.isArray(value)) return value.map(formatEntity).filter(Boolean).slice(0, 4).join(", ");
    if (isPlainObject(value)) {
      const name = compactText(firstObjectValue(value, ["name", "title", "projectName", "productName", "primaryApp", "label"]), 180);
      const id = compactText(firstObjectValue(value, ["projectId", "productId", "documentId", "id"]), 120);
      if (name && id && name !== id) return `${name} (${id})`;
      return name || id;
    }
    return compactText(value, 220);
  }

  function looksLikeDocumentSidecar(data) {
    if (!isPlainObject(data)) return false;
    const documentRecord = isPlainObject(data.document) ? data.document : null;
    const documentKeys = documentRecord
      ? ["documentId", "documentUrl", "documentTitle", "title", "filePath", "fileName"].filter(key => Object.prototype.hasOwnProperty.call(documentRecord, key)).length
      : 0;
    const structuralKeys = ["sections", "publication", "projectContext", "subject", "narrative", "supervisorView", "workCoverage", "projectContribution", "technical", "technicalContent", "provenance"]
      .filter(key => Object.prototype.hasOwnProperty.call(data, key)).length;
    const schemaText = String(data.schemaVersion || data.schema || "").toLowerCase();
    const explicitType = String(data.recordType || data.metadataType || documentRecord?.recordType || documentRecord?.documentType || "").toLowerCase();
    return documentKeys >= 2 || (documentKeys >= 1 && structuralKeys >= 1) || schemaText.includes("sidecar") || explicitType.includes("sidecar");
  }

  function buildSidecarPreview(data, basePath = "") {
    if (!looksLikeDocumentSidecar(data)) return null;
    const stringField = paths => pickPreviewField(data, paths, basePath, value => typeof value === "string" && value.trim().length > 0);
    return {
      title: stringField(["preview.title", "document.title", "document.documentTitle", "documentTitle", "title", "publication.listingTitle", "listing.title", "googleSites.title", "metadata.title"]) || { value: "Untitled document", path: basePath },
      subtitle: stringField(["preview.subtitle", "document.subtitle", "document.headline", "headline", "publication.subtitle", "listing.subtitle"]),
      summary: pickPreviewField(data, ["preview.summary", "document.executiveSummary", "executiveSummary", "document.summary", "summary", "abstract", "document.description", "description", "subject.description", "workCoverage.coverageDescription", "publication.listingDescription", "listing.description", "googleSites.listingDescription"], basePath),
      documentType: pickPreviewField(data, ["document.documentType", "document.type", "documentType", "recordType", "type"], basePath),
      date: pickPreviewField(data, ["document.publicationDate", "document.publishedDate", "document.date", "document.createdTimestamp", "publication.publishedAt", "publication.publicationDate", "publication.date", "publishedDate", "createdTimestamp", "date"], basePath),
      documentId: pickPreviewField(data, ["document.documentId", "documentId", "id"], basePath),
      documentUrl: stringField(["document.documentUrl", "document.url", "publication.canonicalUrl", "publication.documentUrl", "canonicalUrl", "links.fullDocument", "links.document", "url"]),
      filePath: stringField(["document.filePath", "document.fileName", "filePath", "fileName", "metadata.filePath"]),
      project: pickPreviewField(data, ["projectContext.primaryProject", "primaryProject", "project", "document.project", "subject.primaryProject", "subject.projectName", "subject.primaryApp", "projectName"], basePath),
      purpose: pickPreviewField(data, ["preview.purpose", "workCoverage.purpose", "document.purpose", "purpose", "projectContribution.purpose", "subject.mainFocus"], basePath),
      supervisorBrief: pickPreviewField(data, ["supervisorView.brief", "supervisorView.summary", "supervisorBrief", "audienceViews.supervisor.brief", "audiences.supervisor.brief", "publication.supervisorBrief"], basePath),
      outcomes: pickPreviewField(data, ["preview.outcomes", "keyOutcomes", "outcomes", "projectContribution.outcomes", "projectContribution.result", "resultingCapabilities", "currentState.capabilities", "workPerformed.outcomes", "workCoverage.completed", "keywords"], basePath),
      currentState: pickPreviewField(data, ["preview.currentState", "currentState.summary", "currentState", "resultingState", "projectContribution.currentState", "status"], basePath),
      decisions: pickPreviewField(data, ["preview.decisions", "keyDecisions", "decisions", "narrative.decisions", "designDecisions"], basePath),
      nextSteps: pickPreviewField(data, ["preview.nextSteps", "nextSteps", "roadmap.nextSteps", "projectContribution.nextSteps", "bootstrapNextSteps", "currentState.nextSteps"], basePath),
      topics: pickPreviewField(data, ["preview.topics", "topics", "tags", "subjectClassification.topics", "classification.topics", "document.topics", "publication.keywords", "subjects", "keywords"], basePath),
      sections: pickPreviewField(data, ["document.sections", "sections", "content.sections", "narrative.sections"], basePath),
      schemaVersion: pickPreviewField(data, ["schemaVersion", "metadata.schemaVersion", "document.schemaVersion"], basePath),
      previewMode: stringField(["profile.previewMode", "profile.profileType"]),
      workflowIdentity: pickPreviewField(data, ["workflowIdentity"], basePath),
      workflowMetrics: pickPreviewField(data, ["workflowMetrics"], basePath),
      workflowStateModel: pickPreviewField(data, ["stateModel"], basePath),
      workflowPhases: pickPreviewField(data, ["phases"], basePath),
      workflowSteps: pickPreviewField(data, ["steps"], basePath),
      workflowInstructionSets: pickPreviewField(data, ["instructionSets"], basePath),
      workflowArtifactModel: pickPreviewField(data, ["artifactModel"], basePath),
      workflowHumanReviewModel: pickPreviewField(data, ["humanReviewModel"], basePath),
      workflowValidationModel: pickPreviewField(data, ["validationModel"], basePath),
      workflowClosureModel: pickPreviewField(data, ["closureModel"], basePath),
      workflowDesignDecisions: pickPreviewField(data, ["designDecisions"], basePath),
      sourceData: data,
      basePath,
    };
  }

  function looksLikeChemicalEntry(data) {
    return isPlainObject(data) && (
      isPlainObject(data.product_info) ||
      isPlainObject(data.manufacturer_info_sheet) ||
      isPlainObject(data.sds_info_sheet) ||
      Object.prototype.hasOwnProperty.call(data, "catalog_entry_id")
    );
  }

  function looksLikeChemicalCatalog(data) {
    if (!isPlainObject(data) || !Array.isArray(data.entries)) return false;
    const schemaName = String(data.schema?.schema_name || data.schema_name || "").toLowerCase();
    const catalogId = String(data.catalog_metadata?.catalog_id || data.catalog?.catalog_id || data.catalog?.catalogId || "").toLowerCase();
    return schemaName.includes("chemical_product_catalog") ||
      catalogId.includes("chemical-product-catalog") ||
      isPlainObject(data.entry_template) ||
      data.entries.some(looksLikeChemicalEntry);
  }

  function buildChemicalPreview(data, basePath = "") {
    if (!looksLikeChemicalEntry(data)) return null;
    const field = paths => pickPreviewField(data, paths, basePath);
    const stringField = paths => pickPreviewField(data, paths, basePath, value => typeof value === "string" && value.trim().length > 0);
    return {
      previewKind: "chemical",
      title: stringField([
        "manufacturer_info_sheet.identity.canonical_product_name",
        "sds_info_sheet.sds_identity.official_product_name",
        "product_info.workplace_product.inventory_listed_name",
        "catalog_entry_id"
      ]) || { value: "Untitled chemical product", path: basePath },
      subtitle: field([
        "manufacturer_info_sheet.identity.formulation_description",
        "manufacturer_info_sheet.identity.package_description",
        "product_info.department_context.container_or_dispenser"
      ]),
      manufacturer: field([
        "manufacturer_info_sheet.identity.manufacturer",
        "sds_info_sheet.sds_identity.manufacturer",
        "product_info.workplace_product.inventory_listed_manufacturer"
      ]),
      form: field([
        "manufacturer_info_sheet.identity.form_type",
        "sds_info_sheet.sds_identity.form_type",
        "product_info.department_context.carried_form"
      ]),
      status: field(["record_verification.overall_status", "entry_status"]),
      inventoryId: field(["product_info.workplace_product.inventory_product_id"]),
      inventoryName: field(["product_info.workplace_product.inventory_listed_name"]),
      inventoryCode: field(["product_info.workplace_product.inventory_listed_product_code"]),
      inventoryCodeStatus: field(["product_info.workplace_product.inventory_identifier_status"]),
      containerSize: field(["product_info.workplace_product.inventory_container_size"]),
      inventoryUnit: field(["product_info.workplace_product.inventory_unit"]),
      category: field(["product_info.department_context.department_category"]),
      workUses: field(["product_info.department_context.work_uses"]),
      workLocations: field(["product_info.department_context.work_locations"]),
      canonicalName: field(["manufacturer_info_sheet.identity.canonical_product_name"]),
      brand: field(["manufacturer_info_sheet.identity.brand"]),
      productLine: field(["manufacturer_info_sheet.identity.product_line"]),
      packageDescription: field(["manufacturer_info_sheet.identity.package_description"]),
      dispensingSystem: field(["manufacturer_info_sheet.identity.dispensing_system"]),
      manufacturerIdentifiers: field(["manufacturer_info_sheet.identity.manufacturer_identifiers"]),
      officialProductRecord: field(["manufacturer_info_sheet.official_product_record"]),
      officialProductUrl: stringField(["manufacturer_info_sheet.official_product_record.source_url"]),
      manufacturerIdentityStatus: field(["manufacturer_info_sheet.identity_verification.status"]),
      safetyReferenceType: field(["manufacturer_info_sheet.safety_reference.reference_type"]),
      safetyReferenceLabel: field(["manufacturer_info_sheet.safety_reference.reference_label"]),
      manufacturerSdsUrl: stringField(["manufacturer_info_sheet.safety_reference.official_sds_url"]),
      manufacturerSdsId: field(["manufacturer_info_sheet.safety_reference.official_sds_identifier"]),
      casNumbers: field(["manufacturer_info_sheet.safety_reference.cas_numbers_referenced"]),
      sdsProductName: field(["sds_info_sheet.sds_identity.official_product_name"]),
      sdsId: field(["sds_info_sheet.sds_identity.sds_identifier"]),
      sdsRevision: field(["sds_info_sheet.sds_identity.revision_date"]),
      sdsVersion: field(["sds_info_sheet.sds_identity.version"]),
      sdsDilution: field(["sds_info_sheet.sds_identity.formulation_or_dilution"]),
      sdsJurisdiction: field(["sds_info_sheet.sds_identity.jurisdiction"]),
      sdsLanguage: field(["sds_info_sheet.sds_identity.language"]),
      officialSdsUrl: stringField(["sds_info_sheet.official_sds_record.source_url"]),
      sdsMatchStatus: field(["sds_info_sheet.product_match.status"]),
      coverage: field(["sds_info_sheet.coverage"]),
      sections: field(["sds_info_sheet.sections"]),
      recordVerification: field(["record_verification"]),
      recordHistory: field(["record_history"]),
      catalogEntryId: field(["catalog_entry_id"]),
      sourceData: data,
      basePath,
    };
  }

  function looksLikeCatalog(data) {
    if (!isPlainObject(data) || !Array.isArray(data.entries)) return false;
    const schemaName = String(data.schema?.schema_name || data.schema_name || "").toLowerCase();
    return isPlainObject(data.catalog) ||
      isPlainObject(data.catalog_metadata) ||
      schemaName.includes("catalog") ||
      data.entries.some(entry => looksLikeDocumentSidecar(entry) || looksLikeChemicalEntry(entry));
  }

  function fieldText(field, formatter = compactText) {
    return field && isMeaningful(field.value) ? formatter(field.value) : "";
  }

  function extractYear(value) {
    const match = String(value || "").match(/\b(19|20)\d{2}\b/);
    return match ? match[0] : "";
  }

  function buildCatalogModel(data) {
    if (!looksLikeCatalog(data)) return null;
    const chemicalCatalog = looksLikeChemicalCatalog(data);
    const catalogRecord = chemicalCatalog
      ? (isPlainObject(data.catalog_metadata) ? data.catalog_metadata : {})
      : (isPlainObject(data.catalog) ? data.catalog : {});

    const entries = data.entries.map((entry, index) => {
      if (chemicalCatalog) {
        const preview = buildChemicalPreview(entry, `entries[${index}]`) || {
          previewKind: "chemical",
          title: { value: `Chemical entry ${index + 1}`, path: `entries[${index}]` },
          sourceData: entry,
          basePath: `entries[${index}]`
        };
        const title = fieldText(preview.title) || `Chemical entry ${index + 1}`;
        const manufacturer = fieldText(preview.manufacturer);
        const form = fieldText(preview.form);
        const status = fieldText(preview.status);
        const date = fieldText(preview.sdsRevision) || fieldText(preview.recordHistory);
        const headlineParts = [
          fieldText(preview.subtitle),
          fieldText(preview.inventoryName),
          fieldText(preview.sdsId) ? `SDS ${fieldText(preview.sdsId)}` : ""
        ].filter(Boolean);
        const topics = [
          ...previewListItems(preview.workUses?.value, preview.workUses?.path || "", 5).map(item => item.title),
          ...previewListItems(preview.casNumbers?.value, preview.casNumbers?.path || "", 3).map(item => item.title)
        ];
        return {
          index,
          entry,
          preview,
          title,
          headline: headlineParts.join(" · "),
          project: manufacturer,
          type: form,
          year: status,
          date,
          topics,
          searchBlob: `${title} ${headlineParts.join(" ")} ${manufacturer} ${form} ${status} ${date} ${topics.join(" ")} ${JSON.stringify(entry)}`.toLowerCase(),
        };
      }

      const preview = buildSidecarPreview(entry, `entries[${index}]`) || {
        title: { value: `Entry ${index + 1}`, path: `entries[${index}]` }
      };
      const title = fieldText(preview.title) || `Entry ${index + 1}`;
      const headline = fieldText(preview.subtitle) || fieldText(preview.summary);
      const project = fieldText(preview.project, formatEntity);
      const type = fieldText(preview.documentType);
      const date = fieldText(preview.date);
      const topics = previewListItems(preview.topics?.value, preview.topics?.path || "", 8).map(item => item.title);
      return {
        index,
        entry,
        preview,
        title,
        headline,
        project,
        type,
        date,
        year: extractYear(date),
        topics,
        searchBlob: `${title} ${headline} ${project} ${type} ${date} ${topics.join(" ")} ${JSON.stringify(entry)}`.toLowerCase(),
      };
    });

    if (chemicalCatalog) {
      return {
        kind: "chemical",
        eyebrow: "Chemical product catalog",
        title: compactText(catalogRecord.title || "Klinswork Chemical Product Catalog", 250),
        description: compactText(catalogRecord.purpose || catalogRecord.description || "", 900),
        generated: compactText(catalogRecord.updated_at || catalogRecord.created_at || "", 120),
        entries,
        projects: [...new Set(entries.map(entry => entry.project).filter(Boolean))].sort(),
        types: [...new Set(entries.map(entry => entry.type).filter(Boolean))].sort(),
        years: [...new Set(entries.map(entry => entry.year).filter(Boolean))].sort(),
        filterLabels: {
          project: "Manufacturer",
          type: "Form",
          year: "Verification status"
        },
        allLabels: {
          project: "All manufacturers",
          type: "All forms",
          year: "All statuses"
        },
        cardMetaLabels: {
          date: "SDS revision",
          project: "Manufacturer",
          type: "Form",
          year: "Status"
        },
        sortLabels: {
          newest: "Newest SDS revision",
          oldest: "Oldest SDS revision"
        },
        searchPlaceholder: "Search chemical names, manufacturers, forms, SDS IDs, CAS numbers, or text",
        emptyMessage: "This chemical catalog shell is valid, but no product entries have been appended yet."
      };
    }

    return {
      kind: "document",
      eyebrow: "Catalog browser",
      title: compactText(catalogRecord.title || catalogRecord.catalogTitle || "Document catalog", 250),
      description: compactText(catalogRecord.description || catalogRecord.summary || "", 900),
      generated: compactText(catalogRecord.generatedTimestamp || catalogRecord.updatedTimestamp || "", 120),
      entries,
      projects: [...new Set(entries.map(entry => entry.project).filter(Boolean))].sort(),
      types: [...new Set(entries.map(entry => entry.type).filter(Boolean))].sort(),
      years: [...new Set(entries.map(entry => entry.year).filter(Boolean))].sort().reverse(),
      filterLabels: {
        project: "Project",
        type: "Document type",
        year: "Year"
      },
      allLabels: {
        project: "All projects",
        type: "All types",
        year: "All years"
      },
      cardMetaLabels: {
        date: "Date",
        project: "Project",
        type: "Type",
        year: "Year"
      },
      sortLabels: {
        newest: "Newest first",
        oldest: "Oldest first"
      },
      searchPlaceholder: "Search catalog titles, projects, topics, or text",
      emptyMessage: "No catalog entries match the current search and filters."
    };
  }

  function renderCatalog() {
    const model = state.catalogModel;
    els.content.innerHTML = "";
    const shell = document.createElement("div");
    shell.className = "catalog-shell";

    const header = document.createElement("section");
    header.className = "catalog-header";
    header.innerHTML = `
      <p class="catalog-eyebrow">${escapeHtml(model.eyebrow || "Catalog browser")}</p>
      <h2 class="catalog-title">${escapeHtml(model.title)}</h2>
      ${model.description ? `<p class="catalog-description">${escapeHtml(model.description)}</p>` : ""}
      <div class="catalog-stats">
        <span class="preview-chip">Entries: ${model.entries.length}</span>
        ${model.generated ? `<span class="preview-chip">Updated: ${escapeHtml(model.generated)}</span>` : ""}
        <span class="preview-chip">Source: ${escapeHtml(state.currentFile?.path || "")}</span>
      </div>
    `;
    shell.appendChild(header);

    const labels = model.filterLabels || {};
    const allLabels = model.allLabels || {};
    const sortLabels = model.sortLabels || {};
    const controls = document.createElement("section");
    controls.className = "catalog-controls";
    controls.innerHTML = `
      <div class="catalog-control"><label for="catalogProject">${escapeHtml(labels.project || "Project")}</label><select id="catalogProject"><option value="">${escapeHtml(allLabels.project || "All projects")}</option></select></div>
      <div class="catalog-control"><label for="catalogType">${escapeHtml(labels.type || "Type")}</label><select id="catalogType"><option value="">${escapeHtml(allLabels.type || "All types")}</option></select></div>
      <div class="catalog-control"><label for="catalogYear">${escapeHtml(labels.year || "Year")}</label><select id="catalogYear"><option value="">${escapeHtml(allLabels.year || "All years")}</option></select></div>
      <div class="catalog-control"><label for="catalogSort">Sort</label><select id="catalogSort"><option value="newest">${escapeHtml(sortLabels.newest || "Newest first")}</option><option value="oldest">${escapeHtml(sortLabels.oldest || "Oldest first")}</option><option value="title">Title</option><option value="catalog">Catalog order</option></select></div>
    `;
    shell.appendChild(controls);

    const list = document.createElement("div");
    list.className = "catalog-list";
    list.id = "catalogList";
    shell.appendChild(list);
    els.content.appendChild(shell);

    fillSelect(document.getElementById("catalogProject"), model.projects, state.catalogProject);
    fillSelect(document.getElementById("catalogType"), model.types, state.catalogType);
    fillSelect(document.getElementById("catalogYear"), model.years, state.catalogYear);
    document.getElementById("catalogSort").value = state.catalogSort;

    document.getElementById("catalogProject").addEventListener("change", event => { state.catalogProject = event.target.value; renderCatalogResults(); });
    document.getElementById("catalogType").addEventListener("change", event => { state.catalogType = event.target.value; renderCatalogResults(); });
    document.getElementById("catalogYear").addEventListener("change", event => { state.catalogYear = event.target.value; renderCatalogResults(); });
    document.getElementById("catalogSort").addEventListener("change", event => { state.catalogSort = event.target.value; renderCatalogResults(); });
    renderCatalogResults();
  }

  function fillSelect(select, values, selected) {
    for (const value of values) {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = value;
      option.selected = value === selected;
      select.appendChild(option);
    }
  }

  function catalogSortValue(entry) {
    const parsed = Date.parse(entry.date);
    return Number.isFinite(parsed) ? parsed : 0;
  }

  function renderCatalogResults() {
    if (!state.catalogModel || state.view !== "catalog") return;
    const list = document.getElementById("catalogList");
    if (!list) return;
    const query = els.searchInput.value.trim().toLowerCase();
    let entries = state.catalogModel.entries.filter(entry =>
      (!query || entry.searchBlob.includes(query)) &&
      (!state.catalogProject || entry.project === state.catalogProject) &&
      (!state.catalogType || entry.type === state.catalogType) &&
      (!state.catalogYear || entry.year === state.catalogYear)
    );

    entries = [...entries].sort((a, b) => {
      if (state.catalogSort === "title") return a.title.localeCompare(b.title, undefined, { numeric: true });
      if (state.catalogSort === "catalog") return a.index - b.index;
      if (state.catalogSort === "oldest") return catalogSortValue(a) - catalogSortValue(b);
      return catalogSortValue(b) - catalogSortValue(a);
    });

    list.innerHTML = "";
    if (!entries.length) {
      const emptyMessage = state.catalogModel.entries.length
        ? "No catalog entries match the current search and filters."
        : (state.catalogModel.emptyMessage || "This catalog contains no appended entries.");
      list.innerHTML = `<div class="catalog-empty">${escapeHtml(emptyMessage)}</div>`;
      els.status.textContent = state.catalogModel.entries.length ? "No catalog entries match." : "Catalog contains no appended entries.";
      return;
    }

    for (const entry of entries) {
      const card = document.createElement("article");
      card.className = "catalog-card" + (state.selectedCatalogIndex === entry.index ? " selected" : "");
      card.tabIndex = 0;
      card.dataset.catalogIndex = String(entry.index);

      const body = document.createElement("div");
      const title = document.createElement("h3");
      title.className = "catalog-card-title";
      title.textContent = entry.title;
      body.appendChild(title);
      if (entry.headline) {
        const headline = document.createElement("p");
        headline.className = "catalog-card-headline";
        headline.textContent = entry.headline;
        body.appendChild(headline);
      }
      const meta = document.createElement("div");
      meta.className = "catalog-card-meta";
      const metaLabels = state.catalogModel.cardMetaLabels || {};
      const metaRows = [
        [metaLabels.date || "Date", entry.date],
        [metaLabels.project || "Project", entry.project],
        [metaLabels.type || "Type", entry.type],
        [metaLabels.year || "Year", state.catalogModel.kind === "chemical" ? entry.year : ""]
      ];
      for (const [label, value] of metaRows) {
        if (!value) continue;
        const chip = document.createElement("span");
        chip.className = "preview-chip";
        chip.textContent = `${label}: ${value}`;
        meta.appendChild(chip);
      }
      if (meta.children.length) body.appendChild(meta);
      if (entry.topics.length) {
        const topics = document.createElement("div");
        topics.className = "catalog-card-topics";
        for (const topic of entry.topics.slice(0, 6)) {
          const chip = document.createElement("span");
          chip.className = "preview-topic";
          chip.textContent = topic;
          topics.appendChild(chip);
        }
        body.appendChild(topics);
      }

      const actions = document.createElement("div");
      actions.className = "catalog-card-actions";
      const source = document.createElement("button");
      source.className = "catalog-source-button";
      source.textContent = "JSON";
      source.title = `Reveal entries[${entry.index}] in the JSON tree`;
      source.addEventListener("click", event => {
        event.stopPropagation();
        revealJsonPath(`entries[${entry.index}]`);
      });
      actions.appendChild(source);
      card.append(body, actions);
      card.addEventListener("click", () => selectCatalogEntry(entry.index, true));
      card.addEventListener("keydown", event => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          selectCatalogEntry(entry.index, true);
        }
      });
      list.appendChild(card);
    }
    els.status.textContent = `${entries.length} of ${state.catalogModel.entries.length} catalog entries shown.`;
  }

  function selectCatalogEntry(index, rerenderList = true) {
    if (!state.catalogModel || index === null || index === undefined) {
      state.selectedCatalogIndex = null;
      state.previewModel = null;
      state.previewContext = "catalog";
      setPreviewOpen(false);
      return;
    }
    const entry = state.catalogModel.entries.find(item => item.index === Number(index));
    if (!entry) return;
    state.selectedCatalogIndex = entry.index;
    state.previewModel = entry.preview;
    state.previewContext = "catalog";
    setPreviewOpen(true);
    if (rerenderList) renderCatalogResults();
    els.status.textContent = `Catalog entry ${entry.index + 1}: ${entry.title}`;
  }

  function safeDocumentUrl(field) {
    if (!field || typeof field.value !== "string") return "";
    try {
      const url = new URL(field.value);
      return ["http:", "https:"].includes(url.protocol) ? url.href : "";
    } catch {
      return "";
    }
  }

  function makePreviewSourceButton(path) {
    if (!path) return null;
    const button = document.createElement("button");
    button.className = "preview-source";
    button.type = "button";
    button.textContent = path;
    button.title = `Show ${path} in the JSON tree`;
    button.addEventListener("click", () => revealJsonPath(path));
    return button;
  }

  function previewListItems(value, basePath = "", limit = 8) {
    if (!isMeaningful(value)) return [];
    const source = Array.isArray(value)
      ? value.map((item, index) => ({ key: String(index), item, path: `${basePath}[${index}]` }))
      : isPlainObject(value)
        ? Object.entries(value).map(([key, item]) => ({ key, item, path: basePath ? `${basePath}.${key}` : key }))
        : [{ key: "", item: value, path: basePath }];
    const items = [];
    for (const entry of source) {
      if (!isMeaningful(entry.item)) continue;
      if (["string", "number", "boolean"].includes(typeof entry.item)) {
        items.push({ title: compactText(entry.item, 280), detail: "", path: entry.path });
      } else if (isPlainObject(entry.item)) {
        const titleValue = firstObjectValue(entry.item, ["title", "name", "label", "heading", "sectionTitle", "decision", "outcome", "capability", "step", "status", "change", "topic"]);
        const detailValue = firstObjectValue(entry.item, ["summary", "contentSummary", "description", "text", "rationale", "reason", "result", "impact", "currentState", "details"]);
        items.push({
          title: compactText(titleValue, 280) || humanizeKey(entry.key),
          detail: compactText(detailValue, 480),
          path: entry.path,
        });
      } else if (Array.isArray(entry.item)) {
        items.push({ title: humanizeKey(entry.key), detail: compactText(entry.item, 420), path: entry.path });
      }
      if (items.length >= limit) break;
    }
    return items;
  }

  function makePreviewSection(title, field, options = {}) {
    if (!field || !isMeaningful(field.value)) return null;
    const section = document.createElement("section");
    section.className = `preview-section${options.className ? ` ${options.className}` : ""}`;
    const header = document.createElement("div");
    header.className = "preview-section-header";
    const heading = document.createElement("h3");
    heading.textContent = title;
    header.appendChild(heading);
    const sourceButton = makePreviewSourceButton(field.path);
    if (sourceButton) header.appendChild(sourceButton);
    section.appendChild(header);

    if (options.kind === "topics") {
      const list = document.createElement("div");
      list.className = "preview-topic-list";
      for (const item of previewListItems(field.value, field.path, 16)) {
        const chip = document.createElement("span");
        chip.className = "preview-topic";
        chip.textContent = item.title;
        chip.title = item.path || "";
        list.appendChild(chip);
      }
      section.appendChild(list);
      return section;
    }

    if (options.kind === "list") {
      const items = previewListItems(field.value, field.path, options.limit || 8);
      const list = document.createElement(options.ordered ? "ol" : "ul");
      for (const item of items) {
        const listItem = document.createElement("li");
        listItem.textContent = item.title;
        if (item.detail && item.detail !== item.title) {
          const detail = document.createElement("span");
          detail.className = "preview-item-detail";
          detail.textContent = item.detail;
          listItem.appendChild(detail);
        }
        if (item.path) {
          listItem.title = `Source: ${item.path}`;
          listItem.addEventListener("dblclick", () => revealJsonPath(item.path));
        }
        list.appendChild(listItem);
      }
      section.appendChild(list);
      return section;
    }

    const paragraph = document.createElement("p");
    paragraph.textContent = compactText(field.value, options.maxLength || 1300);
    section.appendChild(paragraph);
    return section;
  }

  function appendMetaChip(container, label, field, formatter = compactText) {
    if (!field || !isMeaningful(field.value)) return;
    const value = formatter(field.value);
    if (!value) return;
    const chip = document.createElement("span");
    chip.className = "preview-chip";
    chip.textContent = `${label}: ${value}`;
    if (field.path) {
      chip.title = `Source: ${field.path}`;
      chip.addEventListener("dblclick", () => revealJsonPath(field.path));
    }
    container.appendChild(chip);
  }


  function isWorkflowPreview(model) {
    if (!model) return false;
    const mode = fieldText(model.previewMode).toLowerCase();
    const type = fieldText(model.documentType).toLowerCase();
    return mode === "workflow-specification" || type === "workflow-specification" || Boolean(model.workflowSteps && model.workflowPhases);
  }

  function workflowSourcePath(model, suffix) {
    return pathJoin(model.basePath || "", suffix);
  }

  function makeWorkflowSection(title, sourcePath = "") {
    const section = document.createElement("section");
    section.className = "preview-section workflow-section";
    const header = document.createElement("div");
    header.className = "preview-section-header";
    const heading = document.createElement("h3");
    heading.textContent = title;
    header.appendChild(heading);
    const sourceButton = makePreviewSourceButton(sourcePath);
    if (sourceButton) header.appendChild(sourceButton);
    section.appendChild(header);
    return section;
  }

  function appendWorkflowMetric(container, label, value, sourcePath = "") {
    if (!isMeaningful(value)) return;
    const metric = document.createElement("div");
    metric.className = "workflow-metric";
    const number = document.createElement("strong");
    number.textContent = compactText(value, 80);
    const caption = document.createElement("span");
    caption.textContent = label;
    metric.append(number, caption);
    if (sourcePath) {
      metric.title = `Source: ${sourcePath}`;
      metric.addEventListener("dblclick", () => revealJsonPath(sourcePath));
    }
    container.appendChild(metric);
  }

  function appendWorkflowTextList(container, title, values) {
    if (!Array.isArray(values) || !values.some(isMeaningful)) return;
    const block = document.createElement("section");
    block.className = "workflow-detail-block";
    const heading = document.createElement("h4");
    heading.textContent = title;
    const list = document.createElement("ul");
    for (const value of values.filter(isMeaningful)) {
      const item = document.createElement("li");
      item.textContent = compactText(value, 700);
      list.appendChild(item);
    }
    block.append(heading, list);
    container.appendChild(block);
  }

  function renderWorkflowOverview(model) {
    const identity = isPlainObject(model.workflowIdentity?.value) ? model.workflowIdentity.value : {};
    const metrics = isPlainObject(model.workflowMetrics?.value) ? model.workflowMetrics.value : {};
    const section = makeWorkflowSection("Workflow overview", model.workflowIdentity?.path || model.workflowMetrics?.path || "");

    const overview = document.createElement("div");
    overview.className = "workflow-overview-line";
    const start = compactText(identity.initialState, 140);
    const finish = compactText(identity.finalState, 140);
    if (start) {
      const startChip = document.createElement("span");
      startChip.className = "workflow-state-chip initial";
      startChip.textContent = `Start: ${start}`;
      overview.appendChild(startChip);
    }
    if (start && finish) {
      const arrow = document.createElement("span");
      arrow.className = "workflow-arrow";
      arrow.textContent = "→";
      overview.appendChild(arrow);
    }
    if (finish) {
      const finishChip = document.createElement("span");
      finishChip.className = "workflow-state-chip final";
      finishChip.textContent = `Finish: ${finish}`;
      overview.appendChild(finishChip);
    }
    if (identity.currentStatus) {
      const statusChip = document.createElement("span");
      statusChip.className = "preview-chip";
      statusChip.textContent = `Status: ${compactText(identity.currentStatus, 120)}`;
      overview.appendChild(statusChip);
    }
    if (overview.children.length) section.appendChild(overview);

    const metricGrid = document.createElement("div");
    metricGrid.className = "workflow-metrics";
    const metricDefinitions = [
      ["States", metrics.stateCount, "workflowMetrics.stateCount"],
      ["Phases", metrics.phaseCount, "workflowMetrics.phaseCount"],
      ["Steps", metrics.stepCount, "workflowMetrics.stepCount"],
      ["Instruction sets", metrics.instructionSetCount, "workflowMetrics.instructionSetCount"],
      ["Human-review steps", metrics.humanReviewStepCount, "workflowMetrics.humanReviewStepCount"],
      ["High automation potential", metrics.automatableStepCount, "workflowMetrics.automatableStepCount"],
      ["Validation rules", metrics.validationRuleCount, "workflowMetrics.validationRuleCount"],
      ["Authoritative artifacts", metrics.authoritativeArtifactCount, "workflowMetrics.authoritativeArtifactCount"],
    ];
    for (const [label, value, path] of metricDefinitions) appendWorkflowMetric(metricGrid, label, value, workflowSourcePath(model, path));
    if (metricGrid.children.length) section.appendChild(metricGrid);
    return section;
  }

  function renderWorkflowStates(model) {
    const stateModel = isPlainObject(model.workflowStateModel?.value) ? model.workflowStateModel.value : {};
    const states = Array.isArray(stateModel.states) ? stateModel.states : [];
    if (!states.length) return null;
    const section = makeWorkflowSection("Workflow states", workflowSourcePath(model, "stateModel.states"));
    const path = document.createElement("div");
    path.className = "workflow-state-path";
    states.forEach((stateRecord, index) => {
      if (!isPlainObject(stateRecord)) return;
      const chip = document.createElement("span");
      chip.className = `workflow-state-chip${stateRecord.isInitial ? " initial" : ""}${stateRecord.isFinal ? " final" : ""}`;
      chip.textContent = compactText(stateRecord.stateId || stateRecord.title || `State ${index + 1}`, 180);
      chip.title = compactText(stateRecord.description, 500) || `Source: ${workflowSourcePath(model, `stateModel.states[${index}]`)}`;
      chip.addEventListener("dblclick", () => revealJsonPath(workflowSourcePath(model, `stateModel.states[${index}]`)));
      path.appendChild(chip);
    });
    section.appendChild(path);
    return section;
  }

  function buildWorkflowStep(step, model, stepIndex) {
    const details = document.createElement("details");
    details.className = "workflow-step";
    const sourcePath = workflowSourcePath(model, `steps[${stepIndex}]`);
    details.dataset.sourcePath = sourcePath;

    const summary = document.createElement("summary");
    const number = document.createElement("span");
    number.className = "workflow-step-number";
    number.textContent = compactText(step.stepNumber ?? stepIndex + 1, 20);
    const heading = document.createElement("div");
    heading.className = "workflow-step-heading";
    const title = document.createElement("span");
    title.className = "workflow-step-title";
    title.textContent = compactText(step.title || step.stepId || `Step ${stepIndex + 1}`, 350);
    const transition = document.createElement("span");
    transition.className = "workflow-step-transition";
    transition.textContent = `${compactText(step.stateBefore || "—", 100)} → ${compactText(step.stateAfter || "—", 100)}`;
    heading.append(title, transition);

    const tags = document.createElement("div");
    tags.className = "workflow-step-tags";
    if (step.automationPotential) {
      const tag = document.createElement("span");
      tag.className = "workflow-step-tag";
      tag.textContent = `Automation: ${compactText(step.automationPotential, 80)}`;
      tags.appendChild(tag);
    }
    if (step.humanReviewRequired) {
      const tag = document.createElement("span");
      tag.className = "workflow-step-tag review";
      tag.textContent = step.approvalAuthority ? `Human review: ${compactText(step.approvalAuthority, 90)}` : "Human review required";
      tags.appendChild(tag);
    }
    if (tags.children.length) heading.appendChild(tags);
    summary.append(number, heading);
    summary.title = `Source: ${sourcePath}`;
    summary.addEventListener("dblclick", event => {
      event.preventDefault();
      event.stopPropagation();
      revealJsonPath(sourcePath);
    });
    details.appendChild(summary);

    const body = document.createElement("div");
    body.className = "workflow-step-body";
    if (step.purpose) {
      const purpose = document.createElement("p");
      purpose.className = "workflow-step-purpose";
      purpose.textContent = compactText(step.purpose, 1000);
      body.appendChild(purpose);
    }
    const grid = document.createElement("div");
    grid.className = "workflow-detail-grid";
    appendWorkflowTextList(grid, "Inputs", step.inputs);
    appendWorkflowTextList(grid, "Actions", step.actions);
    appendWorkflowTextList(grid, "Outputs", step.outputs);
    appendWorkflowTextList(grid, "Validation", step.validation);
    appendWorkflowTextList(grid, "Blocking conditions", step.blockingConditions);
    appendWorkflowTextList(grid, "Exception rules", step.exceptionRules);
    if (grid.children.length) body.appendChild(grid);
    if (step.nextStep !== null && step.nextStep !== undefined) {
      const next = document.createElement("div");
      next.className = "workflow-next-step";
      next.textContent = `Next step: ${compactText(step.nextStep, 80)}`;
      body.appendChild(next);
    }
    details.appendChild(body);
    return details;
  }

  function renderWorkflowPhasesAndSteps(model) {
    const phases = Array.isArray(model.workflowPhases?.value) ? model.workflowPhases.value : [];
    const steps = Array.isArray(model.workflowSteps?.value) ? model.workflowSteps.value : [];
    if (!phases.length && !steps.length) return null;
    const section = makeWorkflowSection("Workflow phases and steps", model.workflowSteps?.path || model.workflowPhases?.path || "");

    const controls = document.createElement("div");
    controls.className = "workflow-controls";
    const expandSteps = document.createElement("button");
    expandSteps.type = "button";
    expandSteps.textContent = "Expand all step details";
    const collapseSteps = document.createElement("button");
    collapseSteps.type = "button";
    collapseSteps.textContent = "Collapse step details";
    const expandPhases = document.createElement("button");
    expandPhases.type = "button";
    expandPhases.textContent = "Open all phases";
    const collapsePhases = document.createElement("button");
    collapsePhases.type = "button";
    collapsePhases.textContent = "Close all phases";
    controls.append(expandSteps, collapseSteps, expandPhases, collapsePhases);
    section.appendChild(controls);

    const phaseList = document.createElement("div");
    phaseList.className = "workflow-phase-list";
    const renderPhase = (phase, phaseIndex, phaseSteps) => {
      const phaseDetails = document.createElement("details");
      phaseDetails.className = "workflow-phase";
      phaseDetails.open = true;
      const phasePath = phases.length ? workflowSourcePath(model, `phases[${phaseIndex}]`) : model.workflowSteps?.path || "";
      const summary = document.createElement("summary");
      const heading = document.createElement("div");
      heading.className = "workflow-phase-heading";
      const title = document.createElement("strong");
      title.textContent = phases.length
        ? `${compactText(phase.sequence ?? phaseIndex + 1, 20)}. ${compactText(phase.title || phase.phaseId || `Phase ${phaseIndex + 1}`, 400)}`
        : "Workflow steps";
      const range = isPlainObject(phase.stepRange)
        ? `${phase.stepRange.firstStep ?? "?"}–${phase.stepRange.lastStep ?? "?"}`
        : `${phaseSteps.length} step${phaseSteps.length === 1 ? "" : "s"}`;
      const meta = document.createElement("span");
      const transition = phase.entryState || phase.exitState ? ` · ${compactText(phase.entryState || "—", 100)} → ${compactText(phase.exitState || "—", 100)}` : "";
      meta.textContent = `Steps ${range}${transition}`;
      heading.append(title, meta);
      summary.appendChild(heading);
      summary.title = phasePath ? `Source: ${phasePath}` : "";
      summary.addEventListener("dblclick", event => {
        event.preventDefault();
        event.stopPropagation();
        if (phasePath) revealJsonPath(phasePath);
      });
      phaseDetails.appendChild(summary);

      const body = document.createElement("div");
      body.className = "workflow-phase-body";
      if (phase.purpose) {
        const purpose = document.createElement("p");
        purpose.className = "workflow-phase-purpose";
        purpose.textContent = compactText(phase.purpose, 1000);
        body.appendChild(purpose);
      }
      const stepList = document.createElement("div");
      stepList.className = "workflow-step-list";
      for (const step of phaseSteps) {
        const originalIndex = steps.indexOf(step);
        stepList.appendChild(buildWorkflowStep(step, model, originalIndex >= 0 ? originalIndex : 0));
      }
      body.appendChild(stepList);
      phaseDetails.appendChild(body);
      phaseList.appendChild(phaseDetails);
    };

    if (phases.length) {
      phases.forEach((phase, phaseIndex) => {
        if (!isPlainObject(phase)) return;
        const first = isPlainObject(phase.stepRange) ? Number(phase.stepRange.firstStep) : NaN;
        const last = isPlainObject(phase.stepRange) ? Number(phase.stepRange.lastStep) : NaN;
        const phaseSteps = steps.filter(step => {
          if (!isPlainObject(step)) return false;
          if (phase.phaseId && step.phaseId === phase.phaseId) return true;
          const number = Number(step.stepNumber);
          return Number.isFinite(first) && Number.isFinite(last) && number >= first && number <= last;
        });
        renderPhase(phase, phaseIndex, phaseSteps);
      });
    } else {
      renderPhase({}, 0, steps.filter(isPlainObject));
    }

    expandSteps.addEventListener("click", () => phaseList.querySelectorAll("details.workflow-step").forEach(item => item.open = true));
    collapseSteps.addEventListener("click", () => phaseList.querySelectorAll("details.workflow-step").forEach(item => item.open = false));
    expandPhases.addEventListener("click", () => phaseList.querySelectorAll("details.workflow-phase").forEach(item => item.open = true));
    collapsePhases.addEventListener("click", () => phaseList.querySelectorAll("details.workflow-phase").forEach(item => item.open = false));
    section.appendChild(phaseList);
    return section;
  }

  function appendWorkflowRecords(section, records, basePath, options = {}) {
    if (!Array.isArray(records) || !records.length) return;
    const list = document.createElement("div");
    list.className = "workflow-record-list";
    records.forEach((record, index) => {
      if (!isPlainObject(record)) return;
      const item = document.createElement("div");
      item.className = "workflow-record";
      const title = document.createElement("strong");
      const titleValue = firstObjectValue(record, options.titleKeys || ["title", "name", "decision", "question", "fileName", "instructionSetId", "factType", "reviewPurpose"]);
      title.textContent = compactText(titleValue, 500) || `Record ${index + 1}`;
      item.appendChild(title);
      const codeValue = firstObjectValue(record, options.codeKeys || ["artifactKey", "decisionId", "stateId", "stepId", "suggestedFileName", "authoritativeArtifact"]);
      if (codeValue && compactText(codeValue, 300) !== compactText(titleValue, 300)) {
        const code = document.createElement("code");
        code.textContent = compactText(codeValue, 300);
        item.appendChild(code);
      }
      const detailValue = firstObjectValue(record, options.detailKeys || ["purpose", "description", "rationale", "reasonOpen", "authorityScope", "impact", "status"]);
      if (detailValue) {
        const detail = document.createElement("span");
        detail.textContent = compactText(detailValue, 1000);
        item.appendChild(detail);
      }
      const path = `${basePath}[${index}]`;
      item.title = `Source: ${path}`;
      item.addEventListener("dblclick", () => revealJsonPath(path));
      list.appendChild(item);
    });
    if (list.children.length) section.appendChild(list);
  }

  function renderWorkflowArtifacts(model) {
    const artifactModel = isPlainObject(model.workflowArtifactModel?.value) ? model.workflowArtifactModel.value : {};
    const artifacts = Array.isArray(artifactModel.authoritativeArtifacts) ? artifactModel.authoritativeArtifacts : [];
    const authorities = Array.isArray(artifactModel.artifactAuthority) ? artifactModel.artifactAuthority : [];
    if (!artifacts.length && !authorities.length) return null;
    const section = makeWorkflowSection("Artifacts and fact authority", model.workflowArtifactModel?.path || "");
    if (artifacts.length) {
      const heading = document.createElement("p");
      heading.className = "workflow-phase-purpose";
      heading.textContent = `${artifacts.length} declared workflow artifacts`;
      section.appendChild(heading);
      appendWorkflowRecords(section, artifacts, workflowSourcePath(model, "artifactModel.authoritativeArtifacts"), {
        titleKeys: ["fileName", "artifactKey"],
        codeKeys: ["artifactKey"],
        detailKeys: ["purpose", "lifecycleStage", "artifactType"],
      });
    }
    if (authorities.length) {
      const heading = document.createElement("p");
      heading.className = "workflow-phase-purpose";
      heading.textContent = `${authorities.length} fact-authority assignments`;
      section.appendChild(heading);
      appendWorkflowRecords(section, authorities, workflowSourcePath(model, "artifactModel.artifactAuthority"), {
        titleKeys: ["factType"],
        codeKeys: ["authoritativeArtifact"],
        detailKeys: ["authorityScope", "limitations"],
      });
    }
    return section;
  }

  function renderWorkflowInstructions(model) {
    const instructions = Array.isArray(model.workflowInstructionSets?.value) ? model.workflowInstructionSets.value : [];
    if (!instructions.length) return null;
    const section = makeWorkflowSection("Instruction sets", model.workflowInstructionSets?.path || "");
    appendWorkflowRecords(section, instructions, model.workflowInstructionSets.path, {
      titleKeys: ["instructionSetId", "suggestedFileName"],
      codeKeys: ["suggestedFileName"],
      detailKeys: ["purpose", "status"],
    });
    return section;
  }

  function renderWorkflowDecisions(model) {
    const decisions = isPlainObject(model.workflowDesignDecisions?.value) ? model.workflowDesignDecisions.value : {};
    const resolved = Array.isArray(decisions.resolved) ? decisions.resolved : [];
    const open = Array.isArray(decisions.open) ? decisions.open : [];
    if (!resolved.length && !open.length) return null;
    const section = makeWorkflowSection("Design decisions", model.workflowDesignDecisions?.path || "");
    if (resolved.length) {
      const heading = document.createElement("p");
      heading.className = "workflow-phase-purpose";
      heading.textContent = `Resolved decisions: ${resolved.length}`;
      section.appendChild(heading);
      appendWorkflowRecords(section, resolved, workflowSourcePath(model, "designDecisions.resolved"), {
        titleKeys: ["decision", "title"],
        codeKeys: ["decisionId"],
        detailKeys: ["rationale", "status"],
      });
    }
    if (open.length) {
      const heading = document.createElement("p");
      heading.className = "workflow-phase-purpose";
      heading.textContent = `Open or planned decisions: ${open.length}`;
      section.appendChild(heading);
      appendWorkflowRecords(section, open, workflowSourcePath(model, "designDecisions.open"), {
        titleKeys: ["question", "title"],
        codeKeys: ["decisionId"],
        detailKeys: ["reasonOpen", "impact", "status"],
      });
    }
    return section;
  }

  function renderWorkflowValidationAndClosure(model) {
    const validation = isPlainObject(model.workflowValidationModel?.value) ? model.workflowValidationModel.value : {};
    const closure = isPlainObject(model.workflowClosureModel?.value) ? model.workflowClosureModel.value : {};
    if (!isMeaningful(validation) && !isMeaningful(closure)) return null;
    const section = makeWorkflowSection("Validation and closure", model.workflowValidationModel?.path || model.workflowClosureModel?.path || "");
    const grid = document.createElement("div");
    grid.className = "workflow-detail-grid";
    appendWorkflowTextList(grid, "Blocking conditions", validation.blockingConditions);
    appendWorkflowTextList(grid, "Non-blocking conditions", validation.nonBlockingConditions);
    appendWorkflowTextList(grid, "Completion criteria", closure.completionCriteria);
    appendWorkflowTextList(grid, "Stopping rules", closure.stoppingRules);
    appendWorkflowTextList(grid, "Recursion prevention", closure.recursionPreventionRules);
    appendWorkflowTextList(grid, "Reopen conditions", closure.reopenConditions);
    if (grid.children.length) section.appendChild(grid);
    return section;
  }

  function renderWorkflowPreviewSections(model) {
    const container = document.createElement("div");
    container.className = "preview-sections workflow-preview-sections";
    const candidates = [
      renderWorkflowOverview(model),
      makePreviewSection("Purpose", model.purpose, { maxLength: 1400 }),
      renderWorkflowStates(model),
      renderWorkflowPhasesAndSteps(model),
      renderWorkflowInstructions(model),
      renderWorkflowArtifacts(model),
      renderWorkflowDecisions(model),
      renderWorkflowValidationAndClosure(model),
      makePreviewSection("Topics", model.topics, { kind: "topics", limit: 20 }),
    ];
    for (const section of candidates) if (section) container.appendChild(section);
    return container;
  }

  function chemicalFieldValue(field, maxLength = 500) {
    return field && isMeaningful(field.value) ? compactText(field.value, maxLength) : "";
  }

  function makeChemicalSection(title, path = "") {
    const section = document.createElement("section");
    section.className = "preview-section";
    const header = document.createElement("div");
    header.className = "preview-section-header";
    const heading = document.createElement("h3");
    heading.textContent = title;
    header.appendChild(heading);
    const sourceButton = makePreviewSourceButton(path);
    if (sourceButton) header.appendChild(sourceButton);
    section.appendChild(header);
    return section;
  }

  function appendChemicalFacts(section, rows) {
    const filtered = rows.filter(([, field]) => field && isMeaningful(field.value));
    if (!filtered.length) return;
    const grid = document.createElement("div");
    grid.className = "chemical-fact-grid";
    for (const [label, field, formatter] of filtered) {
      const item = document.createElement("div");
      item.className = "chemical-fact";
      if (field.path) {
        item.title = `Source: ${field.path}`;
        item.addEventListener("dblclick", () => revealJsonPath(field.path));
      }
      const labelNode = document.createElement("span");
      labelNode.className = "chemical-fact-label";
      labelNode.textContent = label;
      const valueNode = document.createElement("span");
      valueNode.className = "chemical-fact-value";
      valueNode.textContent = formatter ? formatter(field.value) : compactText(field.value, 700);
      item.append(labelNode, valueNode);
      grid.appendChild(item);
    }
    section.appendChild(grid);
  }

  function appendChemicalSourceLink(container, label, field) {
    const url = safeDocumentUrl(field);
    if (!url) return;
    const link = document.createElement("a");
    link.className = "preview-link";
    link.href = url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.textContent = label;
    container.appendChild(link);
  }

  function sectionTitleFromKey(key) {
    const match = String(key).match(/^(\d+)_/);
    const number = match ? match[1] : "";
    return {
      number,
      title: humanizeKey(String(key).replace(/^\d+_/, ""))
    };
  }

  function renderChemicalPreview() {
    const model = state.previewModel;
    els.previewFileName.textContent = `${state.currentFile?.path || "Chemical catalog"} · entry ${(state.selectedCatalogIndex ?? 0) + 1}`;
    els.previewPanelHeading.textContent = "Chemical product preview";
    els.previewContent.innerHTML = "";

    const article = document.createElement("article");
    article.className = "preview-document";
    const hero = document.createElement("header");
    hero.className = "preview-hero";

    const eyebrow = document.createElement("p");
    eyebrow.className = "preview-eyebrow";
    eyebrow.textContent = "Verified chemical product record";
    const title = document.createElement("h2");
    title.className = "preview-title";
    title.textContent = chemicalFieldValue(model.title, 300) || "Untitled chemical product";
    if (model.title?.path) {
      title.title = `Source: ${model.title.path}`;
      title.addEventListener("dblclick", () => revealJsonPath(model.title.path));
    }
    hero.append(eyebrow, title);

    if (model.subtitle && isMeaningful(model.subtitle.value)) {
      const subtitle = document.createElement("p");
      subtitle.className = "preview-subtitle";
      subtitle.textContent = compactText(model.subtitle.value, 500);
      hero.appendChild(subtitle);
    }

    const meta = document.createElement("div");
    meta.className = "preview-meta";
    appendMetaChip(meta, "Manufacturer", model.manufacturer);
    appendMetaChip(meta, "Form", model.form);
    appendMetaChip(meta, "Status", model.status);
    appendMetaChip(meta, "Inventory ID", model.inventoryId);
    appendMetaChip(meta, "SDS ID", model.sdsId);
    appendMetaChip(meta, "SDS revision", model.sdsRevision);
    if (meta.children.length) hero.appendChild(meta);

    const actions = document.createElement("div");
    actions.className = "preview-actions";
    appendChemicalSourceLink(actions, "Open manufacturer record", model.officialProductUrl);
    appendChemicalSourceLink(actions, "Open official SDS record", model.officialSdsUrl || model.manufacturerSdsUrl);
    if (actions.children.length) hero.appendChild(actions);
    article.appendChild(hero);

    const sectionsContainer = document.createElement("div");
    sectionsContainer.className = "preview-sections";

    const productSection = makeChemicalSection("Product information", model.sourceData?.product_info ? `${model.basePath}.product_info` : "");
    appendChemicalFacts(productSection, [
      ["Inventory product ID", model.inventoryId],
      ["Inventory-listed name", model.inventoryName],
      ["Inventory-listed code", model.inventoryCode],
      ["Code status", model.inventoryCodeStatus],
      ["Container size", model.containerSize],
      ["Inventory unit", model.inventoryUnit],
      ["Department category", model.category],
      ["Carried form", model.form],
      ["Work uses", model.workUses],
      ["Work locations", model.workLocations]
    ]);
    sectionsContainer.appendChild(productSection);

    const manufacturerSection = makeChemicalSection("Manufacturer information sheet", model.sourceData?.manufacturer_info_sheet ? `${model.basePath}.manufacturer_info_sheet` : "");
    appendChemicalFacts(manufacturerSection, [
      ["Canonical product name", model.canonicalName],
      ["Manufacturer", model.manufacturer],
      ["Brand", model.brand],
      ["Product line", model.productLine],
      ["Package", model.packageDescription],
      ["Dispensing system", model.dispensingSystem],
      ["Manufacturer identifiers", model.manufacturerIdentifiers],
      ["Identity verification", model.manufacturerIdentityStatus],
      ["Safety reference type", model.safetyReferenceType],
      ["Safety reference", model.safetyReferenceLabel],
      ["Official SDS identifier", model.manufacturerSdsId],
      ["Referenced CAS numbers", model.casNumbers]
    ]);
    const manufacturerLinks = document.createElement("div");
    manufacturerLinks.className = "chemical-source-links";
    appendChemicalSourceLink(manufacturerLinks, "Manufacturer product source", model.officialProductUrl);
    appendChemicalSourceLink(manufacturerLinks, "Manufacturer SDS reference", model.manufacturerSdsUrl);
    if (manufacturerLinks.children.length) manufacturerSection.appendChild(manufacturerLinks);
    sectionsContainer.appendChild(manufacturerSection);

    const sdsSection = makeChemicalSection("SDS information sheet", model.sourceData?.sds_info_sheet ? `${model.basePath}.sds_info_sheet` : "");
    appendChemicalFacts(sdsSection, [
      ["Official SDS product name", model.sdsProductName],
      ["SDS identifier", model.sdsId],
      ["Revision date", model.sdsRevision],
      ["Version", model.sdsVersion],
      ["Formulation or dilution", model.sdsDilution],
      ["Jurisdiction", model.sdsJurisdiction],
      ["Language", model.sdsLanguage],
      ["Product match status", model.sdsMatchStatus]
    ]);

    const coverageValue = isPlainObject(model.coverage?.value) ? model.coverage.value : {};
    const required = Array.isArray(coverageValue.required_sections) ? coverageValue.required_sections.length : 0;
    const complete = Array.isArray(coverageValue.complete_sections) ? coverageValue.complete_sections.length : 0;
    const unresolved = Array.isArray(coverageValue.unresolved_sections) ? coverageValue.unresolved_sections.length : 0;
    const coverage = document.createElement("div");
    coverage.className = "chemical-coverage";
    for (const [value, label] of [[required, "Required sections"], [complete, "Complete"], [unresolved, "Unresolved"]]) {
      const item = document.createElement("div");
      item.className = "chemical-coverage-item";
      const strong = document.createElement("strong");
      strong.textContent = String(value);
      const span = document.createElement("span");
      span.textContent = label;
      item.append(strong, span);
      coverage.appendChild(item);
    }
    sdsSection.appendChild(coverage);

    const sectionValues = isPlainObject(model.sections?.value) ? model.sections.value : {};
    if (Object.keys(sectionValues).length) {
      const list = document.createElement("div");
      list.className = "chemical-section-list";
      for (const [key, value] of Object.entries(sectionValues)) {
        const row = document.createElement("div");
        row.className = "chemical-section-row";
        const identity = sectionTitleFromKey(key);
        const number = document.createElement("span");
        number.className = "chemical-section-number";
        number.textContent = identity.number || "—";
        const titleNode = document.createElement("span");
        titleNode.textContent = identity.title;
        const status = document.createElement("span");
        status.className = "chemical-section-status";
        status.textContent = isPlainObject(value) ? compactText(value.status || "unknown", 80) : "unknown";
        const path = `${model.sections.path}.${key}`;
        row.title = `Source: ${path}`;
        row.addEventListener("dblclick", () => revealJsonPath(path));
        row.append(number, titleNode, status);
        list.appendChild(row);
      }
      sdsSection.appendChild(list);
    }

    const sdsLinks = document.createElement("div");
    sdsLinks.className = "chemical-source-links";
    appendChemicalSourceLink(sdsLinks, "Official SDS source", model.officialSdsUrl);
    if (sdsLinks.children.length) sdsSection.appendChild(sdsLinks);
    sectionsContainer.appendChild(sdsSection);

    article.appendChild(sectionsContainer);

    const footer = document.createElement("footer");
    footer.className = "preview-footer";
    footer.textContent = "This preview separates workplace product context, manufacturer identity evidence, and official SDS information. The source JSON remains authoritative.";
    article.appendChild(footer);
    els.previewContent.appendChild(article);
  }

  function renderPreview() {
    const model = state.previewModel;
    if (model?.previewKind === "chemical") {
      renderChemicalPreview();
      return;
    }
    const workflowPreview = isWorkflowPreview(model);
    els.previewFileName.textContent = state.previewContext === "catalog"
      ? `${state.currentFile?.path || "Catalog"} · entry ${(state.selectedCatalogIndex ?? 0) + 1}`
      : state.currentFile?.path || "Document sidecar";
    els.previewPanelHeading.textContent = workflowPreview
      ? (state.previewContext === "catalog" ? "Catalog workflow preview" : "Workflow preview")
      : (state.previewContext === "catalog" ? "Catalog entry preview" : "Document preview");
    els.previewContent.innerHTML = "";

    if (!model) {
      els.previewContent.innerHTML = '<div class="empty"><h2>No preview available</h2><p>This selection was not recognized as a document sidecar.</p></div>';
      return;
    }

    const article = document.createElement("article");
    article.className = "preview-document";
    const hero = document.createElement("header");
    hero.className = "preview-hero";
    const eyebrow = document.createElement("p");
    eyebrow.className = "preview-eyebrow";
    eyebrow.textContent = workflowPreview
      ? (state.previewContext === "catalog" ? "Catalog workflow preview" : "Workflow specification preview")
      : (state.previewContext === "catalog" ? "Catalog entry preview" : "Document sidecar preview");
    const title = document.createElement("h2");
    title.className = "preview-title";
    title.textContent = compactText(model.title.value, 300) || "Untitled document";
    if (model.title.path) {
      title.title = `Source: ${model.title.path}`;
      title.addEventListener("dblclick", () => revealJsonPath(model.title.path));
    }
    hero.append(eyebrow, title);

    if (model.subtitle) {
      const subtitle = document.createElement("p");
      subtitle.className = "preview-subtitle";
      subtitle.textContent = compactText(model.subtitle.value, 500);
      subtitle.title = `Source: ${model.subtitle.path}`;
      subtitle.addEventListener("dblclick", () => revealJsonPath(model.subtitle.path));
      hero.appendChild(subtitle);
    }

    const meta = document.createElement("div");
    meta.className = "preview-meta";
    appendMetaChip(meta, "Type", model.documentType);
    appendMetaChip(meta, "Date", model.date);
    appendMetaChip(meta, "Project", model.project, formatEntity);
    appendMetaChip(meta, "ID", model.documentId);
    appendMetaChip(meta, "Schema", model.schemaVersion);
    if (meta.children.length) hero.appendChild(meta);

    const actions = document.createElement("div");
    actions.className = "preview-actions";
    const fullUrl = safeDocumentUrl(model.documentUrl);
    if (fullUrl) {
      const openLink = document.createElement("a");
      openLink.className = "preview-link";
      openLink.href = fullUrl;
      openLink.target = "_blank";
      openLink.rel = "noopener noreferrer";
      openLink.textContent = "Open full document";
      actions.appendChild(openLink);
      const copyUrl = document.createElement("button");
      copyUrl.type = "button";
      copyUrl.textContent = "Copy document URL";
      copyUrl.addEventListener("click", () => copyText(fullUrl, copyUrl, "Copy document URL"));
      actions.appendChild(copyUrl);
    }
    if (actions.children.length) hero.appendChild(actions);
    article.appendChild(hero);

    if (model.summary) {
      const summary = document.createElement("p");
      summary.className = "preview-summary";
      summary.textContent = compactText(model.summary.value, 1800);
      summary.title = `Source: ${model.summary.path}`;
      summary.addEventListener("dblclick", () => revealJsonPath(model.summary.path));
      article.appendChild(summary);
    }

    if (workflowPreview) {
      article.appendChild(renderWorkflowPreviewSections(model));
    } else {
      const sections = document.createElement("div");
      sections.className = "preview-sections";
      const candidates = [
        makePreviewSection("Supervisor brief", model.supervisorBrief, { className: "supervisor", maxLength: 1400 }),
        makePreviewSection("Purpose", model.purpose, { maxLength: 1200 }),
        makePreviewSection("Key outcomes", model.outcomes, { kind: "list", limit: 8 }),
        makePreviewSection("Current state", model.currentState, { maxLength: 1400 }),
        makePreviewSection("Decisions", model.decisions, { kind: "list", limit: 8 }),
        makePreviewSection("Next steps", model.nextSteps, { kind: "list", limit: 8 }),
        makePreviewSection("Document contents", model.sections, { kind: "list", limit: 12, ordered: true }),
        makePreviewSection("Topics", model.topics, { kind: "topics", limit: 16 }),
      ];
      for (const section of candidates) if (section) sections.appendChild(section);
      article.appendChild(sections);
    }

    const footer = document.createElement("footer");
    footer.className = "preview-footer";
    footer.appendChild(document.createTextNode(workflowPreview
      ? "This workflow preview is generated from the structured sidecar. The source JSON workflow specification remains authoritative."
      : "This abbreviated view is generated from structured JSON. The linked HTML document remains the complete publication."));
    const missing = [];
    if (!model.summary) missing.push("No summary field was found.");
    if (!fullUrl) missing.push("No valid HTTP(S) full-document URL was found.");
    if (!model.filePath) missing.push("No document filename or file path was found.");
    if (missing.length) {
      const notice = document.createElement("div");
      notice.className = "preview-notice";
      notice.textContent = missing.join(" ");
      footer.appendChild(notice);
    } else if (model.filePath) {
      const pathLine = document.createElement("div");
      pathLine.className = "preview-notice";
      pathLine.textContent = `Document file: ${compactText(model.filePath.value, 300)}`;
      pathLine.title = `Source: ${model.filePath.path}`;
      pathLine.addEventListener("dblclick", () => revealJsonPath(model.filePath.path));
      footer.appendChild(pathLine);
    }
    article.appendChild(footer);
    els.previewContent.appendChild(article);
  }

  function updatePreviewButton() {
    const available = Boolean(state.previewModel);
    els.previewButton.disabled = !available;
    els.previewButton.setAttribute("aria-pressed", String(available && state.previewOpen));
    els.previewButton.title = available ? "Show or hide the structured preview" : "No structured preview is available for this selection";
  }

  function setPreviewOpen(open) {
    state.previewOpen = Boolean(open && state.previewModel);
    els.app.classList.toggle("preview-open", state.previewOpen);
    els.previewPanel.setAttribute("aria-hidden", String(!state.previewOpen));
    updatePreviewButton();
    if (state.previewOpen) renderPreview();
  }

  function revealJsonPath(path) {
    if (!path || state.currentData === null) return;
    if (state.view !== "tree") {
      state.view = "tree";
      renderCurrentView();
    }
    const node = [...els.content.querySelectorAll("[data-path]")].find(candidate => candidate.dataset.path === path);
    if (!node) {
      els.status.textContent = `Source path not found in tree: ${path}`;
      return;
    }
    let parent = node.parentElement;
    while (parent) {
      if (parent.matches?.("details.tree-node")) parent.open = true;
      parent = parent.parentElement;
    }
    if (node.matches?.("details.tree-node")) node.open = true;
    els.content.querySelectorAll(".source-highlight").forEach(item => item.classList.remove("source-highlight"));
    node.classList.add("source-highlight");
    node.scrollIntoView({ block: "center", inline: "nearest", behavior: "smooth" });
    els.status.textContent = `Source: ${path}`;
    setTimeout(() => node.classList.remove("source-highlight"), 2200);
  }

  function initializePreviewResizer() {
    const savedWidth = Number(localStorage.getItem("jsonExplorerPreviewWidth"));
    if (Number.isFinite(savedWidth) && savedWidth >= 360 && savedWidth <= 820) els.app.style.setProperty("--preview-width", `${savedWidth}px`);
    els.previewResizer.addEventListener("pointerdown", event => {
      if (!state.previewOpen) return;
      event.preventDefault();
      document.body.classList.add("resizing-preview");
      const move = moveEvent => {
        const maxWidth = Math.min(820, Math.floor(window.innerWidth * .58));
        const width = Math.max(360, Math.min(maxWidth, window.innerWidth - moveEvent.clientX));
        els.app.style.setProperty("--preview-width", `${width}px`);
      };
      const stop = () => {
        document.body.classList.remove("resizing-preview");
        const width = parseInt(getComputedStyle(els.app).getPropertyValue("--preview-width"), 10);
        if (Number.isFinite(width)) localStorage.setItem("jsonExplorerPreviewWidth", String(width));
        window.removeEventListener("pointermove", move);
      };
      window.addEventListener("pointermove", move);
      window.addEventListener("pointerup", stop, { once: true });
    });
    els.previewResizer.addEventListener("dblclick", () => {
      els.app.style.setProperty("--preview-width", "470px");
      localStorage.setItem("jsonExplorerPreviewWidth", "470");
    });
    els.previewResizer.addEventListener("keydown", event => {
      if (!state.previewOpen || !["ArrowLeft", "ArrowRight"].includes(event.key)) return;
      event.preventDefault();
      const current = parseInt(getComputedStyle(els.app).getPropertyValue("--preview-width"), 10) || 470;
      const width = Math.max(360, Math.min(820, current + (event.key === "ArrowLeft" ? 24 : -24)));
      els.app.style.setProperty("--preview-width", `${width}px`);
      localStorage.setItem("jsonExplorerPreviewWidth", String(width));
    });
  }

  function showError(message) {
    els.content.innerHTML = `<div class="error">${escapeHtml(message)}</div>`;
    els.status.textContent = "Could not display this file.";
  }

  els.refreshButton.addEventListener("click", loadFileList);
  els.fileFilter.addEventListener("input", renderFileTree);
  els.sortSelect.addEventListener("change", renderFileTree);
  els.includeArchived.addEventListener("change", () => {
    state.includeArchived = els.includeArchived.checked;
    localStorage.setItem("jsonExplorerIncludeArchived", state.includeArchived ? "1" : "0");
    loadFileList();
  });
  els.treeButton.addEventListener("click", () => setView("tree"));
  els.rawButton.addEventListener("click", () => setView("raw"));
  els.catalogButton.addEventListener("click", () => setView("catalog"));
  els.previewButton.addEventListener("click", () => setPreviewOpen(!state.previewOpen));
  els.closePreviewButton.addEventListener("click", () => setPreviewOpen(false));
  els.expandButton.addEventListener("click", () => els.content.querySelectorAll("details.tree-node").forEach(node => node.open = true));
  els.collapseButton.addEventListener("click", () => els.content.querySelectorAll("details.tree-node").forEach(node => node.open = false));
  els.depthSelect.addEventListener("change", () => { if (state.view === "tree") applyDepth(Number(els.depthSelect.value)); });
  els.searchInput.addEventListener("input", applySearch);
  els.menuButton.addEventListener("click", () => els.sidebar.classList.toggle("open"));
  document.addEventListener("keydown", event => { if (event.key === "Escape" && state.previewOpen) setPreviewOpen(false); });

  state.includeArchived = localStorage.getItem("jsonExplorerIncludeArchived") === "1";
  els.includeArchived.checked = state.includeArchived;
  initializePreviewResizer();
  loadAbout();
  loadFileList();
})();
</script>
</body>
</html>
"""


def count_nodes(value: Any) -> int:
    """Count JSON container and leaf nodes."""
    if isinstance(value, dict):
        return 1 + sum(count_nodes(item) for item in value.values())
    if isinstance(value, list):
        return 1 + sum(count_nodes(item) for item in value)
    return 1


def is_archived_relative_path(relative_path: Path) -> bool:
    """Return True when a relative path passes through an archive directory."""
    return any(part.lower() in ARCHIVE_DIRECTORY_NAMES for part in relative_path.parts[:-1])


def iter_json_files(root_dir: Path, include_archived: bool = False) -> Iterable[Path]:
    """Yield JSON files recursively while pruning generated and hidden tool folders."""
    for current_root, directory_names, file_names in os.walk(root_dir):
        current_path = Path(current_root)
        relative_current = current_path.relative_to(root_dir)

        directory_names[:] = [
            name
            for name in directory_names
            if name.lower() not in EXCLUDED_DIRECTORY_NAMES
            and not name.startswith(".")
            and (include_archived or name.lower() not in ARCHIVE_DIRECTORY_NAMES)
        ]

        if not include_archived and any(part.lower() in ARCHIVE_DIRECTORY_NAMES for part in relative_current.parts):
            directory_names[:] = []
            continue

        for file_name in file_names:
            if not file_name.lower().endswith(".json"):
                continue
            path = current_path / file_name
            if path.is_file():
                yield path


def scan_json_files(root_dir: Path, include_archived: bool = False) -> list[dict[str, Any]]:
    """Return JSON file metadata using repository-relative POSIX paths."""
    files: list[dict[str, Any]] = []
    for path in iter_json_files(root_dir, include_archived=include_archived):
        relative = path.relative_to(root_dir)
        stat = path.stat()
        files.append(
            {
                "name": path.name,
                "path": relative.as_posix(),
                "folder": relative.parent.as_posix() if relative.parent != Path(".") else "",
                "size": stat.st_size,
                "modified": stat.st_mtime,
                "archived": is_archived_relative_path(relative),
            }
        )
    files.sort(key=lambda item: item["path"].lower())
    return files


class JsonExplorerHandler(BaseHTTPRequestHandler):
    """Serve the application and read-only repository APIs."""

    server_version = f"LocalJsonExplorer/{APP_VERSION}"

    @property
    def root_dir(self) -> Path:
        return self.server.root_dir  # type: ignore[attr-defined]

    def log_message(self, format: str, *args: object) -> None:
        return

    def send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def send_html(self, html: str) -> None:
        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; connect-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(body)

    def resolve_json_file(self, requested_path: str) -> Path:
        decoded = urllib.parse.unquote(requested_path).replace("\\", "/").strip()
        if not decoded:
            raise FileNotFoundError("Missing JSON file path.")

        pure_path = PurePosixPath(decoded)
        if pure_path.is_absolute() or any(part in {"", ".", ".."} for part in pure_path.parts):
            raise PermissionError("Only repository-relative JSON paths are allowed.")

        candidate = (self.root_dir.joinpath(*pure_path.parts)).resolve()
        root = self.root_dir.resolve()
        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise PermissionError("Path traversal is not allowed.") from exc

        if candidate.suffix.lower() != ".json":
            raise PermissionError("Only .json files can be opened.")
        if not candidate.is_file():
            raise FileNotFoundError(f"File not found: {decoded}")
        return candidate

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path == "/":
            self.send_html(HTML_PAGE)
            return

        if parsed.path == "/api/about":
            self.send_json(
                {
                    "app": APP_TITLE,
                    "version": APP_VERSION,
                    "buildId": BUILD_ID,
                    "scriptPath": str(Path(__file__).resolve()),
                    "folder": str(self.root_dir),
                    "processId": os.getpid(),
                    "port": self.server.server_address[1],
                }
            )
            return

        if parsed.path == "/api/files":
            query = urllib.parse.parse_qs(parsed.query)
            include_archived = query.get("includeArchived", ["0"])[0].lower() in {"1", "true", "yes"}
            try:
                files = scan_json_files(self.root_dir, include_archived=include_archived)
                self.send_json(
                    {
                        "files": files,
                        "folder": str(self.root_dir),
                        "includeArchived": include_archived,
                    }
                )
            except OSError as exc:
                self.send_json({"error": f"Could not scan repository: {exc}"}, status=500)
            return

        if parsed.path == "/api/file":
            query = urllib.parse.parse_qs(parsed.query)
            paths = query.get("path", [])
            if not paths:
                self.send_json({"error": "Missing file path."}, status=400)
                return

            raw = ""
            try:
                path = self.resolve_json_file(paths[0])
                raw = path.read_text(encoding="utf-8-sig")
                data = json.loads(raw)
                relative = path.relative_to(self.root_dir).as_posix()
                self.send_json(
                    {
                        "name": path.name,
                        "path": relative,
                        "size": path.stat().st_size,
                        "data": data,
                        "raw": json.dumps(data, ensure_ascii=False, indent=2),
                        "nodeCount": count_nodes(data),
                    }
                )
            except json.JSONDecodeError as exc:
                line_text = ""
                lines = raw.splitlines()
                if 1 <= exc.lineno <= len(lines):
                    line_text = lines[exc.lineno - 1]
                pointer = f"\n\n{line_text}\n{' ' * max(exc.colno - 1, 0)}^" if line_text else ""
                message = f"Invalid JSON in {paths[0]}\nLine {exc.lineno}, column {exc.colno}: {exc.msg}{pointer}"
                self.send_json({"error": message, "raw": raw}, status=422)
            except (OSError, PermissionError, FileNotFoundError) as exc:
                self.send_json({"error": str(exc)}, status=400)
            return

        self.send_json({"error": "Not found."}, status=404)


class JsonExplorerServer(ThreadingHTTPServer):
    """Threaded local server with a fixed, read-only repository root."""

    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address: tuple[str, int], root_dir: Path):
        super().__init__(server_address, JsonExplorerHandler)
        self.root_dir = root_dir


def default_content_root() -> Path:
    """Use the parent repository when the script lives in a directory named tools."""
    script_dir = Path(__file__).resolve().parent
    return script_dir.parent if script_dir.name.lower() == "tools" else script_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Open a read-only browser workbench for a recursive JSON repository."
    )
    parser.add_argument(
        "--folder",
        type=Path,
        default=default_content_root(),
        help="Repository root containing JSON subfolders. Defaults to the parent folder when the script is inside tools/.",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Start the server without opening the default browser.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root_dir = args.folder.expanduser().resolve()
    if not root_dir.is_dir():
        raise SystemExit(f"Repository folder does not exist: {root_dir}")

    server = JsonExplorerServer((HOST, 0), root_dir)
    port = server.server_address[1]
    url = f"http://{HOST}:{port}/"

    print(f"{APP_TITLE} v{APP_VERSION}")
    print(f"Build:      {BUILD_ID}")
    print(f"Script:     {Path(__file__).resolve()}")
    print(f"Repository: {root_dir}")
    print(f"PID:        {os.getpid()}")
    print(f"Open:       {url}")
    print("Press Ctrl+C to stop.")

    if not args.no_browser:
        threading.Timer(0.35, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever(poll_interval=0.25)
    except KeyboardInterrupt:
        print("\nStopping JSON Explorer.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
