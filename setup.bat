@echo off
REM Setup Script for Online Course Application

setlocal enabledelayedexpansion

echo.
echo ======================================
echo Online Course Application - Setup
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Navigate to project directory
cd /d "c:\Users\Lifa.Mbangata\Downloads\Python App\onlinecourse"

if %errorlevel% neq 0 (
    echo ERROR: Could not navigate to project directory
    pause
    exit /b 1
)

echo Project directory: %cd%
echo.

REM Create virtual environment
echo [1/4] Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo DONE
echo.

REM Activate virtual environment and install requirements
echo [2/4] Installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo DONE
echo.

REM Run migrations
echo [3/4] Running database migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Failed to run migrations
    pause
    exit /b 1
)
echo DONE
echo.

REM Create superuser
echo [4/4] Creating superuser account...
echo Please enter superuser credentials:
python manage.py createsuperuser
if %errorlevel% neq 0 (
    echo WARNING: Failed to create superuser or skipped
)
echo.

echo ======================================
echo Setup completed successfully!
echo ======================================
echo.
echo To start the development server, run:
echo   cd c:\Users\Lifa.Mbangata\Downloads\Python App\onlinecourse
echo   venv\Scripts\activate.bat
echo   python manage.py runserver
echo.
echo Then access:
echo   Admin: http://localhost:8000/admin/
echo   Main: http://localhost:8000/
echo.
pause
