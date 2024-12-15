#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pipenv install

# Convert static asset files
pipenv run manage.py collectstatic --no-input

# Apply any outstanding database migrations
pipenv run manage.py migrate
