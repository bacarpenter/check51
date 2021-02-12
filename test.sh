#!/bin/sh

clear

# Activate virtual env 
echo "Activating venv"
source ~/Code/check51/env/bin/activate

# Uninstall old version
echo "Uninstalling..."
cd ~/Code/check51
pip uninstall check51 -y -q 
echo "Done!"

# Install new version
echo "Installing new version"
pip install . -q
echo "Done!"

# Run the demo!
echo "Running demo:"
cd ./demo
check51 -d tests/
