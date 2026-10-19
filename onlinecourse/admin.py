from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission, Enrollment, Instructor, Learner

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date', 'total_enrollment')
    search_fields = ['name', 'description']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'course', 'grade')
    search_fields = ['question_text']

# Đăng ký đầy đủ các model vào Django Admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Learner)