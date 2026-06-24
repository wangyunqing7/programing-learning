# Four 30-Day Learning Project Sets Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate 120 small learning projects across Python, Web, C++, and C.

**Architecture:** A single generator script writes all four course trees from structured metadata and templates. Verification uses the local bundled Python/Node runtimes and the local MinGW GCC/G++ toolchain.

**Tech Stack:** Python generator, Python 3.12, Node 24, HTML/CSS/JavaScript, MinGW GCC/G++ 13.1.

---

### Task 1: Create Generator

**Files:**
- Create: `tools/generate_four_language_projects.py`

- [ ] Define metadata for 30 days per language.
- [ ] Generate daily source files, `README.md`, `docs.html`, and `run.ps1`.
- [ ] Generate per-course and top-level HTML indexes.

### Task 2: Generate Projects

**Files:**
- Create: `python-30days/**`
- Create: `web-js-css-html-30days/**`
- Create: `cpp-30days/**`
- Create: `c-30days/**`
- Create: `learning-projects-index.html`

- [ ] Run the generator from the workspace root.
- [ ] Confirm four course directories and 120 daily directories exist.

### Task 3: Verify

- [ ] Run every Python `main.py`.
- [ ] Run `node --check` for every web `script.js`.
- [ ] Compile and run every C++ `main.cpp`.
- [ ] Compile and run every C `main.c`.
- [ ] Confirm required daily docs and scripts exist.

### Task 4: Clean and Report

- [ ] Remove verification build artifacts.
- [ ] Report generated locations and verification results.
