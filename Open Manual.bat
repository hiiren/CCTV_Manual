@echo off
title CCTV Training Manual - Launcher
color 0A

echo.
echo  ╔══════════════════════════════════════════════════════════╗
echo  ║         CCTV TRAINING MANUAL - LAUNCHER                ║
echo  ╚══════════════════════════════════════════════════════════╝
echo.
echo  Starting server...
echo.

cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo  ERROR: Python not found!
    echo.
    echo  Please install Python from: https://python.org
    echo  Make sure to check "Add Python to PATH" during install.
    echo.
    pause
    exit /b 1
)

echo  Server starting on http://localhost:8080
echo.
echo  ══════════════════════════════════════════════════════════
echo.
echo  Opening browser in 2 seconds...
echo  Press Ctrl+C to stop the server.
echo.
echo  ══════════════════════════════════════════════════════════
echo.

REM Wait 2 seconds then open browser
timeout /t 2 /nobreak >nul
start http://localhost:8080/manual.html

REM Start the server
python -m http.server 8080
