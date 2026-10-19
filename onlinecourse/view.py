from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Enrollment, Question, Choice, Submission

def submit(request, course_id):
    """Xử lý nộp bài thi (exam submission)"""
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        submission = Submission.objects.create(enrollment=enrollment)
        
        # Lấy danh sách đáp án người dùng chọn
        for key, value in request.POST.lists():
            if key.startswith('choice'):
                for choice_id in value:
                    choice = Choice.objects.get(pk=int(choice_id))
                    submission.choices.add(choice)
                    
        return HttpResponseRedirect(reverse('onlinecourse:exam_result', args=(course.id, submission.id)))
    return redirect('onlinecourse:course_details', course_id=course.id)

def show_exam_result(request, course_id, submission_id):
    """Hiển thị kết quả bài thi"""
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    context = {
        'course': course,
        'submission': submission,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)