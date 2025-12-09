import os
import shutil
from pathlib import Path
from collections import defaultdict
import re

def split_dataset():
    """
    Split dataset into train/val/test with 8/1/1 pattern for each camera
    """
    # Define directories
    dataset_dir = Path("dataset")
    labels_dir = Path("labels")
    
    train_img_dir = Path("train_test_data/train/images")
    train_lbl_dir = Path("train_test_data/train/labels")
    val_img_dir = Path("train_test_data/val/images")
    val_lbl_dir = Path("train_test_data/val/labels")
    test_img_dir = Path("train_test_data/test")  # Only images for test, no labels
    
    # Create directories if they don't exist
    for dir_path in [train_img_dir, train_lbl_dir, val_img_dir, val_lbl_dir, test_img_dir]:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Check source directories
    if not dataset_dir.exists() or not labels_dir.exists():
        print("Error: dataset/ or labels/ directory doesn't exist!")
        return
    
    # Get all jpg files
    jpg_files = list(dataset_dir.glob("*.jpg"))
    print(f"Total images found: {len(jpg_files)}\n")
    
    # Group files by prefix
    prefix_files = defaultdict(list)
    
    for jpg_file in jpg_files:
        filename = jpg_file.stem
        
        # Extract prefix (cam_XX or src_X_frame)
        cam_match = re.match(r'(cam_\d+)_', filename)
        if cam_match:
            prefix = cam_match.group(1)
            prefix_files[prefix].append(jpg_file)
            continue
        
        src_match = re.match(r'(src_\d+_frame)_', filename)
        if src_match:
            prefix = src_match.group(1)
            prefix_files[prefix].append(jpg_file)
            continue
        
        # Other files
        prefix_files["other"].append(jpg_file)
    
    # Sort files within each prefix to maintain order
    for prefix in prefix_files:
        prefix_files[prefix].sort(key=lambda x: x.name)
    
    # Counters
    train_count = 0
    val_count = 0
    test_count = 0
    
    print("Splitting dataset with 8/1/1 pattern...\n")
    
    # Process each prefix
    for prefix, files in sorted(prefix_files.items()):
        print(f"Processing {prefix}: {len(files)} images")
        
        prefix_train = 0
        prefix_val = 0
        prefix_test = 0
        
        for idx, jpg_file in enumerate(files):
            filename = jpg_file.stem
            txt_file = labels_dir / f"{filename}.txt"
            
            # Check if label exists
            if not txt_file.exists():
                print(f"  Warning: Label not found for {filename}, skipping...")
                continue
            
            # Determine destination based on pattern (8 train, 1 val, 1 test)
            position_in_cycle = idx % 10
            
            if position_in_cycle < 8:  # First 8 go to train
                dest_img = train_img_dir / jpg_file.name
                dest_lbl = train_lbl_dir / txt_file.name
                train_count += 1
                prefix_train += 1
            elif position_in_cycle == 8:  # 9th goes to val
                dest_img = val_img_dir / jpg_file.name
                dest_lbl = val_lbl_dir / txt_file.name
                val_count += 1
                prefix_val += 1
            else:  # 10th goes to test (only image, no label)
                dest_img = test_img_dir / jpg_file.name
                dest_lbl = None  # No label for test set
                test_count += 1
                prefix_test += 1
            
            # Copy files
            try:
                shutil.copy2(jpg_file, dest_img)
                if dest_lbl:  # Only copy label if it's not test set
                    shutil.copy2(txt_file, dest_lbl)
            except Exception as e:
                print(f"  Error copying {filename}: {e}")
        
        print(f"  → Train: {prefix_train}, Val: {prefix_val}, Test: {prefix_test}")
    
    # Final summary
    total = train_count + val_count + test_count
    print("\n" + "="*60)
    print("SPLIT COMPLETE!")
    print("="*60)
    print(f"Train set: {train_count} images ({train_count/total*100:.1f}%)")
    print(f"Val set:   {val_count} images ({val_count/total*100:.1f}%)")
    print(f"Test set:  {test_count} images ({test_count/total*100:.1f}%)")
    print(f"Total:     {total} images")
    print("\nFiles copied to train_test_data/ directory structure.")

if __name__ == "__main__":
    split_dataset()