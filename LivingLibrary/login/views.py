from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm,UserRegisterForm
from django.contrib.auth.models import Group
from login.models import MyUser 

# users_in_manager_group = Group.objects.get(name="Manager").user_set.all()
# users_in_teacher_group = Group.objects.get(name="Teacher").user_set.all()
# users_in_student_group = Group.objects.get(name="Student").user_set.all()
# Create your views here.


def login_view(request):
    if request.session.get('is_login',None):
       return render(request, 'index.html', locals())
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = MyUser.objects.get(username=username)
            except :
                message = '用户不存在！'
                return render(request, 'login.html', locals())

            if user.check_password(password):
                #TODO 增加密码加密
                request.session['is_login'] = True
                request.session['username'] = username
                login(request,user)
                return render(request, 'index.html', locals())
            else:
                message = '密码不正确！'
                return render(request, 'login.html', locals())
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
                samename_user = User.objects.filter(username=username)
                if samename_user:
                    message = '该用户已经存在'
                    return render(request, 'register.html', locals())
                
                try:
                    group = Group.objects.get(name = group_select)
                except:
                    Group.objects.create(name = group_select)
                    group = Group.objects.get(name = group_select)
                    
                new_user = MyUser()
                new_user.username = username
                new_user.password = hash(password1)
                # new_user.group = group
                new_user.save()
                user = MyUser.objects.get(username=username)
                group.user_set.add(user)
                return redirect('/login/')
        else:
            return render(request, 'register.html', locals())
    register_form = UserRegisterForm ()
    return render(request, 'register.html', locals())


def logout_view(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    logout(request)
    return redirect("/login/")