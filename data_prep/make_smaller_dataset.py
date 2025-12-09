import os
import shutil
from pathlib import Path

def copy_sample_files(src_dir, dst_dir, fraction=0.1):
    """
    Copy a fraction of files from source to destination directory
    
    Args:
        src_dir: Source directory path
        dst_dir: Destination directory path
        fraction: Fraction of files to copy (default 0.1 = 10%)
    """
    # Create destination directory if it doesn't exist
    os.makedirs(dst_dir, exist_ok=True)
    
    # Get all files in source directory
    files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
    
    # Calculate number of files to copy
    num_files = int(len(files) * fraction)
    
    # Sort files to ensure consistency
    files.sort()
    
    # Copy the first num_files
    for i, file in enumerate(files[:num_files]):
        src_path = os.path.join(src_dir, file)
        dst_path = os.path.join(dst_dir, file)
        shutil.copy2(src_path, dst_path)
        
        if (i + 1) % 100 == 0:
            print(f"  Copied {i + 1}/{num_files} files...")
    
    print(f"✓ Copied {num_files} files from {src_dir} to {dst_dir}")
    return num_files

def create_sample_dataset(base_dir='train_test_data', new_dir='new_train_test_data', fraction=0.1):
    """
    Create a sample dataset with a fraction of the original files
    
    Args:
        base_dir: Original dataset directory
        new_dir: New dataset directory
        fraction: Fraction of files to copy (default 0.1 = 10%)
    """
    print("="*60)
    print(f"Creating sample dataset ({fraction*100}% of original)")
    print("="*60)
    
    # Define directory mappings
    directories = [
        ('test', 'test'),
        ('train/images', 'train/images'),
        ('train/labels', 'train/labels'),
        ('val/images', 'val/images'),
        ('val/labels', 'val/labels'),
    ]
    
    total_files = 0
    
    for src_subdir, dst_subdir in directories:
        src_path = os.path.join(base_dir, src_subdir)
        dst_path = os.path.join(new_dir, dst_subdir)
        
        print(f"\nProcessing: {src_path}")
        
        if os.path.exists(src_path):
            num_files = copy_sample_files(src_path, dst_path, fraction)
            total_files += num_files
        else:
            print(f"✗ Directory not found: {src_path}")
    
    print("\n" + "="*60)
    print(f"Sample dataset created successfully!")
    print(f"Total files copied: {total_files}")
    print(f"Location: {new_dir}")
    print("="*60)

if __name__ == "__main__":
    # Create sample dataset with 10% of original files
    create_sample_dataset(
        base_dir='train_test_data',
        new_dir='new_train_test_data',
        fraction=0.1  # Change this to 0.05 for 5%, 0.2 for 20%, etc.
    )