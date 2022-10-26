from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm,UserRegisterForm
from django.contrib.auth.models import Group
from .models import UserModel

users_in_manager_group = Group.objects.get(name="Manager").user_set.all()
users_in_teacher_group = Group.objects.get(name="Teacher").user_set.all()
users_in_student_group = Group.objects.get(name="Student").user_set.all()
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                message = '登录成功！'
                if user in users_in_manager_group:
                    return redirect('/admin/')
                if user in users_in_student_group or user in users_in_teacher_group:
                    # 现在chat登录之后也会跳转到主页，chat自身检查并回到刚才的页面这个url失效
                    # 是否可以通过弹窗让用户选择是否需要跳转到主页，这样子就可以让chat跳转到源页面了
                    return render(request, 'index.html', locals())
            else:
                message = '用户名或密码错误！'
        else:
            return render(request, 'login.html', locals())
    else:
        login_form = UserForm()
    return render(request, 'login.html', locals())


def register_view(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            group_select = register_form.cleaned_data.get('group')
            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'register.html', locals())
            else:
                samename_user = UserModel.objects.filter(name=username)
                if samename_user:
                    message = '该用户已经存在'
                    return render(request, 'register.html', locals())
                
                new_user = UserModel()
                new_user.username = username
                new_user.password = hash(password1)
                new_user.save()
                user = UserModel.objects.get(username=username)
                group = Group.objects.get(id= group_select)
                user.groups.add(group)
                return redirect('/login/')
        else:
            return render(request, 'register.html', locals())
    register_form = UserForm()
    return render(request, 'register.html', locals())


def logout_view(request):
    if not request.session.get('is_login', None):
        logout(request)
        return redirect('/index/')
