#!/usr/bin/env bash

# ARC Protocol v2.0 - Shell Bootstrapper
# This script delegates all logic to setup_arc.py for consistency.

echo "🚀 Bootstrapping ARC Installation via Python Wizard..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: python3 is required to install ARC."
    exit 1
fi

# Run the Universal Setup Wizard
python3 setup_arc.py
