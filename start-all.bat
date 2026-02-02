@echo off
echo ========================================
echo Investment Assistant - Full Stack Startup
echo ========================================
echo.
echo This will start both backend and frontend servers
echo.

:: Start backend in a new window
start "Investment Assistant - Backend" cmd /k "cd backend && py -3.11 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

:: Wait a bit for backend to start
timeout /t 5 /nobreak > nul

:: Start frontend in a new window
start "Investment Assistant - Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo Both servers are starting!
echo ========================================
echo.
echo Backend: http://localhost:8000
echo Backend API Docs: http://localhost:8000/docs
echo Frontend: Will be shown in the frontend window
echo.
echo Press any key to exit this window...
pause > nul
