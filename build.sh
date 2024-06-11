#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt

cd backend

#python3 manage.py collectstatic --no-input
python3 manage.py migrate