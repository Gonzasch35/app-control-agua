#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt

cd backend

python3 manage.py collections --no-input
python3 manage.py migrate