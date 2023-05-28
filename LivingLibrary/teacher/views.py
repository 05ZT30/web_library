from django.shortcuts import render
from login.models import MyUser
from django.core.paginator import Paginator
from django.conf import settings
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):

    subject= request.GET.get('category','all')
    q_name = request.GET.get("q", "")

    if subject == 'all':
        if q_name:
            teachers = MyUser.objects.filter(is_teacher=True,username__icontains=q_name)  # 获取所有教师对象
        else:
            teachers = MyUser.objects.filter(is_teacher=True)  # 获取所有教师对象
        page = int(request.GET.get('page',1))
        page_szie = 20
        start = (page -1)* page_szie
        end =page *page_szie
        if q_name:
            teachers = MyUser.objects.filter(is_teacher=True,username__icontains=q_name)[start:end]
        else:
            teachers = MyUser.objects.filter(is_teacher=True)[start:end]
        # print('BASE_DIR:', settings.BASE_DIR)
        # print('TEMPLATES:', settings.TEMPLATES)

        # 数据总条数
        if q_name:
            total_count = MyUser.objects.filter(is_teacher=True,username__icontains=q_name).count()
        else:
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

    else:
        if q_name:
            teachers = MyUser.objects.filter(is_teacher=True,category=subject,username__icontains=q_name)
        else:
            teachers = MyUser.objects.filter(is_teacher=True, category=subject)
        page = int(request.GET.get('page',1))
        page_szie = 20
        start = (page -1)* page_szie
        end =page *page_szie
        if q_name:
            teachers = MyUser.objects.filter(is_teacher=True,category=subject,username__icontains=q_name)[start:end]
        else:
            teachers = MyUser.objects.filter(is_teacher=True, category=subject)[start:end]
        # print('BASE_DIR:', settings.BASE_DIR)
        # print('TEMPLATES:', settings.TEMPLATES)

        # 数据总条数
        total_count = MyUser.objects.filter(is_teacher=True,category=subject,username__icontains=q_name).count()
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

    
   
    print(teachers)
    return render(request, 'teacher.html', {"teachers":teachers,"page_string":page_string,"q_name":q_name})



def teacherDetail(request):
    card_id = request.GET.get('card_id', 0)
    print("card_id",card_id)
    teacher = MyUser.objects.filter(card_id=card_id)
    print("学工号",teacher[0].card_id)
    print('用户名',teacher[0].username)
    print('邮箱',teacher[0].email)
    print('出生日期',teacher[0].date_of_birth)
    print('电话号码',teacher[0].category)
    print('专业领域',teacher[0].phone)
    print('照片',teacher[0].photo)
    print('简介',teacher[0].introduction)
    print('是否在线',teacher[0].is_active)
    print('是否为管理员',teacher[0].is_admin)
    print('是否能管理数据',teacher[0].is_superuser)
    print("是否老师",teacher[0].is_teacher)
    return render(request, 'teacherDetail.html',{"teacher":teacher[0]})