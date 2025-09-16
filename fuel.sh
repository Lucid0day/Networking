#!/bin/bash

# Run your Python script
python3 /path/to/your_script.py &

# Start mitmweb
mitmweb &

# Open Wireshark GUI
open -a Wireshark
