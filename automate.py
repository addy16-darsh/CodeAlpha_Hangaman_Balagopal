# -*- coding: utf-8 -*-
"""Untitled29.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KT8EKahX-Zli08EKmrHnjibYsDXhT8cd
"""

import os
import shutil

# Define file extensions and their corresponding folders
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".apk", ".bat"],
    "Others": []  # Catch-all for files without specific extensions
}

# Function to organize files
def organize_files(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Create categorized folders if not already present
    for folder in FILE_CATEGORIES.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Move files into corresponding folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file extension
        _, file_extension = os.path.splitext(filename)

        # Move file to the appropriate folder
        moved = False
        for folder, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                print(f"Moved: {filename} -> {folder}")
                moved = True
                break

        # Move to "Others" if no match
        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others", filename))
            print(f"Moved: {filename} -> Others")

    print("\nFile organization complete!")

if __name__ == "__main__":
    # Specify the directory to organize (e.g., Downloads folder)
    directory_to_organize = input("Enter the directory path to organize: ").strip()
    organize_files(directory_to_organize)