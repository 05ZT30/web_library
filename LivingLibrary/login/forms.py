from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
# from .models import MyUser,MyTeacher

GROUPS_CHOICES = (
    ("Manager", "管理员"),
    ("Teacher", "教师"),
    ("Student", "学生"),
)


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control',  'placeholder': "Password"}))
    captcha = CaptchaField(label='验证码')


class UserRegisterForm(forms.Form):
    card_id = forms.CharField(label="学工号", max_length=8, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "CardID", 'autofocus': ''}))
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control',  'placeholder': "Password"}))
    password2 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control',  'placeholder': "Please Confirm Password"}))
    # group = forms.ChoiceField(choices=GROUPS_CHOICES)
    captcha = CaptchaField(label='验证码')

# class CustomPasswordResetForm(PasswordResetForm):
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if not MyUser.objects.filter(email__iexact=email).exists():
#             raise ValidationError("该邮箱未注册。")
#         return email