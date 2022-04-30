#!/bin/bash
python -m venv .venv
pip install -U pip
source .venv/bin/activate
pip install -r requirements.txt
mkdir build
cd build
pyinstaller ../src/main.py -F -w --clean -n "Snake"
cp -r ../assets ./dist/