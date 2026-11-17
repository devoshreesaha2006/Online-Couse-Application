from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from .models import Course, Lesson, Question, Choice, Enrollment, Submission


def index(request):
    return render(request, 'index.html', {'courses': Course.objects.all()})


@login_required
def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_details_bootstrap.html', {
        'course': course,
        'lessons': course.lessons.all(),
    })


@login_required
@require_http_methods(['GET', 'POST'])
def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = Question.objects.filter(lesson__course=course, is_exam=True).select_related('lesson').prefetch_related('choices')
    if request.method == 'GET':
        first_lesson = course.lessons.first()
        return render(request, 'submit_exam.html', {
            'course': course, 'lesson': first_lesson, 'questions': questions,
        })

    enrollment, _ = Enrollment.objects.get_or_create(user=request.user, course=course, defaults={'mode': Enrollment.HONOR})
    first_lesson = course.lessons.first()
    submission = Submission.objects.create(
        enrollment=enrollment,
        student=request.user,
        lesson=first_lesson,
        total_questions=questions.count(),
    )

    selected_choices = []
    answers = {}
    correct_count = 0
    for question in questions:
        selected_id = request.POST.get(f'question_{question.id}')
        choice = question.choices.filter(id=selected_id).first() if selected_id else None
        if choice:
            selected_choices.append(choice)
            is_correct = choice.is_correct
            answers[str(question.id)] = {
                'choice_id': choice.id,
                'choice_text': choice.choice_text,
                'is_correct': is_correct,
            }
            if is_correct:
                correct_count += 1
        else:
            answers[str(question.id)] = {
                'choice_id': None, 'choice_text': 'No answer', 'is_correct': False,
            }

    submission.choices.set(selected_choices)
    percentage = (correct_count / questions.count() * 100) if questions.exists() else 0
    submission.answers = answers
    submission.score = correct_count
    submission.is_passed = percentage >= 70
    submission.save()
    return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)


@login_required
def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, id=course_id)
    submission = get_object_or_404(
        Submission, id=submission_id, enrollment__user=request.user, enrollment__course=course
    )
    questions = Question.objects.filter(lesson__course=course, is_exam=True).select_related('lesson').prefetch_related('choices')
    question_results = []
    for question in questions:
        answer = submission.answers.get(str(question.id), {
            'choice_text': 'No answer', 'is_correct': False,
        })
        question_results.append({
            'question': question,
            'answer': answer,
            'choices': question.choices.all(),
        })
    percentage = (submission.score / submission.total_questions * 100) if submission.total_questions else 0
    return render(request, 'exam_result.html', {
        'course': course,
        'submission': submission,
        'question_results': question_results,
        'percentage': percentage,
        'lesson': submission.lesson,
    })
