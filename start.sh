#!/bin/bash
python -m venv .venv
pip install -U pip
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py