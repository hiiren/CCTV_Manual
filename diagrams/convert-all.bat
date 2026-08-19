@echo off
echo ========================================
echo  Mermaid Diagram Converter
echo ========================================
echo.
echo This script converts Mermaid diagrams to PNG images.
echo.
echo Prerequisites:
echo   1. Install Node.js from https://nodejs.org
echo   2. Run: npm install -g @mermaid-js/mermaid-cli
echo.
echo After installing, place individual .mmd files in this folder
echo and run this script to convert them all to PNG.
echo ========================================
echo.

REM Check if mmdc is installed
where mmdc >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: mermaid-cli not found!
    echo.
    echo Install it by running:
    echo   npm install -g @mermaid-js/mermaid-cli
    echo.
    echo Then run this script again.
    pause
    exit /b 1
)

echo Converting .mmd files to PNG...
echo.

for %%f in (*.mmd) do (
    echo Converting: %%f
    mmdc -i "%%f" -o "..\images\%%~nf.png" -b transparent -w 1200
    if %errorlevel% equ 0 (
        echo   SUCCESS: %%~nf.png created
    ) else (
        echo   FAILED: %%f
    )
    echo.
)

echo ========================================
echo  Conversion Complete!
echo ========================================
echo.
echo Check the images\ folder for PNG files.
echo.
pause
