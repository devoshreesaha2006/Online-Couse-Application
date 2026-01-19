# Assignment Submission Checklist

## Pre-Submission Tasks

### Step 1: Install Git (if not already installed)
- [ ] Download Git from https://git-scm.com/download/win
- [ ] Install Git with default settings
- [ ] Restart your computer or terminal

### Step 2: Set up Django Application
- [ ] Open Command Prompt or PowerShell
- [ ] Navigate to: `c:\Users\Lifa.Mbangata\Downloads\Python App\onlinecourse`
- [ ] Run: `setup.bat` (double-click the file)
- [ ] Wait for setup to complete
- [ ] Enter superuser credentials when prompted

### Step 3: Create Test Data
- [ ] Run: `python manage.py runserver` (from the project directory with venv activated)
- [ ] Open browser and go to: http://localhost:8000/admin/
- [ ] Log in with superuser credentials
- [ ] Create a Course:
  - [ ] Click "Add Course"
  - [ ] Name: "Python Programming" or similar
  - [ ] Description: "Learn Python basics"
  - [ ] Save
  
- [ ] Create a Lesson:
  - [ ] Click "Lessons" then "Add Lesson"
  - [ ] Select the course
  - [ ] Name: "Functions" or similar
  - [ ] Description: "Understanding functions"
  - [ ] Content: "Functions are reusable blocks of code..."
  - [ ] Order: 1
  - [ ] Save
  
- [ ] Create Questions (at least 10 for good score):
  - [ ] Click "Questions" then "Add Question"
  - [ ] Lesson: Select the course lesson
  - [ ] Question Text: "What is a function?"
  - [ ] Is Exam: ✓ (CHECK THIS!)
  - [ ] Order: 1
  - [ ] Save
  
- [ ] Create Choices for each question:
  - [ ] Click on the question to edit
  - [ ] Scroll to "Choices" section
  - [ ] Add multiple choices:
     - [ ] Choice 1: "A reusable block of code" (Mark is_correct: ✓)
     - [ ] Choice 2: "A variable"
     - [ ] Choice 3: "A loop"
     - [ ] Choice 4: "A data type"
  - [ ] Save
  
- [ ] Repeat: Create at least 10 questions with choices to ensure 70%+ passing score

### Step 4: Test the Application
- [ ] Go to http://localhost:8000/
- [ ] Click on your course
- [ ] Verify course details display correctly with:
  - [ ] Course name
  - [ ] Course description
  - [ ] List of lessons with descriptions
  - [ ] "Take Exam" button for lessons
  
- [ ] Click "Take Exam"
- [ ] Verify exam page shows:
  - [ ] All questions
  - [ ] All choices for each question
  - [ ] Question counter
  
- [ ] Answer at least 7 out of 10 questions correctly (70% minimum)
- [ ] Click "Submit Exam"

## Screenshot Capture Tasks

### Task 3: Admin Site Screenshot (03-admin-site.png)
- [ ] Keep your browser on http://localhost:8000/admin/
- [ ] Ensure you can see both:
  - [ ] "Authentication and Authorization" section
  - [ ] "OnlineCourse" section (with Course, Lesson, Question, Choice, Submission)
