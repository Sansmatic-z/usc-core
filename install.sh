#!/bin/bash

# USC Core - Termux Setup Script
# This script prepares your environment and installs the 'usc' command.

echo "--- USC System Initialization ---"

# 1. Check for Python
if ! command -v python3 &> /dev/null
then
    echo "[!] Python3 not found. Installing..."
    pkg install python -y
else
    echo "[✓] Python3 is ready."
fi

# 2. Upgrade pip
echo "[*] Ensuring pip is up to date..."
python3 -m pip install --upgrade pip

# 3. Install USC in editable mode
# This allows you to modify the code and see changes instantly.
echo "[*] Installing USC Core library..."
cd "$(dirname "$0")"
python3 -m pip install -e .

# 4. Verify Installation
if command -v usc &> /dev/null
then
    echo "[✓] USC System successfully installed!"
    echo "---"
    echo "You can now run USC using the 'usc' command."
    echo "Try: usc view examples/hello.usc"
else
    # Fallback if pip bin is not in PATH
    echo "[!] Note: 'usc' command not in PATH."
    echo "You can run it using: python3 cli.py"
    echo "To fix this, add this to your ~/.bashrc:"
    echo 'export PATH=$PATH:~/.local/bin'
fi

echo "--- Setup Complete ---"
