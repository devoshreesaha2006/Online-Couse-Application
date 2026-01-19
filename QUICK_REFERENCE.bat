@echo off
title Online Course Application - Quick Commands
cls
echo.
echo ========================================
echo    ONLINE COURSE APP - QUICK REFERENCE
echo ========================================
echo.
echo STEP 1 - Initial Setup (Run once)
echo   Double-click: setup.bat
echo   OR manually:
echo     python -m venv venv
echo     venv\Scripts\activate
echo     pip install -r requirements.txt
echo     python manage.py migrate
echo     python manage.py createsuperuser
echo.
echo STEP 2 - Start Development Server
echo   venv\Scripts\activate
echo   python manage.py runserver
echo   Then open: http://localhost:8000/
echo.
echo STEP 3 - Access Admin (create test data)
echo   URL: http://localhost:8000/admin/
echo   Create: Course ^> Lesson ^> Questions ^> Choices
echo   (Create at least 10 questions for good results)
echo.
echo STEP 4 - Test the Exam
echo   Go to: http://localhost:8000/
echo   Select course
echo   Take exam (must get 70%+ to pass)
echo   Screenshots:
echo     - After logging into admin (Task 3)
echo     - After passing exam (Task 7)
echo.
echo STEP 5 - Push to GitHub (Run once)
echo   Double-click: push-to-github.bat
echo   OR manually:
echo     git init
echo     git config user.email "your-email@example.com"
echo     git config user.name "Your Name"
echo     git add .
echo     git commit -m "Initial commit"
echo     git remote add origin https://github.com/Lifa-Mbangata/Online-Couse-Application.git
echo     git branch -M main
echo     git push -u origin main
echo.
echo STEP 6 - Submit Assignment
echo   Task 1: models.py URL
echo   Task 2: admin.py URL
echo   Task 3: 03-admin-site.png screenshot
echo   Task 4: course_details_bootstrap.html URL
echo   Task 5: views.py URL
echo   Task 6: urls.py URL
echo   Task 7: 07-final.png screenshot
echo.
echo ========================================
echo    USEFUL COMMANDS
echo ========================================
echo.
echo Activate venv:         venv\Scripts\activate
echo Deactivate venv:       deactivate
echo Run server:            python manage.py runserver
echo Create superuser:      python manage.py createsuperuser
echo Run migrations:        python manage.py migrate
echo Django shell:          python manage.py shell
echo Collect static files:  python manage.py collectstatic
echo.
echo ========================================
echo    TROUBLESHOOTING
echo ========================================
echo.
echo Port 8000 in use?      python manage.py runserver 8001
echo Database error?        python manage.py migrate
echo Can't login admin?     python manage.py createsuperuser
echo Can't find Python?     Install from python.org
echo Can't find Git?        Install from git-scm.com
echo.
echo ========================================
echo    DOCUMENTATION
echo ========================================
echo.
echo Read these files:
echo   - 00-START-HERE.md
echo   - SUBMISSION_CHECKLIST.md
echo   - SUBMISSION_GUIDE.md
echo.
pause
