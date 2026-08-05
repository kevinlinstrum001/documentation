# Local JSON Explorer v1.6.0 — PST-SP Upgrade

Place these together in the viewer `tools` folder:

- `json-viewer-v1.5.0.py`
- `upgrade-json-viewer-1.5.0-to-1.6.0.py`

Run:

```bat
py -3 upgrade-json-viewer-1.5.0-to-1.6.0.py
```

The patcher creates `json-viewer-v1.6.0.py` and leaves v1.5.0 unchanged.

The PST-SP preview activates when the sidecar contains:

```json
"profile": { "previewMode": "pst-sp-study-guide" }
```

It adds tabs for Overview, Toolkits, Exercises, Measures, Visuals, and Coverage. Exercise and visual lists are filterable, and JSON buttons reveal the corresponding source record in Tree view.
