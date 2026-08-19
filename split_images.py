"""
Split All25Images.png into 25 individual images.
Run this script to automatically crop and save each image.
"""
from PIL import Image
import os

# Configuration
INPUT_FILE = r"C:\Users\Lenovo\Desktop\CCTV_Installation_Manual\images\All25Images.png"
OUTPUT_DIR = r"C:\Users\Lenovo\Desktop\CCTV_Installation_Manual\images"

# Image names in order (5x5 grid, left to right, top to bottom)
IMAGE_NAMES = [
    "01_dome_camera.jpg",
    "02_bullet_camera.jpg",
    "03_ptz_camera.jpg",
    "04_dvr.jpg",
    "05_nvr.jpg",
    "06_bnc_connector.jpg",
    "07_rj45_connector.jpg",
    "08_dc_power_connector.jpg",
    "09_coaxial_cable.jpg",
    "10_cat6_cable.jpg",
    "11_fiber_optic_cable.jpg",
    "12_bnc_crimping_tool.jpg",
    "13_rj45_crimping_tool.jpg",
    "14_cable_tester.jpg",
    "15_multimeter.jpg",
    "16_surveillance_hdd.jpg",
    "17_pvc_conduit.jpg",
    "18_trunking.jpg",
    "19_poe_switch.jpg",
    "20_router.jpg",
    "21_wifi_camera.jpg",
    "22_smps_power.jpg",
    "23_hidden_camera.jpg",
    "24_cable_ties.jpg",
    "25_tool_kit.jpg",
]

def split_grid_image(input_path, output_dir, names, rows=5, cols=5):
    """Split a grid image into individual images."""
    if not os.path.exists(input_path):
        print(f"ERROR: File not found: {input_path}")
        return False
    
    try:
        img = Image.open(input_path)
        width, height = img.size
        print(f"Input image: {width}x{height}")
        
        cell_width = width // cols
        cell_height = height // rows
        print(f"Cell size: {cell_width}x{cell_height}")
        
        count = 0
        for row in range(rows):
            for col in range(cols):
                idx = row * cols + col
                if idx >= len(names):
                    break
                
                left = col * cell_width
                top = row * cell_height
                right = left + cell_width
                bottom = top + cell_height
                
                cropped = img.crop((left, top, right, bottom))
                
                # Save as JPG
                output_path = os.path.join(output_dir, names[idx])
                cropped.save(output_path, "JPEG", quality=95)
                print(f"  Saved: {names[idx]}")
                count += 1
        
        print(f"\nDone! {count} images saved to {output_dir}")
        return True
        
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("  Splitting All25Images.png into 25 files")
    print("=" * 50)
    print()
    split_grid_image(INPUT_FILE, OUTPUT_DIR, IMAGE_NAMES)
    print()
    input("Press Enter to exit...")
