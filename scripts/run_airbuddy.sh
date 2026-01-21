#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/home/airbuddy/airbuddy_v1"
cd "$APP_DIR"

source "$APP_DIR/.venv/bin/activate"
export PYTHONPATH="$APP_DIR/src"

exec "$APP_DIR/.venv/bin/python" "$APP_DIR/src/main.py"
