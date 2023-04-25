from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserRegisterForm
from login.models import MyUser
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    def form_valid(self, form):
        # username = form.cleaned_data.get('username')
        card_id = form.cleaned_data.get('card_id')
        password = form.cleaned_data.get('password')
        user = MyUser.objects.get(card_id= card_id)
        # user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            if user.is_staff:
                return redirect('/admin/')
            else:
                return redirect('/')
        else:
            return self.form_invalid(form)


def login_view(request):
    if request.session.get('is_login', None):
        return render(request, 'index.html', locals())
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            card_id = login_form.cleaned_data.get('card_id')
            password = login_form.cleaned_data.get('password')

            try:
                user = MyUser.objects.get(card_id=card_id)
            except:
                message = '用户不存在！'
                return render(request, 'login.html', locals())
            username = user.username
            if user.check_password(password):
                # TODO 增加密码加密
                request.session['is_login'] = True
                request.session['username'] = username
                login(request, user)
                request.session.modified = True
                if user.is_admin :
                    return redirect('/admin/')
                else:
                    return redirect('/index/')
                # return render(request, 'index.html', locals())
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
            card_id = register_form.cleaned_data.get('card_id')
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            # group_select = register_form.cleaned_data.get('group')
            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'register.html', locals())
            else:
                samename_user = MyUser.objects.filter(username=username)
                if samename_user:
                    message = '该用户已经存在'
                    return render(request, 'register.html', locals())

                # try:
                #     group = Group.objects.get(name = group_select)
                # except:
                #     Group.objects.create(name = group_select)
                #     group = Group.objects.get(name = group_select)

                new_user = MyUser.objects.create_user(
                    card_id=card_id, username=username, password=password1)
                new_user.save()
                return redirect('/login/')
        else:
            return render(request, 'register.html', locals())
    register_form = UserRegisterForm()
    return render(request, 'register.html', locals())


def logout_view(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    logout(request)
    return redirect("/login/")


# class CustomPasswordResetForm(PasswordRestForm):
#     # 实现'邮箱未注册'的提示
#     class clean_email(self):
#         email = self.cleaned_date.get('email', '')
#         if not User.objects.filter(email=email):
#             raise forms.ValidationError('邮箱未注册')
#         return email

# class CustomPasswordResetView(PasswordRestView):
#     template_name = 'your_passd_reset.html'
#     form_class = CustomPasswordResetForm
