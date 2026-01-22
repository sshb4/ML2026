# Capstone Project — Local Setup

This repository contains the minimal local setup for the capstone dataset verification.

Files included:
- `capstone_local.ipynb` — Jupyter notebook that loads and inspects `df_power.csv`.
- `generate_capstone_report.py` — small script that loads `df_power.csv` and prints/writes a short summary (optional).
- `requirements.txt` — pinned Python dependencies.
- `.gitignore` — ignores virtualenv and `df_power.csv` by default.

Quick reproduction steps (local macOS / zsh):

```bash
# create a project venv
python3.11 -m venv .venv311
source .venv311/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

# run the notebook (optional):
# jupyter lab

# or run the verification script:
python generate_capstone_report.py
```

Notes:
- `df_power.csv` is intentionally ignored by `.gitignore`. Add it manually if you want it tracked.
- The notebook demonstrates loading and basic inspection; you can run it inside the venv to verify the environment.
