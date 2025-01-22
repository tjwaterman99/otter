#!/bin/bash

poetry install
rm -r build/
rm -r dist/
poetry run pyinstaller run.py --name otter --onefile
