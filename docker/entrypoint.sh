#!/usr/bin/env bash
set -e

if [ "$1" = 'bash' ]; then
  exec bash
else
  python server.py
fi