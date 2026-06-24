# Four 30-Day Learning Project Sets Design

## Goal

Create four independent 30-day learning project collections:

- Python 30 days
- JavaScript + CSS + HTML 30 days
- Pure C++ 30 days
- C language 30 days

Each day is a small runnable project with source code, a Chinese `README.md`, a Chinese `docs.html`, and a `run.ps1` script where relevant.

## Output Structure

Generate these directories under the workspace:

```text
python-30days/
web-js-css-html-30days/
cpp-30days/
c-30days/
learning-projects-index.html
```

Each course contains:

```text
assets/style.css
index.html
README.md
day01/
  README.md
  docs.html
  run.ps1
  source files
...
day30/
```

## Course Style

The projects are intentionally small and self-contained. They should be useful as daily learning checkpoints rather than large production systems.

- Python projects use only the standard library.
- Web projects use plain HTML, CSS, and JavaScript without external packages.
- C++ projects use standard C++17 and no Qt dependency.
- C projects use portable C11-style code and the C standard library.

## Verification

After generation:

- Run all 30 Python projects.
- Syntax-check all 30 JavaScript files with Node.
- Compile and run all 30 C++ projects with MinGW `g++`.
- Compile and run all 30 C projects with MinGW `gcc`.
- Confirm all required files exist.
- Remove verification build artifacts.
