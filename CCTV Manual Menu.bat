@echo off
title CCTV Manual - Quick Menu
color 0F

:menu
cls
echo.
echo  ╔══════════════════════════════════════════════════════════╗
echo  ║           CCTV TRAINING MANUAL - MAIN MENU             ║
echo  ╚══════════════════════════════════════════════════════════╝
echo.
echo  Select an option:
echo.
echo    [1] Open Manual (Full Viewer)
echo    [2] Open Dashboard (Status Page)
echo    [3] Setup Images (Split & Copy)  <-- NEW!
echo    [4] Convert Diagrams to PNG
echo    [5] Open Images Folder
echo    [6] Open Diagrams Folder
echo    [7] Exit
echo.
echo  ══════════════════════════════════════════════════════════
echo.

set /p choice="  Enter choice (1-7): "

if "%choice%"=="1" goto manual
if "%choice%"=="2" goto dashboard
if "%choice%"=="3" goto setup
if "%choice%"=="4" goto convert
if "%choice%"=="5" goto images
if "%choice%"=="6" goto diagrams
if "%choice%"=="7" goto exit

echo  Invalid choice. Try again.
timeout /t 2 >nul
goto menu

:manual
cd /d "%~dp0"
start http://localhost:8080/manual.html
python -m http.server 8080
goto menu

:dashboard
cd /d "%~dp0"
start http://localhost:8080/index.html
python -m http.server 8080
goto menu

:setup
cd /d "%~dp0"
call "Setup Images.bat"
goto menu

:convert
cd /d "%~dp0\diagrams"
call convert-all.bat
goto menu

:images
explorer "%~dp0images"
goto menu

:diagrams
explorer "%~dp0diagrams"
goto menu

:exit
exit
