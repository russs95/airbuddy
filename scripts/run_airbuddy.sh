#!/usr/bin/env bash
set -e

APP_DIR="/home/airbuddy/airbuddy_v1"
cd "$APP_DIR"

# Activate venv
source .venv/bin/activate

# Ensure imports work from src/
export PYTHONPATH="$APP_DIR/src"

# Run
exec python "$APP_DIR/src/main.py"