- [ ] Press Print Screen or use Snipping Tool
- [ ] Save as: `03-admin-site.png`
- [ ] Location: `c:\Users\Lifa.Mbangata\Downloads\Python App\onlinecourse\`

### Task 7: Final Exam Result Screenshot (07-final.png)
- [ ] Complete the exam (with 70%+ correct answers)
- [ ] You should see the results page with:
  - [ ] "Congratulations!" message
  - [ ] Score (e.g., "8/10")
  - [ ] Percentage (e.g., "80%")
  - [ ] "You have passed the exam!"
  - [ ] Review of answers with correct/incorrect indicators
- [ ] Press Print Screen or use Snipping Tool
- [ ] Save as: `07-final.png`
- [ ] Location: `c:\Users\Lifa.Mbangata\Downloads\Python App\onlinecourse\`

## GitHub Submission Tasks

### Step 5: Push to GitHub
- [ ] Run: `push-to-github.bat` (double-click the file)
- [ ] Wait for script to complete successfully
- [ ] Verify files appear on: https://github.com/Lifa-Mbangata/Online-Couse-Application

## Assignment Submission Tasks

### Task 1: Submit models.py GitHub URL (3 points)
- [ ] Copy URL: `https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/models.py`
- [ ] Verify page contains:
  - [ ] `class Question`
  - [ ] `class Choice`
  - [ ] `class Submission`
  - [ ] Correct model fields and relationships
- [ ] Submit URL to assignment

### Task 2: Submit admin.py GitHub URL (3 points)
- [ ] Copy URL: `https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/admin.py`
- [ ] Verify page contains:
  - [ ] 7 imported classes (admin + 5 models + ...)
  - [ ] `class QuestionInline`
  - [ ] `class ChoiceInline`
  - [ ] `class QuestionAdmin`
  - [ ] `class LessonAdmin`
- [ ] Submit URL to assignment

### Task 3: Submit Admin Site Screenshot (1 point)
- [ ] Have `03-admin-site.png` ready
- [ ] Upload screenshot to assignment
- [ ] Ensure screenshot clearly shows:
  - [ ] "Authentication and Authorization" section
  - [ ] "OnlineCourse" section with all models

### Task 4: Submit course_details_bootstrap.html GitHub URL (2 points)
- [ ] Copy URL: `https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/templates/course_details_bootstrap.html`
- [ ] Verify page contains:
  - [ ] Bootstrap CDN link
  - [ ] Course name display
  - [ ] Course description display
  - [ ] Django template tags (`{% for %}`, `{{ }}`)
  - [ ] List of lessons
  - [ ] "Take Exam" links
  - [ ] Bootstrap styling (navbar, cards, buttons, etc.)
- [ ] Submit URL to assignment

### Task 5: Submit views.py GitHub URL (2 points)
- [ ] Copy URL: `https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/views.py`
- [ ] Verify page contains:
  - [ ] `def submit(request, lesson_id)` function
  - [ ] `def show_exam_result(request, submission_id)` function
  - [ ] Correct imports
  - [ ] Answer processing logic
  - [ ] Score calculation
- [ ] Submit URL to assignment

### Task 6: Submit urls.py GitHub URL (2 points)
- [ ] Copy URL: `https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/urls.py`
- [ ] Verify page contains:
  - [ ] Path for `submit` view
  - [ ] Path for `show_exam_result` view
  - [ ] Correct URL patterns with parameters
- [ ] Submit URL to assignment

### Task 7: Submit Final Exam Result Screenshot (2 points)
- [ ] Have `07-final.png` ready
- [ ] Upload screenshot to assignment
- [ ] Ensure screenshot clearly shows:
  - [ ] "Congratulations!" message
  - [ ] Score display (e.g., "8/10")
  - [ ] Percentage (e.g., "80%")
  - [ ] "You have passed the exam!" message
  - [ ] Answer review section
- [ ] Screenshot must show a passing result (70%+ score)

## Final Submission

- [ ] All 7 tasks completed
- [ ] All URLs are valid and point to correct files
- [ ] Both screenshots are uploaded
- [ ] Click "Submit assignment" button
- [ ] Review feedback from AI evaluator
- [ ] Expected score: 15 points (100%)

## Quick Reference Commands

```powershell
# Start development server
cd "c:\Users\Lifa.Mbangata\Downloads\Python App\onlinecourse"
venv\Scripts\activate
python manage.py runserver

# Create superuser (if needed)
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Shell access (for testing)
python manage.py shell
```

## Troubleshooting

**Issue**: "Git is not installed"
- **Solution**: Download and install from https://git-scm.com/download/win

**Issue**: "Python is not installed"
- **Solution**: Download and install from https://www.python.org/downloads/

**Issue**: "Command not found: venv"
- **Solution**: Run: `python -m venv venv`

**Issue**: Database errors
- **Solution**: Run: `python manage.py migrate`

**Issue**: Port 8000 already in use
- **Solution**: Run: `python manage.py runserver 8001`

**Issue**: Can't log in to admin
- **Solution**: Run: `python manage.py createsuperuser`

---

**Good luck with your submission! You're required to score 70% (10.5 points) to pass.**
