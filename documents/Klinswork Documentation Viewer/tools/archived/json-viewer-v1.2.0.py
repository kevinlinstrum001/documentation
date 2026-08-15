#!/usr/bin/env python3
"""
Local JSON Explorer

Place this file in a folder containing JSON files and run it.
It opens a read-only browser interface for searching and exploring JSON trees.

No third-party packages are required.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import threading
import urllib.parse
import webbrowser
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

APP_TITLE = "Local JSON Explorer"
APP_VERSION = "1.2.0"
BUILD_ID = "2026-08-01-sidecar-preview"
HOST = "127.0.0.1"

HTML_PAGE = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Local JSON Explorer v1.2.0</title>
  <style>
    :root {
      color-scheme: light dark;
      --bg: #eef2f6;
      --panel: #ffffff;
      --panel-2: #f7f9fb;
      --text: #18212b;
      --muted: #637180;
      --line: #d6dde5;
      --accent: #315f8f;
      --accent-soft: #dce8f3;
      --danger: #a33a3a;
      --danger-soft: #fff0f0;
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
        --text: #eef5fb;
        --muted: #aab7c3;
        --line: #334352;
        --accent: #83b8e5;
        --accent-soft: #213c54;
        --danger: #ff9d9d;
        --danger-soft: #412427;
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

    button, input, select {
      font: inherit;
    }

    button {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      color: var(--text);
      padding: .48rem .7rem;
      cursor: pointer;
    }

    button:hover { border-color: var(--accent); }
    button:disabled {
      cursor: not-allowed;
      opacity: .5;
    }
    button[aria-pressed="true"] {
      background: var(--accent-soft);
      border-color: var(--accent);
      color: var(--accent);
    }
    button:focus-visible, input:focus-visible, select:focus-visible {
      outline: 3px solid color-mix(in srgb, var(--accent) 35%, transparent);
      outline-offset: 2px;
    }

    .app {
      --preview-width: 460px;
      display: grid;
      grid-template-columns: minmax(260px, 340px) minmax(0, 1fr) 0 0;
      width: 100vw;
      height: 100vh;
      min-width: 0;
      min-height: 0;
      overflow: hidden;
    }

    .app.preview-open {
      grid-template-columns:
        minmax(260px, 340px)
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
      padding: 1rem;
      border-bottom: 1px solid var(--line);
    }

    h1 {
      margin: 0 0 .2rem;
      font-size: 1.2rem;
      color: var(--accent);
    }

    .subtle {
      margin: 0;
      color: var(--muted);
      font-size: .84rem;
    }

    .file-controls {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: .5rem;
      margin-top: .85rem;
    }

    .file-controls input, .toolbar input, select {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel-2);
      color: var(--text);
      padding: .52rem .65rem;
    }

    .sort-row {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: .5rem;
      margin-top: .5rem;
    }

    .file-list {
      overflow: auto;
      padding: .55rem;
    }

    .file-item {
      width: 100%;
      margin: 0 0 .35rem;
      padding: .65rem .7rem;
      text-align: left;
      background: transparent;
      border: 1px solid transparent;
      border-radius: 9px;
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
      font-weight: 700;
    }

    .file-meta {
      display: block;
      margin-top: .2rem;
      color: var(--muted);
      font-size: .76rem;
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
      padding: .75rem 1rem;
      min-width: 0;
      background: var(--panel);
      border-bottom: 1px solid var(--line);
      box-shadow: var(--shadow);
      z-index: 2;
    }

    .current-file {
      display: flex;
      align-items: baseline;
      gap: .65rem;
      min-width: 0;
      margin-bottom: .65rem;
    }

    .current-file strong {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .badge {
      flex: 0 0 auto;
      padding: .16rem .5rem;
      border-radius: 999px;
      background: var(--accent-soft);
      color: var(--accent);
      font-size: .72rem;
      font-weight: 800;
    }

    .toolbar {
      display: grid;
      grid-template-columns: auto auto auto auto auto minmax(180px, 1fr) auto;
      gap: .45rem;
      align-items: center;
      max-width: 100%;
      overflow-x: auto;
      padding-bottom: .15rem;
    }

    .depth-wrap {
      display: flex;
      align-items: center;
      gap: .35rem;
    }

    .depth-wrap select { width: auto; }

    .content {
      min-width: 0;
      min-height: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      overscroll-behavior: contain;
      padding: 1rem;
      scrollbar-gutter: stable both-edges;
      -webkit-overflow-scrolling: touch;
    }

    .empty {
      max-width: 760px;
      margin: 8vh auto 0;
      padding: 2rem;
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
      padding: .75rem .9rem 2rem;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }

    .tree-node {
      margin-left: 1.15rem;
      border-left: 1px dotted var(--line);
      padding-left: .55rem;
    }

    .tree-node.root {
      margin-left: 0;
      border-left: 0;
      padding-left: 0;
    }

    details > summary {
      list-style: none;
      cursor: pointer;
      padding: .18rem .3rem;
      border-radius: 5px;
      font-family: var(--mono);
      white-space: normal;
    }

    details > summary::-webkit-details-marker { display: none; }

    details > summary::before {
      content: "▸";
      display: inline-block;
      width: 1rem;
      color: var(--accent);
      transition: transform .1s ease;
    }

    details[open] > summary::before {
      transform: rotate(90deg);
    }

    .key { color: var(--accent); font-weight: 700; }
    .type-note { color: var(--muted); font-size: .8em; }

    .leaf {
      display: grid;
      grid-template-columns: minmax(120px, auto) 1fr auto;
      gap: .55rem;
      align-items: start;
      padding: .18rem .3rem .18rem 1.15rem;
      border-radius: 5px;
      font-family: var(--mono);
      white-space: normal;
    }

    .leaf:hover, details > summary:hover {
      background: var(--panel-2);
    }

    .value {
      max-width: 78ch;
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
      padding: .13rem .35rem;
      font-size: .72rem;
    }

    .leaf:hover .copy-button, summary:hover .copy-button {
      opacity: 1;
    }

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

    .raw {
      margin: 0;
      min-height: 100%;
      padding: 1rem;
      overflow: auto;
      color: var(--text);
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      font: .9rem/1.55 var(--mono);
      white-space: pre;
      tab-size: 2;
    }


    .preview-resizer {
      display: none;
      width: 6px;
      min-width: 6px;
      height: 100vh;
      cursor: col-resize;
      background:
        linear-gradient(
          to right,
          transparent 0,
          transparent 2px,
          var(--line) 2px,
          var(--line) 4px,
          transparent 4px
        );
      touch-action: none;
    }

    .app.preview-open .preview-resizer {
      display: block;
    }

    body.resizing-preview,
    body.resizing-preview * {
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
      padding: .8rem .9rem;
      background: var(--panel);
      border-bottom: 1px solid var(--line);
    }

    .preview-panel-title {
      min-width: 0;
    }

    .preview-panel-title strong {
      display: block;
      color: var(--accent);
      font-size: .94rem;
    }

    .preview-panel-title span {
      display: block;
      margin-top: .12rem;
      overflow: hidden;
      color: var(--muted);
      font-size: .76rem;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .preview-scroll {
      min-width: 0;
      min-height: 0;
      overflow: auto;
      padding: 1rem;
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
      padding: 1.2rem 1.25rem 1.1rem;
      background:
        linear-gradient(
          145deg,
          color-mix(in srgb, var(--accent-soft) 68%, var(--panel)),
          var(--panel) 72%
        );
      border-bottom: 1px solid var(--line);
    }

    .preview-eyebrow {
      margin: 0 0 .42rem;
      color: var(--accent);
      font-size: .7rem;
      font-weight: 850;
      letter-spacing: .11em;
      text-transform: uppercase;
    }

    .preview-title {
      margin: 0;
      color: var(--text);
      font-size: clamp(1.35rem, 2vw, 2rem);
      line-height: 1.12;
      text-wrap: balance;
    }

    .preview-subtitle {
      margin: .55rem 0 0;
      color: var(--muted);
      font-size: .98rem;
      line-height: 1.45;
    }

    .preview-meta {
      display: flex;
      flex-wrap: wrap;
      gap: .35rem;
      margin-top: .85rem;
    }

    .preview-chip {
      display: inline-flex;
      align-items: center;
      max-width: 100%;
      padding: .22rem .5rem;
      overflow: hidden;
      color: var(--muted);
      background: color-mix(in srgb, var(--panel) 82%, var(--accent-soft));
      border: 1px solid var(--line);
      border-radius: 999px;
      font-size: .72rem;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .preview-actions {
      display: flex;
      flex-wrap: wrap;
      gap: .45rem;
      margin-top: .85rem;
    }

    .preview-link {
      display: inline-flex;
      align-items: center;
      border: 1px solid var(--accent);
      border-radius: 8px;
      background: var(--accent);
      color: var(--panel);
      padding: .48rem .72rem;
      font-size: .83rem;
      font-weight: 750;
      text-decoration: none;
    }

    .preview-link:hover {
      filter: brightness(1.06);
    }

    .preview-summary {
      margin: 0;
      padding: 1.1rem 1.25rem;
      color: var(--text);
      border-bottom: 1px solid var(--line);
      font-size: 1rem;
      line-height: 1.62;
    }

    .preview-sections {
      padding: .35rem 1.25rem 1.15rem;
    }

    .preview-section {
      padding: 1rem 0;
      border-bottom: 1px solid var(--line);
    }

    .preview-section:last-child {
      border-bottom: 0;
    }

    .preview-section.supervisor {
      margin: .75rem -.35rem .1rem;
      padding: .9rem .85rem;
      background: color-mix(in srgb, #d8bd67 18%, var(--panel));
      border: 1px solid color-mix(in srgb, #9a7a22 35%, var(--line));
      border-radius: 10px;
    }

    .preview-section-header {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: .6rem;
      margin-bottom: .45rem;
    }

    .preview-section h3 {
      margin: 0;
      color: var(--accent);
      font-size: .85rem;
      letter-spacing: .045em;
      text-transform: uppercase;
    }

    .preview-section p {
      margin: 0;
      color: var(--text);
      font-size: .91rem;
      line-height: 1.58;
      white-space: pre-wrap;
    }

    .preview-section ul,
    .preview-section ol {
      margin: .15rem 0 0;
      padding-left: 1.2rem;
    }

    .preview-section li {
      margin: .38rem 0;
      color: var(--text);
      font-size: .88rem;
      line-height: 1.48;
    }

    .preview-item-detail {
      display: block;
      margin-top: .12rem;
      color: var(--muted);
      font-size: .82rem;
    }

    .preview-source {
      flex: 0 0 auto;
      padding: .16rem .4rem;
      color: var(--muted);
      background: transparent;
      border-color: transparent;
      font-family: var(--mono);
      font-size: .67rem;
    }

    .preview-source:hover {
      color: var(--accent);
      background: var(--accent-soft);
      border-color: var(--accent);
    }

    .preview-topic-list {
      display: flex;
      flex-wrap: wrap;
      gap: .35rem;
      margin-top: .25rem;
    }

    .preview-topic {
      padding: .24rem .5rem;
      color: var(--accent);
      background: var(--accent-soft);
      border-radius: 999px;
      font-size: .75rem;
    }

    .preview-footer {
      padding: .85rem 1.25rem 1rem;
      color: var(--muted);
      background: var(--panel-2);
      border-top: 1px solid var(--line);
      font-size: .76rem;
      line-height: 1.45;
    }

    .preview-notice {
      margin-top: .55rem;
      padding: .55rem .65rem;
      background: var(--panel);
      border: 1px dashed var(--line);
      border-radius: 8px;
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

    .status {
      margin-top: .5rem;
      color: var(--muted);
      font-size: .78rem;
    }

    .hidden { display: none !important; }

    @media (max-width: 800px) {
      .app,
      .app.preview-open {
        grid-template-columns: 1fr;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
      }

      .preview-resizer {
        display: none !important;
      }

      .preview-panel,
      .app.preview-open .preview-panel {
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
        width: min(86vw, 340px);
        height: 100vh;
        min-height: 0;
        z-index: 5;
        transform: translateX(-100%);
        transition: transform .18s ease;
      }
      .sidebar.open { transform: translateX(0); }
      .toolbar {
        grid-template-columns: repeat(5, auto);
      }
      .toolbar input {
        grid-column: 1 / -1;
      }
      #menuButton { display: inline-block !important; }
    }
  </style>
</head>
<body>
<div class="app" id="app">
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <h1>Local JSON Explorer</h1>
      <p class="subtle">Read-only files from this folder</p>
      <p class="subtle" id="runtimeInfo">Version 1.2.0 · loading runtime identity…</p>
      <div class="file-controls">
        <input id="fileFilter" type="search" placeholder="Filter filenames">
        <button id="refreshButton" title="Refresh file list">Refresh</button>
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
    </div>
    <div class="file-list" id="fileList"></div>
  </aside>

  <main class="main">
    <div class="topbar">
      <div class="current-file">
        <button id="menuButton" class="hidden" aria-label="Open file list">Files</button>
        <strong id="currentFileName">Choose a JSON file</strong>
        <span class="badge" id="modeBadge">TREE</span>
      </div>
      <div class="toolbar">
        <button id="treeButton">Tree</button>
        <button id="rawButton">Raw</button>
        <button id="previewButton" aria-pressed="false" disabled title="Select a document sidecar">Preview</button>
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
        <p>Select a file from the left panel to inspect its hierarchy, search its contents, copy paths, or view the raw JSON.</p>
      </div>
    </section>
  </main>

  <div class="preview-resizer" id="previewResizer" role="separator" aria-label="Resize document preview" aria-orientation="vertical" tabindex="0"></div>

  <aside class="preview-panel" id="previewPanel" aria-label="Document preview" aria-hidden="true">
    <header class="preview-panel-header">
      <div class="preview-panel-title">
        <strong>Document preview</strong>
        <span id="previewFileName">No sidecar selected</span>
      </div>
      <button id="closePreviewButton" title="Close preview">Close</button>
    </header>
    <div class="preview-scroll" id="previewContent">
      <div class="empty">
        <h2>No preview available</h2>
        <p>Select a document sidecar to generate an abbreviated reading view.</p>
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
    previewModel: null,
    previewOpen: false,
  };

  const els = {
    app: document.getElementById("app"),
    sidebar: document.getElementById("sidebar"),
    fileList: document.getElementById("fileList"),
    fileFilter: document.getElementById("fileFilter"),
    refreshButton: document.getElementById("refreshButton"),
    sortSelect: document.getElementById("sortSelect"),
    fileCount: document.getElementById("fileCount"),
    currentFileName: document.getElementById("currentFileName"),
    modeBadge: document.getElementById("modeBadge"),
    treeButton: document.getElementById("treeButton"),
    rawButton: document.getElementById("rawButton"),
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
    previewFileName: document.getElementById("previewFileName"),
    previewContent: document.getElementById("previewContent"),
    closePreviewButton: document.getElementById("closePreviewButton"),
  };

  const escapeHtml = (value) => String(value)
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
      els.runtimeInfo.textContent =
        `v${about.version} · build ${about.buildId} · PID ${about.processId} · port ${about.port}`;
      els.runtimeInfo.title = `Script: ${about.scriptPath}\nFolder: ${about.folder}`;
    } catch {
      els.runtimeInfo.textContent = "Version 1.2.0 · runtime identity unavailable";
    }
  }

  async function loadFileList() {
    els.status.textContent = "Refreshing file list…";
    try {
      const response = await fetch("/api/files", { cache: "no-store" });
      const payload = await response.json();
      if (!response.ok) throw new Error(payload.error || "Could not load files.");
      state.files = payload.files;
      renderFileList();
      els.status.textContent = state.currentFile ? `Loaded ${state.currentFile.name}` : "Choose a JSON file.";
    } catch (error) {
      showError(error.message);
    }
  }

  function renderFileList() {
    const filter = els.fileFilter.value.trim().toLowerCase();
    const files = sortFiles(state.files).filter(file => file.name.toLowerCase().includes(filter));
    els.fileCount.textContent = `${files.length} file${files.length === 1 ? "" : "s"}`;

    if (!files.length) {
      els.fileList.innerHTML = '<p class="subtle" style="padding:.7rem">No matching JSON files.</p>';
      return;
    }

    els.fileList.innerHTML = "";
    for (const file of files) {
      const button = document.createElement("button");
      button.className = "file-item" + (state.currentFile?.name === file.name ? " active" : "");
      button.innerHTML = `
        <span class="file-name">${escapeHtml(file.name)}</span>
        <span class="file-meta">${formatBytes(file.size)} · ${escapeHtml(formatDate(file.modified))}</span>
      `;
      button.addEventListener("click", () => loadFile(file.name));
      els.fileList.appendChild(button);
    }
  }

  async function loadFile(name) {
    els.status.textContent = `Loading ${name}…`;
    try {
      const response = await fetch(`/api/file?name=${encodeURIComponent(name)}`, { cache: "no-store" });
      const payload = await response.json();
      if (!response.ok) {
        state.currentFile = state.files.find(f => f.name === name) || { name };
        state.currentData = null;
        state.currentRaw = payload.raw || "";
        state.previewModel = null;
        els.currentFileName.textContent = name;
        renderFileList();
        setPreviewOpen(false);
        updatePreviewButton();
        showError(payload.error || "Invalid JSON.");
        return;
      }

      state.currentFile = state.files.find(f => f.name === name) || { name };
      state.currentData = payload.data;
      state.currentRaw = payload.raw;
      state.query = "";
      els.searchInput.value = "";
      els.currentFileName.textContent = name;
      els.status.textContent = `${payload.nodeCount.toLocaleString()} nodes · ${formatBytes(payload.size)}`;
      renderFileList();
      renderCurrentView();
      updateSidecarPreview();
      if (window.innerWidth <= 800) els.sidebar.classList.remove("open");
    } catch (error) {
      state.previewModel = null;
      setPreviewOpen(false);
      updatePreviewButton();
      showError(error.message);
    }
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

  function childPath(parentPath, key, isArray) {
    if (isArray) return `${parentPath}[${key}]`;
    const safeIdentifier = /^[A-Za-z_$][A-Za-z0-9_$]*$/.test(key);
    if (!parentPath) return safeIdentifier ? key : `[${JSON.stringify(key)}]`;
    return safeIdentifier ? `${parentPath}.${key}` : `${parentPath}[${JSON.stringify(key)}]`;
  }

  function makeCopyButton(text, label) {
    const button = document.createElement("button");
    button.className = "copy-button";
    button.textContent = label;
    button.title = `Copy ${label.toLowerCase()}`;
    button.addEventListener("click", async (event) => {
      event.preventDefault();
      event.stopPropagation();
      try {
        await navigator.clipboard.writeText(text);
        button.textContent = "Copied";
        setTimeout(() => button.textContent = label, 900);
      } catch {
        prompt("Copy:", text);
      }
    });
    return button;
  }

  function createNode(key, value, path, depth = 0, isRoot = false) {
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

      const entries = isArray ? value.map((v, i) => [String(i), v]) : Object.entries(value);
      for (const [childKey, childValue] of entries) {
        const nextPath = childPath(path, childKey, isArray);
        details.appendChild(createNode(childKey, childValue, nextPath, depth + 1, false));
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
    controls.appendChild(makeCopyButton(path, "Path"));
    controls.appendChild(makeCopyButton(valueText(value), "Value"));

    row.append(keySpan, valueSpan, controls);
    return row;
  }

  function renderTree() {
    els.content.innerHTML = "";
    const shell = document.createElement("div");
    shell.className = "tree-shell";
    const rootLabel = Array.isArray(state.currentData) ? "root" : "root";
    shell.appendChild(createNode(rootLabel, state.currentData, "", 0, true));
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
    if (state.view === "raw") renderRaw();
    else renderTree();
  }

  function setView(view) {
    state.view = view;
    renderCurrentView();
  }

  function applyDepth(maxDepth) {
    const details = [...els.content.querySelectorAll("details")];
    for (const node of details) {
      let depth = 0;
      let parent = node.parentElement;
      while (parent && parent !== els.content) {
        if (parent.tagName === "DETAILS") depth += 1;
        parent = parent.parentElement;
      }
      node.open = depth < maxDepth;
    }
  }

  function clearMarks(root) {
    root.querySelectorAll("mark").forEach(mark => {
      mark.replaceWith(document.createTextNode(mark.textContent || ""));
    });
    root.querySelectorAll(".search-match").forEach(el => el.classList.remove("search-match"));
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
        if (parent.tagName === "DETAILS") parent.open = true;
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

  function pickPreviewField(paths, validator = isMeaningful) {
    for (const path of paths) {
      const value = readDataPath(state.currentData, path);
      if (validator(value)) return { value, path };
    }
    return null;
  }

  function firstObjectValue(object, keys) {
    if (!isPlainObject(object)) return undefined;
    for (const key of keys) {
      if (Object.prototype.hasOwnProperty.call(object, key) && isMeaningful(object[key])) {
        return object[key];
      }
    }
    return undefined;
  }

  function compactText(value, maxLength = 900) {
    let text = "";

    if (value === null || value === undefined) return "";
    if (typeof value === "string") {
      text = value.trim();
    } else if (typeof value === "number" || typeof value === "boolean") {
      text = String(value);
    } else if (Array.isArray(value)) {
      text = value.map(item => compactText(item, 220)).filter(Boolean).join("; ");
    } else if (isPlainObject(value)) {
      const preferred = firstObjectValue(value, [
        "summary", "description", "text", "value", "title", "name",
        "purpose", "status", "outcome", "result", "currentState"
      ]);

      if (preferred !== undefined) {
        text = compactText(preferred, maxLength);
      } else {
        text = Object.entries(value)
          .filter(([, item]) => ["string", "number", "boolean"].includes(typeof item))
          .slice(0, 5)
          .map(([key, item]) => `${humanizeKey(key)}: ${String(item)}`)
          .join(" · ");
      }
    }

    if (text.length > maxLength) return `${text.slice(0, maxLength - 1).trim()}…`;
    return text;
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

    if (Array.isArray(value)) {
      return value.map(formatEntity).filter(Boolean).slice(0, 4).join(", ");
    }

    if (isPlainObject(value)) {
      const name = compactText(firstObjectValue(value, [
        "name", "title", "projectName", "productName", "label"
      ]), 180);
      const id = compactText(firstObjectValue(value, [
        "projectId", "productId", "documentId", "id"
      ]), 120);

      if (name && id && name !== id) return `${name} (${id})`;
      if (name || id) return name || id;
    }

    return compactText(value, 220);
  }

  function looksLikeDocumentSidecar(data) {
    if (!isPlainObject(data)) return false;

    const documentRecord = isPlainObject(data.document) ? data.document : null;
    const documentKeys = documentRecord
      ? ["documentId", "documentUrl", "documentTitle", "title", "filePath", "fileName"]
          .filter(key => Object.prototype.hasOwnProperty.call(documentRecord, key)).length
      : 0;

    const topIdentityKeys = ["documentId", "documentUrl", "documentTitle"]
      .filter(key => Object.prototype.hasOwnProperty.call(data, key)).length;

    const structuralKeys = [
      "sections", "publication", "projectContext", "narrative", "supervisorView",
      "workCoverage", "projectContribution", "technicalContent", "provenance"
    ].filter(key => Object.prototype.hasOwnProperty.call(data, key)).length;

    const schemaText = String(data.schemaVersion || data.schema || "").toLowerCase();
    const explicitType = String(
      data.recordType ||
      data.metadataType ||
      documentRecord?.recordType ||
      documentRecord?.documentType ||
      ""
    ).toLowerCase();

    return (
      documentKeys >= 2 ||
      (documentKeys >= 1 && structuralKeys >= 1) ||
      (topIdentityKeys >= 1 && structuralKeys >= 2) ||
      schemaText.includes("sidecar") ||
      explicitType.includes("sidecar")
    );
  }

  function buildSidecarPreview() {
    if (!looksLikeDocumentSidecar(state.currentData)) return null;

    const stringField = paths => pickPreviewField(
      paths,
      value => typeof value === "string" && value.trim().length > 0
    );

    const title = stringField([
      "preview.title",
      "document.title",
      "document.documentTitle",
      "documentTitle",
      "title",
      "publication.listingTitle",
      "listing.title",
      "googleSites.title",
      "metadata.title"
    ]);

    const subtitle = stringField([
      "preview.subtitle",
      "document.subtitle",
      "document.headline",
      "headline",
      "publication.subtitle",
      "listing.subtitle"
    ]);

    const summary = pickPreviewField([
      "preview.summary",
      "document.executiveSummary",
      "executiveSummary",
      "document.summary",
      "summary",
      "abstract",
      "document.description",
      "description",
      "publication.listingDescription",
      "listing.description",
      "googleSites.listingDescription"
    ]);

    const documentType = pickPreviewField([
      "document.documentType",
      "document.type",
      "documentType",
      "recordType",
      "type"
    ]);

    const date = pickPreviewField([
      "document.publicationDate",
      "document.publishedDate",
      "document.date",
      "publication.publishedAt",
      "publication.publicationDate",
      "publication.date",
      "publishedDate",
      "date"
    ]);

    const documentId = pickPreviewField([
      "document.documentId",
      "documentId",
      "id"
    ]);

    const documentUrl = stringField([
      "document.documentUrl",
      "document.url",
      "publication.canonicalUrl",
      "publication.documentUrl",
      "canonicalUrl",
      "links.fullDocument",
      "links.document",
      "url"
    ]);

    const filePath = stringField([
      "document.filePath",
      "document.fileName",
      "filePath",
      "fileName"
    ]);

    const project = pickPreviewField([
      "projectContext.primaryProject",
      "primaryProject",
      "project",
      "document.project",
      "subject.primaryProject"
    ]);

    const purpose = pickPreviewField([
      "preview.purpose",
      "workCoverage.purpose",
      "document.purpose",
      "purpose",
      "projectContribution.purpose"
    ]);

    const supervisorBrief = pickPreviewField([
      "supervisorView.brief",
      "supervisorView.summary",
      "supervisorBrief",
      "audienceViews.supervisor.brief",
      "audiences.supervisor.brief",
      "publication.supervisorBrief"
    ]);

    const outcomes = pickPreviewField([
      "preview.outcomes",
      "keyOutcomes",
      "outcomes",
      "projectContribution.outcomes",
      "projectContribution.result",
      "resultingCapabilities",
      "currentState.capabilities",
      "workPerformed.outcomes",
      "workCoverage.completed"
    ]);

    const currentState = pickPreviewField([
      "preview.currentState",
      "currentState.summary",
      "currentState",
      "resultingState",
      "projectContribution.currentState",
      "status"
    ]);

    const decisions = pickPreviewField([
      "preview.decisions",
      "keyDecisions",
      "decisions",
      "narrative.decisions",
      "designDecisions"
    ]);

    const nextSteps = pickPreviewField([
      "preview.nextSteps",
      "nextSteps",
      "roadmap.nextSteps",
      "projectContribution.nextSteps",
      "bootstrapNextSteps",
      "currentState.nextSteps"
    ]);

    const topics = pickPreviewField([
      "preview.topics",
      "topics",
      "tags",
      "subjectClassification.topics",
      "classification.topics",
      "document.topics",
      "publication.keywords",
      "subjects"
    ]);

    const sections = pickPreviewField([
      "document.sections",
      "sections",
      "content.sections",
      "narrative.sections"
    ]);

    const schemaVersion = pickPreviewField([
      "schemaVersion",
      "metadata.schemaVersion",
      "document.schemaVersion"
    ]);

    return {
      title: title || {
        value: state.currentFile?.name?.replace(/\.json$/i, "") || "Untitled document",
        path: ""
      },
      subtitle,
      summary,
      documentType,
      date,
      documentId,
      documentUrl,
      filePath,
      project,
      purpose,
      supervisorBrief,
      outcomes,
      currentState,
      decisions,
      nextSteps,
      topics,
      sections,
      schemaVersion
    };
  }

  function safeDocumentUrl(field) {
    if (!field || typeof field.value !== "string") return "";
    try {
      const url = new URL(field.value);
      if (url.protocol === "http:" || url.protocol === "https:") return url.href;
    } catch {
      return "";
    }
    return "";
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
      const topics = previewListItems(field.value, field.path, 16);
      const list = document.createElement("div");
      list.className = "preview-topic-list";
      for (const item of topics) {
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
      if (!items.length) {
        const paragraph = document.createElement("p");
        paragraph.textContent = compactText(field.value);
        section.appendChild(paragraph);
        return section;
      }

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

  function previewListItems(value, basePath = "", limit = 8) {
    const source = Array.isArray(value)
      ? value.map((item, index) => ({ key: String(index), item, path: `${basePath}[${index}]` }))
      : isPlainObject(value)
        ? Object.entries(value).map(([key, item]) => ({
            key,
            item,
            path: basePath ? `${basePath}.${key}` : key
          }))
        : [{ key: "", item: value, path: basePath }];

    const items = [];
    for (const entry of source) {
      if (!isMeaningful(entry.item)) continue;

      if (typeof entry.item === "string" ||
          typeof entry.item === "number" ||
          typeof entry.item === "boolean") {
        items.push({
          title: compactText(entry.item, 280),
          detail: "",
          path: entry.path
        });
      } else if (isPlainObject(entry.item)) {
        const titleValue = firstObjectValue(entry.item, [
          "title", "name", "label", "heading", "sectionTitle", "decision",
          "outcome", "capability", "step", "status", "change", "topic"
        ]);
        const detailValue = firstObjectValue(entry.item, [
          "summary", "description", "text", "rationale", "reason", "result",
          "impact", "currentState", "details"
        ]);

        const title = compactText(titleValue, 280) || humanizeKey(entry.key);
        const detail = compactText(detailValue, 480);

        items.push({ title, detail, path: entry.path });
      } else if (Array.isArray(entry.item)) {
        items.push({
          title: humanizeKey(entry.key),
          detail: compactText(entry.item, 420),
          path: entry.path
        });
      }

      if (items.length >= limit) break;
    }

    return items;
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

  function renderPreview() {
    const model = state.previewModel;
    els.previewFileName.textContent = state.currentFile?.name || "Document sidecar";
    els.previewContent.innerHTML = "";

    if (!model) {
      els.previewContent.innerHTML = `
        <div class="empty">
          <h2>No preview available</h2>
          <p>This JSON file was not recognized as an individual HTML-document sidecar.</p>
        </div>
      `;
      return;
    }

    const article = document.createElement("article");
    article.className = "preview-document";

    const hero = document.createElement("header");
    hero.className = "preview-hero";

    const eyebrow = document.createElement("p");
    eyebrow.className = "preview-eyebrow";
    eyebrow.textContent = "Document sidecar preview";

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
      copyUrl.addEventListener("click", async () => {
        try {
          await navigator.clipboard.writeText(fullUrl);
          copyUrl.textContent = "Copied";
          setTimeout(() => copyUrl.textContent = "Copy document URL", 900);
        } catch {
          prompt("Copy document URL:", fullUrl);
        }
      });
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

    const sections = document.createElement("div");
    sections.className = "preview-sections";

    const candidates = [
      makePreviewSection("Supervisor brief", model.supervisorBrief, {
        className: "supervisor",
        maxLength: 1400
      }),
      makePreviewSection("Purpose", model.purpose, { maxLength: 1200 }),
      makePreviewSection("Key outcomes", model.outcomes, { kind: "list", limit: 8 }),
      makePreviewSection("Current state", model.currentState, { maxLength: 1400 }),
      makePreviewSection("Decisions", model.decisions, { kind: "list", limit: 8 }),
      makePreviewSection("Next steps", model.nextSteps, { kind: "list", limit: 8 }),
      makePreviewSection("Document contents", model.sections, {
        kind: "list",
        limit: 10,
        ordered: true
      }),
      makePreviewSection("Topics", model.topics, { kind: "topics", limit: 16 })
    ];

    for (const section of candidates) {
      if (section) sections.appendChild(section);
    }

    if (!sections.children.length && !model.summary) {
      const sparse = document.createElement("section");
      sparse.className = "preview-section";
      sparse.innerHTML = `
        <div class="preview-section-header"><h3>Preview incomplete</h3></div>
        <p>The file has document identity fields, but no recognized summary, purpose, outcomes, state, decisions, next steps, topics, or section descriptions.</p>
      `;
      sections.appendChild(sparse);
    }

    article.appendChild(sections);

    const footer = document.createElement("footer");
    footer.className = "preview-footer";
    footer.appendChild(document.createTextNode(
      "This abbreviated view is generated from the sidecar. The linked HTML document remains the complete publication."
    ));

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
    els.previewButton.title = available
      ? "Show or hide the abbreviated document preview"
      : "This JSON file is not recognized as an individual document sidecar";
  }

  function setPreviewOpen(open) {
    state.previewOpen = Boolean(open && state.previewModel);
    els.app.classList.toggle("preview-open", state.previewOpen);
    els.previewPanel.setAttribute("aria-hidden", String(!state.previewOpen));
    updatePreviewButton();
    if (state.previewOpen) renderPreview();
  }

  function updateSidecarPreview() {
    state.previewModel = buildSidecarPreview();
    updatePreviewButton();
    setPreviewOpen(Boolean(state.previewModel));
  }

  function revealJsonPath(path) {
    if (!path || state.currentData === null) return;

    if (state.view !== "tree") {
      state.view = "tree";
      renderCurrentView();
    }

    const candidates = [...els.content.querySelectorAll("[data-path]")];
    const node = candidates.find(candidate => candidate.dataset.path === path);

    if (!node) {
      els.status.textContent = `Preview source path not found in tree: ${path}`;
      return;
    }

    let parent = node.parentElement;
    while (parent) {
      if (parent.tagName === "DETAILS") parent.open = true;
      parent = parent.parentElement;
    }

    if (node.tagName === "DETAILS") node.open = true;
    els.content.querySelectorAll(".source-highlight").forEach(item => item.classList.remove("source-highlight"));
    node.classList.add("source-highlight");
    node.scrollIntoView({ block: "center", inline: "nearest", behavior: "smooth" });
    els.status.textContent = `Preview source: ${path}`;
    setTimeout(() => node.classList.remove("source-highlight"), 2200);
  }

  function initializePreviewResizer() {
    const savedWidth = Number(localStorage.getItem("jsonExplorerPreviewWidth"));
    if (Number.isFinite(savedWidth) && savedWidth >= 360 && savedWidth <= 760) {
      els.app.style.setProperty("--preview-width", `${savedWidth}px`);
    }

    els.previewResizer.addEventListener("pointerdown", event => {
      if (!state.previewOpen) return;
      event.preventDefault();
      document.body.classList.add("resizing-preview");

      const move = moveEvent => {
        const maxWidth = Math.min(760, Math.floor(window.innerWidth * .55));
        const width = Math.max(360, Math.min(maxWidth, window.innerWidth - moveEvent.clientX));
        els.app.style.setProperty("--preview-width", `${width}px`);
      };

      const stop = () => {
        document.body.classList.remove("resizing-preview");
        const width = parseInt(getComputedStyle(els.app).getPropertyValue("--preview-width"), 10);
        if (Number.isFinite(width)) localStorage.setItem("jsonExplorerPreviewWidth", String(width));
        window.removeEventListener("pointermove", move);
        window.removeEventListener("pointerup", stop);
      };

      window.addEventListener("pointermove", move);
      window.addEventListener("pointerup", stop, { once: true });
    });

    els.previewResizer.addEventListener("dblclick", () => {
      els.app.style.setProperty("--preview-width", "460px");
      localStorage.setItem("jsonExplorerPreviewWidth", "460");
    });

    els.previewResizer.addEventListener("keydown", event => {
      if (!state.previewOpen || !["ArrowLeft", "ArrowRight"].includes(event.key)) return;
      event.preventDefault();
      const current = parseInt(getComputedStyle(els.app).getPropertyValue("--preview-width"), 10) || 460;
      const change = event.key === "ArrowLeft" ? 24 : -24;
      const width = Math.max(360, Math.min(760, current + change));
      els.app.style.setProperty("--preview-width", `${width}px`);
      localStorage.setItem("jsonExplorerPreviewWidth", String(width));
    });
  }


  function showError(message) {
    els.content.innerHTML = `<div class="error">${escapeHtml(message)}</div>`;
    els.status.textContent = "Could not display this file.";
  }

  els.refreshButton.addEventListener("click", loadFileList);
  els.fileFilter.addEventListener("input", renderFileList);
  els.sortSelect.addEventListener("change", renderFileList);
  els.treeButton.addEventListener("click", () => setView("tree"));
  els.rawButton.addEventListener("click", () => setView("raw"));
  els.previewButton.addEventListener("click", () => setPreviewOpen(!state.previewOpen));
  els.closePreviewButton.addEventListener("click", () => setPreviewOpen(false));
  els.expandButton.addEventListener("click", () => {
    els.content.querySelectorAll("details").forEach(node => node.open = true);
  });
  els.collapseButton.addEventListener("click", () => {
    els.content.querySelectorAll("details").forEach(node => node.open = false);
  });
  els.depthSelect.addEventListener("change", () => {
    if (state.view === "tree") applyDepth(Number(els.depthSelect.value));
  });
  els.searchInput.addEventListener("input", applySearch);
  els.menuButton.addEventListener("click", () => els.sidebar.classList.toggle("open"));
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && state.previewOpen) setPreviewOpen(false);
  });

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


class JsonExplorerHandler(BaseHTTPRequestHandler):
    """Serve the application and read-only JSON APIs."""

    server_version = f"LocalJsonExplorer/{APP_VERSION}"

    @property
    def root_dir(self) -> Path:
        return self.server.root_dir  # type: ignore[attr-defined]

    def log_message(self, format: str, *args: object) -> None:
        # Keep the console quiet except for startup and real errors.
        return

    def send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def send_html(self, html: str) -> None:
        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def resolve_json_file(self, requested_name: str) -> Path:
        decoded_name = urllib.parse.unquote(requested_name)
        candidate = (self.root_dir / decoded_name).resolve()
        root = self.root_dir.resolve()

        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise PermissionError("Path traversal is not allowed.") from exc

        if candidate.parent != root:
            raise PermissionError("Only JSON files in this folder can be opened.")
        if candidate.suffix.lower() != ".json":
            raise PermissionError("Only .json files can be opened.")
        if not candidate.is_file():
            raise FileNotFoundError(f"File not found: {decoded_name}")
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
            files = []
            try:
                for path in self.root_dir.iterdir():
                    if not path.is_file() or path.suffix.lower() != ".json":
                        continue
                    stat = path.stat()
                    files.append(
                        {
                            "name": path.name,
                            "size": stat.st_size,
                            "modified": stat.st_mtime,
                        }
                    )
                self.send_json({"files": files, "folder": str(self.root_dir)})
            except OSError as exc:
                self.send_json({"error": f"Could not read folder: {exc}"}, status=500)
            return

        if parsed.path == "/api/file":
            query = urllib.parse.parse_qs(parsed.query)
            names = query.get("name", [])
            if not names:
                self.send_json({"error": "Missing file name."}, status=400)
                return

            try:
                path = self.resolve_json_file(names[0])
                raw = path.read_text(encoding="utf-8-sig")
                data = json.loads(raw)
                self.send_json(
                    {
                        "name": path.name,
                        "size": path.stat().st_size,
                        "data": data,
                        "raw": json.dumps(data, ensure_ascii=False, indent=2),
                        "nodeCount": count_nodes(data),
                    }
                )
            except json.JSONDecodeError as exc:
                line_text = ""
                try:
                    lines = raw.splitlines()
                    if 1 <= exc.lineno <= len(lines):
                        line_text = lines[exc.lineno - 1]
                except Exception:
                    pass
                pointer = ""
                if line_text:
                    pointer = f"\n\n{line_text}\n{' ' * max(exc.colno - 1, 0)}^"
                message = (
                    f"Invalid JSON in {names[0]}\n"
                    f"Line {exc.lineno}, column {exc.colno}: {exc.msg}{pointer}"
                )
                self.send_json({"error": message, "raw": raw}, status=422)
            except (OSError, PermissionError, FileNotFoundError) as exc:
                self.send_json({"error": str(exc)}, status=400)
            return

        self.send_json({"error": "Not found."}, status=404)


class JsonExplorerServer(ThreadingHTTPServer):
    def __init__(self, server_address: tuple[str, int], root_dir: Path):
        super().__init__(server_address, JsonExplorerHandler)
        self.root_dir = root_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Open a read-only browser explorer for JSON files.")
    parser.add_argument(
        "--folder",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Folder containing JSON files. Defaults to the script folder.",
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
        raise SystemExit(f"Folder does not exist: {root_dir}")

    server = JsonExplorerServer((HOST, 0), root_dir)
    port = server.server_address[1]
    url = f"http://{HOST}:{port}/"

    print(f"{APP_TITLE} v{APP_VERSION}")
    print(f"Build:  {BUILD_ID}")
    print(f"Script: {Path(__file__).resolve()}")
    print(f"Folder: {root_dir}")
    print(f"PID:    {os.getpid()}")
    print(f"Open:   {url}")
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
