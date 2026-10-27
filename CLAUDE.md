# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

Wi-Fi Signal Mapper (course "Project 1"): a Python tool that reads Wi-Fi RSSI measurements from a CSV and renders an interpolated heatmap PNG. The repo currently contains **only planning documents** — no source code, tests, or dependency manifest exist yet.

- `SPEC.md` — the authoritative requirements (R1–R5), constraints, and I/O interface. Implementation should be traceable to these requirement IDs.
- `README.md` — project proposal (problem, team, tools plan).
- `AI_USE.md` — a log of AI tool usage required by the course. When AI assistance produces a meaningful artifact (spec changes, new modules, etc.), add a row: date, tool, purpose, key outcome.

## Requirements summary (from SPEC.md)

- **Input:** CSV with columns `x,y,rssi` (coordinates + RSSI in dBm).
- **R1/R5:** Require at least 20 data points and no missing fields; otherwise print an error and exit cleanly (non-zero exit, no traceback).
- **R2:** 2D spatial interpolation over a grid of unmeasured points (SciPy, e.g. `scipy.interpolate.griddata`).
- **R3/R4:** Save a color-coded heatmap as `.png` with a labeled colorbar in dBm.
- **Performance:** PNG must render in under 10 seconds (live demo constraint).
- **Stack:** Python 3.10+, pandas, numpy, scipy, matplotlib.

## Environment

A local virtualenv exists at `.venv` (Python 3.14, Windows) with pandas, numpy, scipy, and matplotlib installed.

```bash
# Git Bash
source .venv/Scripts/activate
# PowerShell
.venv\Scripts\Activate.ps1

pip install pandas numpy scipy matplotlib
```

`.gitignore` excludes `.venv/`, bytecode, and all `*.png` files (generated heatmaps). Use `git add -f` if a PNG must be committed, e.g. a sample output for the README.
