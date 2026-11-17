from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission
from .models import Enrollment


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ('question_text', 'is_exam', 'grade', 'order')


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    fields = ('choice_text', 'is_correct', 'order')


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ('name', 'order')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'lesson', 'grade', 'is_exam', 'order')
    list_filter = ('is_exam', 'lesson')
    search_fields = ('question_text', 'content')
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('name',)
    inlines = [QuestionInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    inlines = [LessonInline]


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'score', 'is_passed', 'submitted_at')
    list_filter = ('is_passed', 'submitted_at')
    readonly_fields = ('student', 'lesson', 'answers', 'score', 'submitted_at')


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Enrollment)
