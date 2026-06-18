@echo off
REM 🚀 DORAEMON AI - WINDOWS INSTANT START SCRIPT
REM Run this to start everything automatically!

echo.
echo 🤖 Starting Doraemon AI...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo ✅ Python found

REM Install dependencies
echo 📦 Installing dependencies...
python -m pip install -r requirements.txt --quiet

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed
echo.
echo ==========================================
echo 🤖 DORAEMON AI IS READY!
echo ==========================================
echo.
echo 🔧 Backend: http://localhost:5000
echo 🎨 Frontend: Open index.html in your browser
echo.
echo Press Ctrl+C to stop the server
echo.
echo ==========================================
echo.

REM Start the Flask app
python app.py

pause
