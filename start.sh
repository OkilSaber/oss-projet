#!/bin/bash
python -m venv .venv
pip -u pip
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
