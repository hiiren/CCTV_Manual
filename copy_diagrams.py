"""
Copy diagram images from ChatGPT folder to images folder with proper names.
Run this script to rename and copy the diagram images.
"""
import shutil
import os

# Source and destination
DIAGRAMS_DIR = r"C:\Users\Lenovo\Desktop\CCTV_Installation_Manual\diagrams"
IMAGES_DIR = r"C:\Users\Lenovo\Desktop\CCTV_Installation_Manual\images"

# Map ChatGPT filenames to our naming convention
# Update these mappings based on what the images actually contain
DIAGRAM_MAPPINGS = {
    # First diagram image - update the source filename and target name
    "ChatGPT Image Jul 17, 2026, 06_12_23 PM.png": "diagram_access_control.png",
    # Second diagram image
    "ChatGPT Image Jul 17, 2026, 06_14_39 PM.png": "diagram_boom_barrier.png",
}

def copy_diagrams():
    """Copy and rename diagram images."""
    print("=" * 50)
    print("  Copying diagram images to images folder")
    print("=" * 50)
    print()
    
    count = 0
    for src_name, dst_name in DIAGRAM_MAPPINGS.items():
        src_path = os.path.join(DIAGRAMS_DIR, src_name)
        dst_path = os.path.join(IMAGES_DIR, dst_name)
        
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"  Copied: {src_name}")
            print(f"       -> {dst_name}")
            count += 1
        else:
            print(f"  NOT FOUND: {src_name}")
        print()
    
    print(f"Done! {count} diagrams copied to images folder")
    print()
    
    # List all files in images folder
    print("Files in images folder:")
    print("-" * 40)
    for f in sorted(os.listdir(IMAGES_DIR)):
        size = os.path.getsize(os.path.join(IMAGES_DIR, f))
        print(f"  {f:<40} {size:>10,} bytes")

if __name__ == "__main__":
    copy_diagrams()
    print()
    input("Press Enter to exit...")
