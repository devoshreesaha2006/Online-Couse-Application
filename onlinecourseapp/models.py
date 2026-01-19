from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    is_exam = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text[:50]

    class Meta:
        ordering = ['order']


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        ordering = ['order']


class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='submissions')
    answers = models.JSONField(default=dict)
    score = models.FloatField(default=0)
    total_questions = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_passed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.lesson.name}"

    class Meta:
        ordering = ['-submitted_at']
