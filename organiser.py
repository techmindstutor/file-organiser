import os
import shutil
from pathlib import Path

# Define file type categories
FILE_TYPES = {
    "images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "videos":    [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "audio":     [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "code":      [".py", ".js", ".html", ".css", ".java", ".cpp", ".ts"],
    "others":    []
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "others"

def organise_folder(folder_path):
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Folder not found: {folder_path}")
        return

    moved = 0
    skipped = 0

    for file in folder.iterdir():
        # Skip folders and hidden files
        if file.is_dir() or file.name.startswith("."):
            skipped += 1
            continue

        # Get category for this file
        category = get_category(file.suffix)

        # Create category subfolder if it doesn't exist
        destination_folder = folder / category
        destination_folder.mkdir(exist_ok=True)

        # Move the file
        destination = destination_folder / file.name
        shutil.move(str(file), str(destination))
        print(f"Moved: {file.name} → /{category}")
        moved += 1

    print(f"\nDone. {moved} files organised, {skipped} items skipped.")

if __name__ == "__main__":
    # Change this path to any folder you want to organise
    target_folder = input("Enter the folder path to organise: ")
    organise_folder(target_folder)