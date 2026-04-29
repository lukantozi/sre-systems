#!/usr/bin/env bash
set -euo pipefail

PY="${PY:-python3}"
script="$1"
input="$2"

echo "== Running: $script < $input =="
time "$PY" "$script" < "$input"
