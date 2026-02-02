@echo off
echo ========================================
echo Starting Investment Assistant Backend
echo ========================================
echo.

cd backend

echo Backend server starting on http://localhost:8000
echo API docs available at http://localhost:8000/docs
echo.

py -3.11 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
