#!/usr/bin/fish

# ARC Protocol v2.1 - Fish Bootstrapper
# This script delegates all logic to setup_arc.py for consistency.

echo (set_color cyan)"🚀 Bootstrapping ARC Installation via Python Wizard..."

# Check for Python
if not command -v python3 &> /dev/null
    echo (set_color red)"❌ ERROR: python3 is required to install ARC."
    exit 1
end

# Run the Universal Setup Wizard
python3 setup_arc.py
