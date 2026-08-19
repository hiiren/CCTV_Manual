@echo off
title CCTV Manual - Dashboard
color 0B

echo.
echo  ╔══════════════════════════════════════════════════════════╗
echo  ║         CCTV MANUAL - STATUS DASHBOARD                 ║
echo  ╚══════════════════════════════════════════════════════════╝
echo.
echo  Starting server...
echo.

cd /d "%~dp0"

python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo  ERROR: Python not found!
    echo  Please install Python from: https://python.org
    pause
    exit /b 1
)

echo  Server starting on http://localhost:8080
echo.
echo  Opening dashboard in 2 seconds...
echo  Press Ctrl+C to stop the server.
echo.

timeout /t 2 /nobreak >nul
start http://localhost:8080/index.html

python -m http.server 8080
