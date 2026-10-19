from django.contrib import admin
# Import 7 lớp/models từ file models.py của ứng dụng
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Định nghĩa ChoiceInline cho phép thêm Choice trực tiếp trong Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Định nghĩa QuestionInline cho phép thêm Question trực tiếp trong Lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

# Tùy chỉnh giao diện hiển thị cho Question trong Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'lesson', 'grade']

# Tùy chỉnh giao diện hiển thị cho Lesson trong Admin, tích hợp QuestionInline
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'course']

# Đăng ký các models và các lớp admin tương ứng
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
