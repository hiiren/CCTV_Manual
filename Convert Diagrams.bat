@echo off
title CCTV Manual - Convert Diagrams
color 0E

echo.
echo  ╔══════════════════════════════════════════════════════════╗
echo  ║         DIAGRAM CONVERTER - Mermaid to PNG             ║
echo  ╚══════════════════════════════════════════════════════════╝
echo.

cd /d "%~dp0\diagrams"

REM Check if mmdc is installed
where mmdc >nul 2>nul
if %errorlevel% neq 0 (
    echo  mermaid-cli not found!
    echo.
    echo  To install, run these commands in order:
    echo.
    echo    1. npm install -g @mermaid-js/mermaid-cli
    echo    2. Then run this script again
    echo.
    echo  If npm is not installed, get Node.js from:
    echo    https://nodejs.org
    echo.
    pause
    exit /b 1
)

echo  Converting Mermaid diagrams to PNG...
echo.

set count=0
for %%f in (*.mmd) do (
    set /a count+=1
    echo  Converting: %%f
    mmdc -i "%%f" -o "..\images\%%~nf.png" -b white -w 1200
    if !errorlevel! equ 0 (
        echo    SUCCESS: %%~nf.png
    ) else (
        echo    FAILED: %%f
    )
    echo.
)

echo  ══════════════════════════════════════════════════════════
echo  Conversion complete! Check images\ folder.
echo  ══════════════════════════════════════════════════════════
echo.
pause
