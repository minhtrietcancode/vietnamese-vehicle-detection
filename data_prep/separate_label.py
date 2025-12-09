import os
import shutil
from pathlib import Path

def separate_labels():
    """
    Move all .txt label files from dataset/ directory to labels/ directory
    """
    # Define source and destination directories
    source_dir = Path("dataset")
    dest_dir = Path("labels")
    
    # Create destination directory if it doesn't exist
    dest_dir.mkdir(exist_ok=True)
    
    # Check if source directory exists
    if not source_dir.exists():
        print(f"Error: Source directory '{source_dir}' does not exist!")
        return
    
    # Get all .txt files from source directory
    txt_files = list(source_dir.glob("*.txt"))
    
    if not txt_files:
        print(f"No .txt files found in '{source_dir}' directory.")
        return
    
    print(f"Found {len(txt_files)} label files to move...")
    
    # Move each .txt file to destination directory
    moved_count = 0
    for txt_file in txt_files:
        try:
            dest_path = dest_dir / txt_file.name
            shutil.move(str(txt_file), str(dest_path))
            moved_count += 1
            print(f"Moved: {txt_file.name}")
        except Exception as e:
            print(f"Error moving {txt_file.name}: {e}")
    
    print(f"\nSuccessfully moved {moved_count}/{len(txt_files)} files to '{dest_dir}' directory.")

if __name__ == "__main__":
    separate_labels()