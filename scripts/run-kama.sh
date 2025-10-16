#!/usr/bin/env bash
set -euo pipefail

# Usage: ./post_json.sh [path/to/file.json]

# Default path (used if no argument is passed)
DEFAULT_JSON_PATH="./data/sample.json"

# If user provides a path, use it; otherwise fall back
JSON_PATH="${1:-$DEFAULT_JSON_PATH}"

# Verify file exists
if [[ ! -f "$JSON_PATH" ]]; then
  echo "❌ JSON file not found: $JSON_PATH" >&2
  exit 1
fi

# POST to localhost:8080/kama
echo "📤 Sending $JSON_PATH → http://localhost:8080/kama"
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d @"$JSON_PATH" \
  http://localhost:8080/kama | jq .
