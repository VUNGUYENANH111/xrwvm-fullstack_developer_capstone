from django.db import models
from django.utils.timezone import now

# Giả sử mô hình Lesson đã tồn tại trong dự án của bạn từ các bài trước.
# Nếu dự án của bạn đặt tên mô hình bài học khác, bạn có thể điều chỉnh cho phù hợp.

class Question(models.Model):
    # Khóa ngoại liên kết câu hỏi với bài học (Lesson)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=50)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # Khóa ngoại liên kết đáp án với câu hỏi (Question)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class Submission(models.Model):
    # Lưu trữ các lựa chọn của học viên cho bài kiểm tra
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    
    def __str__(self):
        return f"Submission {self.id}"
