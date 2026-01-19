from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Course, Lesson, Question, Submission
import json


@login_required
def course_details(request, course_id):
    """Display course details with all lessons"""
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all()
    context = {
        'course': course,
        'lessons': lessons
    }
    return render(request, 'course_details_bootstrap.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def submit(request, lesson_id):
    """Handle exam submission"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    questions = lesson.questions.filter(is_exam=True)
    
    if request.method == 'POST':
        # Process exam submission
        answers = {}
        score = 0
        total_questions = questions.count()
        
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                try:
                    choice = question.choices.get(id=selected_choice_id)
                    answers[str(question.id)] = {
                        'choice_id': int(selected_choice_id),
                        'choice_text': choice.choice_text,
                        'is_correct': choice.is_correct
                    }
                    if choice.is_correct:
                        score += 1
                except:
                    answers[str(question.id)] = {
                        'choice_id': None,
                        'choice_text': 'No answer',
                        'is_correct': False
                    }
            else:
                answers[str(question.id)] = {
                    'choice_id': None,
                    'choice_text': 'No answer',
                    'is_correct': False
                }
        
        # Calculate percentage
        percentage = (score / total_questions * 100) if total_questions > 0 else 0
        is_passed = percentage >= 70
        
        # Create submission
        submission = Submission.objects.create(
            student=request.user,
            lesson=lesson,
            answers=answers,
            score=score,
            total_questions=total_questions,
            is_passed=is_passed
        )
        
        return redirect('show_exam_result', submission_id=submission.id)
    
    context = {
        'lesson': lesson,
        'questions': questions
    }
    return render(request, 'submit_exam.html', context)


@login_required
def show_exam_result(request, submission_id):
    """Display exam results"""
    submission = get_object_or_404(Submission, id=submission_id, student=request.user)
    
    # Get question details
    questions = submission.lesson.questions.filter(is_exam=True)
    question_results = []
    
    for question in questions:
        question_id = str(question.id)
        if question_id in submission.answers:
            answer_data = submission.answers[question_id]
            question_results.append({
                'question': question,
                'answer': answer_data,
                'choices': question.choices.all()
            })
    
    percentage = (submission.score / submission.total_questions * 100) if submission.total_questions > 0 else 0
    
    context = {
        'submission': submission,
        'question_results': question_results,
        'percentage': percentage,
        'lesson': submission.lesson
    }
    return render(request, 'exam_result.html', context)


def index(request):
    """Display all courses"""
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'index.html', context)
