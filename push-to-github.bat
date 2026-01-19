@echo off
REM Automated Git Setup and Push Script for Online Course Application

setlocal enabledelayedexpansion

echo.
echo ======================================
echo Online Course Application - Git Setup
echo ======================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from: https://git-scm.com/download/win
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

REM Initialize git
echo [1/6] Initializing git repository...
git init
if %errorlevel% neq 0 (
    echo ERROR: Failed to initialize git
    pause
    exit /b 1
)
echo DONE
echo.

REM Configure git user
echo [2/6] Configuring git user...
git config user.email "lifa.mbangata@example.com"
git config user.name "Lifa Mbangata"
echo DONE
echo.

REM Add all files
echo [3/6] Adding all files to git...
git add .
if %errorlevel% neq 0 (
    echo ERROR: Failed to add files
    pause
    exit /b 1
)
echo DONE
echo.

REM Commit files
echo [4/6] Committing files...
git commit -m "Initial commit: Complete Online Course Application with exam features"
if %errorlevel% neq 0 (
    echo ERROR: Failed to commit files
    pause
    exit /b 1
)
echo DONE
echo.

REM Add remote
echo [5/6] Adding remote repository...
git remote add origin https://github.com/Lifa-Mbangata/Online-Couse-Application.git
if %errorlevel% neq 0 (
    echo WARNING: Remote may already exist or URL is incorrect
    git remote set-url origin https://github.com/Lifa-Mbangata/Online-Couse-Application.git
)
echo DONE
echo.

REM Push to GitHub
echo [6/6] Pushing to GitHub...
git branch -M main
git push -u origin main
if %errorlevel% neq 0 (
    echo ERROR: Failed to push to GitHub
    echo Please ensure:
    echo   1. You have internet connection
    echo   2. GitHub repository is created and empty
    echo   3. You have push permissions to the repository
    echo.
    pause
    exit /b 1
)
echo DONE
echo.

echo ======================================
echo Git setup completed successfully!
echo ======================================
echo.
echo Your project has been pushed to:
echo https://github.com/Lifa-Mbangata/Online-Couse-Application
echo.
echo File URLs for submission:
echo   models.py: https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/models.py
echo   admin.py: https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/admin.py
echo   course_details_bootstrap.html: https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/templates/course_details_bootstrap.html
echo   views.py: https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/views.py
echo   urls.py: https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/urls.py
echo.
pause
