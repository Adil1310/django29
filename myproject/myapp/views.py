from django.shortcuts import render
from .models import Student, Course

# Create your views here.

def student_course_list(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'students': students, 'courses': courses})