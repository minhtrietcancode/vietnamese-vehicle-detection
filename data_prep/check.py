import os
from pathlib import Path
from collections import defaultdict
import re

def analyze_dataset():
    """
    Analyze the dataset to count images by camera/source type
    """
    dataset_dir = Path("dataset")
    
    # Check if directory exists
    if not dataset_dir.exists():
        print(f"Error: Directory '{dataset_dir}' does not exist!")
        return
    
    # Get all .jpg files
    jpg_files = list(dataset_dir.glob("*.jpg"))
    
    if not jpg_files:
        print(f"No .jpg files found in '{dataset_dir}' directory.")
        return
    
    print(f"Total images found: {len(jpg_files)}\n")
    print("="*60)
    
    # Dictionary to store counts by prefix
    prefix_counts = defaultdict(int)
    prefix_examples = defaultdict(list)
    
    # Analyze each file
    for jpg_file in jpg_files:
        filename = jpg_file.stem  # Get filename without extension
        
        # Extract prefix based on patterns
        # Pattern 1: cam_XX_XXXXX -> cam_XX
        cam_match = re.match(r'(cam_\d+)_\d+', filename)
        if cam_match:
            prefix = cam_match.group(1)
            prefix_counts[prefix] += 1
            if len(prefix_examples[prefix]) < 3:  # Store first 3 examples
                prefix_examples[prefix].append(filename)
            continue
        
        # Pattern 2: src_X_frame_XXX -> src_X_frame
        src_match = re.match(r'(src_\d+_frame)_\d+', filename)
        if src_match:
            prefix = src_match.group(1)
            prefix_counts[prefix] += 1
            if len(prefix_examples[prefix]) < 3:
                prefix_examples[prefix].append(filename)
            continue
        
        # If no pattern matches, store as "other"
        prefix_counts["other"] += 1
        if len(prefix_examples["other"]) < 3:
            prefix_examples["other"].append(filename)
    
    # Sort by prefix name
    sorted_prefixes = sorted(prefix_counts.items())
    
    # Display results
    print("DATASET BREAKDOWN BY PREFIX:\n")
    
    total_categorized = 0
    for prefix, count in sorted_prefixes:
        print(f"{prefix}:")
        print(f"  Count: {count} images")
        print(f"  Examples: {', '.join(prefix_examples[prefix])}")
        print()
        total_categorized += count
    
    print("="*60)
    print(f"\nSUMMARY:")
    print(f"Total unique prefixes: {len(prefix_counts)}")
    print(f"Total images categorized: {total_categorized}")
    
    # Check for missing labels
    labels_dir = Path("labels")
    if labels_dir.exists():
        txt_files = set([f.stem for f in labels_dir.glob("*.txt")])
        jpg_stems = set([f.stem for f in jpg_files])
        
        missing_labels = jpg_stems - txt_files
        missing_images = txt_files - jpg_stems
        
        print(f"\nLABEL VERIFICATION:")
        print(f"Images without labels: {len(missing_labels)}")
        print(f"Labels without images: {len(missing_images)}")
        
        if missing_labels:
            print(f"\nFirst 5 images missing labels:")
            for stem in list(missing_labels)[:5]:
                print(f"  - {stem}")
        
        if missing_images:
            print(f"\nFirst 5 labels missing images:")
            for stem in list(missing_images)[:5]:
                print(f"  - {stem}")

if __name__ == "__main__":
    analyze_dataset()