from django.shortcuts import render
from login.models import MyUser
from django.core.paginator import Paginator
from django.conf import settings

# Create your views here.
def index(request):
#      return render(request, 'teacher.html', locals())
    teachers = MyUser.objects.filter(is_teacher=True)
# def teacher_view(request):
    page = int(request.GET.get('page',1))
    page_szie = 20
    start = (page -1)* page_szie
    end =page *page_szie
    teachers = MyUser.objects.filter(is_teacher=True)[start:end]
    # print('BASE_DIR:', settings.BASE_DIR)
    # print('TEMPLATES:', settings.TEMPLATES)
    return render(request, 'teacher.html', {"teachers":teachers})


def teacher_view(request, category='all'):
    if category == 'all':
        teachers = MyUser.objects.filter(is_teacher=True)
    else:
        teachers = MyUser.objects.filter(is_teacher=True, subject=category)
    return render(request, 'teacher.html', {'teachers': teachers, 'category': category})
