@echo off
title CCTV Manual - Image Setup Wizard
color 0F
cls

echo.
echo  ╔══════════════════════════════════════════════════════════╗
echo  ║         CCTV MANUAL - IMAGE SETUP WIZARD               ║
echo  ╚══════════════════════════════════════════════════════════╝
echo.
echo  This script will:
echo    1. Split All25Images.png into 25 separate images
echo    2. Copy diagram images to the images folder
echo    3. Update the manual to use all images
echo.
echo  ══════════════════════════════════════════════════════════
echo.

cd /d "%~dp0"

REM Check if Pillow is installed
python -c "from PIL import Image" 2>nul
if %errorlevel% neq 0 (
    echo  Installing Pillow library...
    pip install Pillow
    echo.
)

echo  Step 1: Splitting All25Images.png into 25 images...
echo  ─────────────────────────────────────────────────────
echo.
python split_images.py
echo.

echo  Step 2: Copying diagram images...
echo  ─────────────────────────────────────────────────────
echo.
python copy_diagrams.py
echo.

echo  ══════════════════════════════════════════════════════════
echo  Setup complete! 
echo  ══════════════════════════════════════════════════════════
echo.
echo  You can now:
echo    - Run "Open Manual.bat" to view the manual
echo    - Run "Open Dashboard.bat" to see status
echo.
pause
