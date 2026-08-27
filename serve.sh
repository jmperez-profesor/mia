#!/bin/bash
set -e
python3 -m venv ~/virtual-envs/mia-mkdocs
source ~/virtual-envs/mia-mkdocs/bin/activate
pip install -r requirements.txt
mkdocs serve
