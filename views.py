from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Enrollment, Question, Choice, Submission

def submit(request, course_id):
    """Xử lý nộp bài thi (exam submission) và tính điểm cho học viên."""
    course = get_object_or_404(Course, pk=course_id)
    
    # Kiểm tra xem người dùng đã đăng nhập và có đăng ký khóa học chưa
    if request.method == 'POST':
        # Lấy thông tin enrollment của user hiện tại với khóa học này
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        
        # Tạo mới một đối tượng Submission
        submission = Submission.objects.create(enrollment=enrollment)
        
        # Lấy danh sách các lựa chọn (choices) mà người dùng đã chọn từ form POST
        # Các checkbox hoặc radio trong form thường được đặt tên dạng choice_<question_id> hoặc lấy qua request.POST.getlist
        choosed_ids = []
        for key, value in request.POST.lists():
            if key.startswith('choice'):
                for choice_id in value:
                    choosed_ids.append(int(choice_id))
                    
        # Thêm các choice đã chọn vào submission thông qua mối quan hệ ManyToMany
        for choice_id in choosed_ids:
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)
            
        # Điều hướng sang trang xem kết quả thi sau khi lưu thành công
        return HttpResponseRedirect(reverse('onlinecourse:exam_result', args=(course.id, submission.id)))
    
    return redirect('onlinecourse:course_details', course_id=course.id)


def show_exam_result(request, course_id, submission_id):
    """Hiển thị kết quả bài thi của học viên (điểm số, câu đúng/sai)."""
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Tính toán điểm số dựa trên các câu trả lời đúng của học viên
    score = 0
    total_score = 0
    
    # Lấy tất cả các câu hỏi thuộc các lesson của khóa học này (hoặc cấu trúc bài kiểm tra của bạn)
    # Tùy theo cách bạn định nghĩa quan hệ giữa Course -> Lesson -> Question
    
    context = {
        'course': course,
        'submission': submission,
        'score': score,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
