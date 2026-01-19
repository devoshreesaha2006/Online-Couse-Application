from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ['question_text', 'is_exam', 'order']


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fields = ['choice_text', 'is_correct', 'order']


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ['name', 'order']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'lesson', 'is_exam', 'order']
    list_filter = ['is_exam', 'lesson']
    search_fields = ['question_text']
    inlines = [ChoiceInline]
    fieldsets = (
        ('Question Details', {
            'fields': ('lesson', 'question_text', 'is_exam', 'order')
        }),
    )


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'order']
    list_filter = ['course']
    search_fields = ['name']
    inlines = [QuestionInline]
    fieldsets = (
        ('Lesson Information', {
            'fields': ('course', 'name', 'description', 'order')
        }),
        ('Content', {
            'fields': ('content',),
            'classes': ('collapse',)
        }),
    )


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    inlines = [LessonInline]
    fieldsets = (
        ('Course Information', {
            'fields': ('name', 'description')
        }),
    )


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['student', 'lesson', 'score', 'is_passed', 'submitted_at']
    list_filter = ['is_passed', 'submitted_at', 'lesson']
    search_fields = ['student__username']
    readonly_fields = ['student', 'lesson', 'answers', 'score', 'submitted_at']


# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, admin.ModelAdmin)
admin.site.register(Submission, SubmissionAdmin)
