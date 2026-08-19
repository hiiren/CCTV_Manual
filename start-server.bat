@echo off
echo ========================================
echo  CCTV Manual - Local Server
echo ========================================
echo.
echo Starting server on http://localhost:8080
echo.
echo Open this URL in your browser:
echo   http://localhost:8080/manual.html
echo.
echo Press Ctrl+C to stop the server.
echo ========================================
echo.
cd /d "%~dp0"
python -m http.server 8080
