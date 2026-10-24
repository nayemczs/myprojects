#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Create the output directory for static files
mkdir -p staticfiles_build/static
cp -r staticfiles_build_temp/* staticfiles_build/static/ 2>/dev/null || true
