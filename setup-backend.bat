@echo off
echo ========================================
echo Investment Assistant - Backend Setup
echo ========================================
echo.

cd backend

echo Checking Python version...
python --version
echo.

echo Installing Python dependencies...
pip install -r requirements.txt
echo.

echo ========================================
echo Backend setup complete!
echo ========================================
echo.
echo To start the backend server, run: start-backend.bat
pause
