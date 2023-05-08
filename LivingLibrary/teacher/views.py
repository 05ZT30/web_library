from django.shortcuts import render
from login.models import MyUser
from django.core.paginator import Paginator
from django.conf import settings
from django.utils.safestring import mark_safe

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

    # 数据总条数
    total_count = MyUser.objects.filter(is_teacher=True).count()
    #总页码
    total_page_count, div = divmod(total_count,page_szie)
    if div:
        total_page_count += 1
    page_str_list=[]
    #上页
    if page >1:
        prev='<li><a href="?page={}">上一页</a></li>'.format(page - 1)
    else:
        prev='<li><a href="?page={}">上一页</a></li>'.format(1)
    page_str_list.append(prev)

    for i in range(1,total_page_count + 1):

        if i==page:
            ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i,i)
        else:
            ele = '<li><a href="?page={}">{}</a></li>'.format(i,i)
        page_str_list.append(ele)
    

    #下页
    if page < total_page_count:
        prev='<li><a href="?page={}">下一页</a></li>'.format(page + 1)
    else:
        prev='<li><a href="?page={}">下一页</a></li>'.format(total_page_count)
    page_str_list.append(prev)

    
    page_string = mark_safe("".join(page_str_list))

    return render(request, 'teacher.html', {"teachers":teachers,"page_string":page_string})


def teacher_view(request, category='all'):
    if category == 'all':
        teachers = MyUser.objects.filter(is_teacher=True)
    else:
        teachers = MyUser.objects.filter(is_teacher=True, subject=category)
    return render(request, 'teacher.html', {'teachers': teachers, 'category': category})
