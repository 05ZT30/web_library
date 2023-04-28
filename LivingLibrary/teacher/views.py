from django.shortcuts import render
from login.models import MyUser

# Create your views here.
def index(request):
#      return render(request, 'teacher.html', locals())

# def teacher_view(request):
    teachers = MyUser.objects.filter(is_teacher=True)
    return render(request, 'teacher.html', {'teachers': teachers})
