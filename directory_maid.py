#!/usr/bin/env python3
# move_folders_safe.py
# Moves a list of folders from source to destination safely

import os
import shutil

# --- CONFIGURATION ---
SOURCE_DIR = "/path/to/source"        # Replace with your source directory
DEST_DIR = "/path/to/destination"     # Replace with your destination directory

# List of folder names to move
folders_to_move = [
    "Folder 1",
    "Another Folder",
    "Project_3"
]

# --- SAFETY CHECKS ---
if not os.path.isdir(SOURCE_DIR):
    print(f"Source directory does not exist: {SOURCE_DIR}")
    exit(1)

if not os.path.isdir(DEST_DIR):
    print(f"Destination directory does not exist. Creating: {DEST_DIR}")
    os.makedirs(DEST_DIR)

# --- MOVE FOLDERS ---
for folder_name in folders_to_move:
    src_path = os.path.join(SOURCE_DIR, folder_name)
    dest_path = os.path.join(DEST_DIR, folder_name)

    try:
        if os.path.isdir(src_path):
            print(f"Moving '{folder_name}'...")
            shutil.move(src_path, dest_path)
        else:
            print(f"Folder does not exist: '{folder_name}'")
    except Exception as e:
        print(f"Error moving '{folder_name}': {e}")

print("Done!")
