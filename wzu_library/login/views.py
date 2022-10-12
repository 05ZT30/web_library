from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms
# Create your views here.
def login_view(request):
    # if request.method == 'POST':
    login_form = forms.UserForm(request.POST)
    message = '请检查填写的内容！'
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            message = '登录成功！'
            #现在chat登录之后也会跳转到主页，chat自身检查并回到刚才的页面这个url失效
            #是否可以通过弹窗让用户选择是否需要跳转到主页，这样子就可以让chat跳转到源页面了
            return render(request, 'index.html', locals())
        else:
            message = '用户名或密码错误！'
    else:
        return render(requesivt, 'login.html', locals())

    # login_form = forms.UserForm()
    return render(request, 'login.html')

# def register_student(request):
#     if request.session.get('is_login', None):
#         return redirect('/index/')

#     if request.method == 'POST':
#         register_form = forms.UserForm(request.POST)
#         message = "请检查填写的内容！"
#         if register_form.is_valid():
#             username = register_form.cleaned_data.get('username')
#             password1 = register_form.cleaned_data.get('password1')
#             password2 = register_form.cleaned_data.get('password2')

#             if password1 != password2:
#                 message = '两次输入的密码不同！'
#                 return render(request, 'login/register_student.html', locals())
#             else:
#                 same_id_user = models.MyStudentUser.objects.filter(
#                     name=student_id)
#                 if same_id_user:
#                     message = '该用户已经存在'
#                     return render(request, 'login/register_student.html', locals())
#                 same_email_user = models.MyStudentUser.objects.filter(
#                     email=email)
#                 if same_email_user:
#                     message = '该邮箱已经被注册了！'
#                     return render(request, 'login/register_student.html', locals())

#                 new_user = models.MyStudentUser()
#                 new_user.student_id = student_id
#                 new_user.name = username
#                 new_user.password = hash_code(password1)
#                 new_user.email = email
#                 new_user.sex = sex
#                 new_user.save()

#                 return redirect('/login/')
#         else:
#             return render(request, 'login/register_student.html', locals())
#     register_form = forms.UserForm()
#     return render(request, 'login/register_student.html', locals())


def logout_view(request):
    if not request.session.get('is_login', None):
        logout(request)
        return redirect('/index/')
