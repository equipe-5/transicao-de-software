#!/usr/bin/env bash

set -e

: "${MODE:=development}"

echo "Installing requirements"
if [ "$MODE" = "development" ]; then
    pip3 install --no-input --no-cache-dir -r "$1/development.txt"
elif [ "$MODE" = "staging" ]; then
    pip3 install --no-input --no-cache-dir -r "$1/staging.txt"
elif [ "$MODE" = "production" ]; then
    pip3 install --no-input --no-cache-dir -r "$1/production.txt"
fi
echo "Requirements installed"
