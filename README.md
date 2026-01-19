# 🎓 Online Course Application

A complete Django-based Online Course Application with exam features, built for assignment submission.

**Location**: `C:\Users\Lifa.Mbangata\Downloads\Python App\onlinecourse`

## ✨ Features

✅ Create and manage courses and lessons
✅ Add questions and choices for exams
✅ Submit exam answers with validation
✅ Automatic exam grading (70% pass threshold)
✅ Result evaluation with detailed scoring
✅ Admin interface with custom inlines
✅ Bootstrap-styled responsive templates
✅ Django template tags and inheritance
✅ User authentication and authorization
✅ Answer review and feedback

## 📚 Models

- **Course**: Main course container with description
- **Lesson**: Individual lessons within courses
- **Question**: Exam questions with metadata (is_exam flag)
- **Choice**: Multiple choice options with correct answer indicator
- **Submission**: Student exam submissions with scores and answers

## 🚀 Quick Start

### Automated Setup
```bash
# Double-click: setup.bat
```

### Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## 📖 Usage

1. **Admin Interface**: http://localhost:8000/admin/
   - Create courses and lessons
   - Add questions and choices
   - Manage submissions

2. **Student Interface**: http://localhost:8000/
   - View available courses
   - Take exams
   - View results

## 📋 Assignment Tasks

| Task | File | Type | Points |
|------|------|------|--------|
| 1 | models.py | GitHub URL | 3 |
| 2 | admin.py | GitHub URL | 3 |
| 3 | 03-admin-site.png | Screenshot | 1 |
| 4 | course_details_bootstrap.html | GitHub URL | 2 |
| 5 | views.py | GitHub URL | 2 |
| 6 | urls.py | GitHub URL | 2 |
| 7 | 07-final.png | Screenshot | 2 |

## 📁 File Structure

### Core Files (For Submission)
- `onlinecourseapp/models.py` - Question, Choice, Submission models
- `onlinecourseapp/admin.py` - Admin configuration with inlines
- `onlinecourseapp/views.py` - submit() and show_exam_result() functions
- `onlinecourseapp/urls.py` - URL routes for exam functions
- `onlinecourseapp/templates/course_details_bootstrap.html` - Bootstrap template

### Configuration Files
- `onlinecourse/settings.py` - Django configuration
- `onlinecourse/urls.py` - Main URL configuration
- `manage.py` - Django management CLI
- `requirements.txt` - Python dependencies

### Helper Files
- `setup.bat` - Automated setup script
- `push-to-github.bat` - Automated GitHub push
- `00-START-HERE.md` - Quick start guide
- `SUBMISSION_CHECKLIST.md` - Step-by-step instructions
- `SUBMISSION_GUIDE.md` - Detailed guide

## 🔑 Key Components

### Models (Task 1)
```python
Question(lesson, question_text, is_exam, order)
Choice(question, choice_text, is_correct, order)
Submission(student, lesson, answers, score, total_questions, is_passed)
```

### Admin (Task 2)
- QuestionInline - Inline question editing
- ChoiceInline - Inline choice editing
- QuestionAdmin - Question admin with filters
- LessonAdmin - Lesson admin with inlines

### Views (Task 5)
- `submit()` - Process exam submissions
- `show_exam_result()` - Display results

### URLs (Task 6)
- `/lesson/<id>/submit/` - Exam submission
- `/exam-result/<id>/` - Exam results

### Template (Task 4)
- `course_details_bootstrap.html` - Bootstrap-styled course view

## 📸 Screenshots for Assignment

### Task 3: Admin Site (03-admin-site.png)
- Shows admin interface with Authentication and OnlineCourse sections
- Location: Root project directory

### Task 7: Final Result (07-final.png)
- Shows exam results with "Congratulations" message
- Must have 70%+ score
- Location: Root project directory

## 🎯 Assignment Submission URLs

After pushing to GitHub:

1. **models.py**: `https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/models.py`
2. **admin.py**: `https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/admin.py`
3. **course_details_bootstrap.html**: `https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/templates/course_details_bootstrap.html`
4. **views.py**: `https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/views.py`
5. **urls.py**: `https://github.com/Lifa-Mbangata/Online-Couse-Application/blob/main/onlinecourse/onlinecourseapp/urls.py`

## 🔧 Database Commands

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Access shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8000 in use | `python manage.py runserver 8001` |
| Database error | `python manage.py migrate` |
| Can't login | `python manage.py createsuperuser` |
| Python not found | Install from python.org |
| Git not found | Install from git-scm.com |

## 📊 Grading Criteria

- **Pass**: 70% (10.5 points minimum)
- **Expected**: 100% (15 points)
- **All files ready**: ✅ Yes
- **Screenshots needed**: 2 (tasks 3 & 7)

## 📞 Documentation

Read these files for detailed instructions:
- `00-START-HERE.md` - Quick start guide
- `SUBMISSION_CHECKLIST.md` - Step-by-step instructions
- `SUBMISSION_GUIDE.md` - Detailed setup guide
- `COMPLETE_SUMMARY.md` - Full project overview

## ⏱️ Setup Time

- Initial setup: 5 minutes
- Create test data: 10 minutes
- Take exam: 5 minutes
- Capture screenshots: 5 minutes
- Push to GitHub: 2 minutes
- Submit assignment: 3 minutes

**Total: ~30 minutes**

## ✅ Checklist

- [x] All models created (Question, Choice, Submission)
- [x] Admin configuration complete (QuestionInline, ChoiceInline, etc.)
- [x] Views implemented (submit, show_exam_result)
- [x] URLs configured properly
- [x] Templates created with Bootstrap
- [x] Automatic grading system
- [x] Result display with feedback
- [x] Setup scripts created
- [x] Documentation complete
- [ ] Screenshots captured (pending)
- [ ] Pushed to GitHub (pending)

## 🎓 Ready for Submission

All code is complete and tested. Follow the SUBMISSION_CHECKLIST.md to:
1. Set up the application
2. Create test data
3. Capture required screenshots
4. Push to GitHub
5. Submit assignment

**Expected Grade: 100%**
