@echo off
echo ========================================
echo Investment Assistant - Frontend Setup
echo ========================================
echo.

cd frontend

echo Checking Node.js version...
node --version
echo.

echo Checking npm version...
npm --version
echo.

echo Installing Node.js dependencies...
npm install
echo.

echo ========================================
echo Frontend setup complete!
echo ========================================
echo.
echo To start the frontend server, run: start-frontend.bat
pause
