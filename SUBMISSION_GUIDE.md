# Online Course Application - Assignment Submission Guide

## Project Overview

A complete Django-based Online Course Application with exam features has been created. The project is located at:
```
c:\Users\Lifa.Mbangata\Downloads\Python App\onlinecourse
```

## How to Deploy to GitHub

Since Git is not installed on your system, follow these steps to push the project to GitHub:

1. **Install Git** from https://git-scm.com/download/win
2. **Open PowerShell/Command Prompt** and navigate to the project:
   ```
   cd "c:\Users\Lifa.Mbangata\Downloads\Python App\onlinecourse"
   ```

3. **Initialize git and configure user**:
   ```
   git init
   git config user.email "your-email@example.com"
   git config user.name "Your Name"
   ```

4. **Add all files**:
   ```
   git add .
   ```

5. **Commit files**:
   ```
   git commit -m "Initial commit: Complete Online Course Application with exam features"
   ```

6. **Add remote repository**:
   ```
   git remote add origin https://github.com/Lifa-Mbangata/Online-Couse-Application.git
   ```

7. **Push to GitHub**:
   ```
   git branch -M main
   git push -u origin main
   ```

## Project Structure

```
onlinecourse/
├── manage.py                           # Django management script
├── requirements.txt                    # Python dependencies
├── README.md                          # Project documentation
├── .gitignore                         # Git ignore file
├── onlinecourse/                      # Project settings directory
│   ├── __init__.py
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # Main URL configuration
│   ├── asgi.py                        # ASGI configuration
│   └── wsgi.py                        # WSGI configuration
└── onlinecourseapp/                   # Main application
    ├── __init__.py
    ├── apps.py                        # App configuration
    ├── models.py                      # Models: Course, Lesson, Question, Choice, Submission
    ├── admin.py                       # Admin configuration with inlines
    ├── views.py                       # Views: submit and show_exam_result
    ├── urls.py                        # App URL routing
    ├── tests.py                       # Tests
    └── templates/                     # HTML templates
        ├── index.html
        ├── course_details_bootstrap.html
        ├── submit_exam.html
        └── exam_result.html
```

## Task Completion Guide

### Task 1: Submit models.py URL
After pushing to GitHub, the URL will be:
```
https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/models.py
```

**Contains**: Question, Choice, Submission models (plus Course and Lesson)

### Task 2: Submit admin.py URL
```
https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/admin.py
```

**Contains**: 
- Imported classes: admin, Course, Lesson, Question, Choice, Submission (7 imports)
- QuestionInline
- ChoiceInline
- LessonInline
- QuestionAdmin
- LessonAdmin
- CourseAdmin
- SubmissionAdmin

### Task 3: Admin Site Screenshot (03-admin-site)
After running the application, take a screenshot of:
1. Go to http://localhost:8000/admin/
2. Log in with superuser credentials
3. Capture the page showing:
   - Authentication and Authorization section
   - OnlineCourse section (with Course, Lesson, Question, Choice, Submission)

**Save as**: `03-admin-site.png`

### Task 4: Submit course_details_bootstrap.html URL
```
https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/templates/course_details_bootstrap.html
```

**Features**:
- Course name and description display
- Lists all related lessons using Django template tags
- Bootstrap 5 styling
- Links to take exams
- Shows question count per lesson

### Task 5: Submit views.py URL
```
https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/views.py
```

**Contains**:
- `submit()` function: Handles exam submission and answer processing
- `show_exam_result()` function: Displays exam results with scoring
- `course_details()` function: Display course details
- `index()` function: Display available courses

### Task 6: Submit urls.py URL
```
https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/urls.py
```

**Contains**:
- Path for `submit`: `lesson/<int:lesson_id>/submit/`
- Path for `show_exam_result`: `exam-result/<int:submission_id>/`

### Task 7: Final Exam Result Screenshot (07-final)
After running the application and completing an exam:
1. Run: `python manage.py runserver`
2. Create test data (course, lesson, questions, choices)
3. Take exam with 70%+ score
4. Capture the result page showing:
   - "Congratulations!" message
   - Score (e.g., "8/10")
   - Percentage
   - Exam results breakdown

**Save as**: `07-final.png`

## Setting Up Local Development

### Prerequisites
- Python 3.8+
- Django 4.2.0

### Installation Steps

1. **Navigate to project**:
   ```
   cd "c:\Users\Lifa.Mbangata\Downloads\Python App\onlinecourse"
   ```

2. **Create virtual environment**:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```
   python manage.py migrate
   ```

5. **Create superuser**:
   ```
   python manage.py createsuperuser
   ```

6. **Run development server**:
   ```
   python manage.py runserver
   ```

7. **Access application**:
   - Admin: http://localhost:8000/admin/
   - Main: http://localhost:8000/

## Creating Test Data

To create test data in the admin interface:

1. Log in to http://localhost:8000/admin/
2. Click "Courses" → "Add Course"
3. Add a course with name and description
4. Click "Lessons" → "Add Lesson"
5. Add lesson to the course
6. Click "Questions" → "Add Question"
7. Select the lesson and mark as "is_exam"
8. Add question text
9. Click "Choices" → "Add Choice"
10. Add multiple choices, mark the correct one with "is_correct"

## Models Description

### Course
- name: CharField
- description: TextField
- created_at: DateTimeField (auto)

### Lesson
- course: ForeignKey(Course)
- name: CharField
- description: TextField
- content: TextField
- order: IntegerField

### Question
- lesson: ForeignKey(Lesson)
- question_text: TextField
- is_exam: BooleanField
- order: IntegerField

### Choice
- question: ForeignKey(Question)
- choice_text: CharField
- is_correct: BooleanField
- order: IntegerField

### Submission
- student: ForeignKey(User)
- lesson: ForeignKey(Lesson)
- answers: JSONField (stores user answers)
- score: FloatField (number of correct answers)
- total_questions: IntegerField
- is_passed: BooleanField (score >= 70%)
- submitted_at: DateTimeField

## Key Features Implemented

✓ Question, Choice, and Submission models
✓ Admin configuration with custom inlines and admin classes
✓ Course and lesson management
✓ Exam submission with automatic grading
✓ Result evaluation and feedback
✓ Bootstrap-styled templates
✓ Course details display with Django template tags
✓ Responsive design
✓ Result tracking with passing/failing status

## Grading Criteria (15 points total)

- Task 1: models.py URL (3 points)
- Task 2: admin.py URL (3 points)
- Task 3: Admin site screenshot (1 point)
- Task 4: course_details_bootstrap.html URL (2 points)
- Task 5: views.py URL (2 points)
- Task 6: urls.py URL (2 points)
- Task 7: Final exam result screenshot (2 points)

**Required to Pass**: 70% (10.5 points minimum)

---

For any issues, please ensure:
1. Django 4.2.0 is installed
2. All migrations are applied
3. Superuser is created
4. Development server is running on port 8000
