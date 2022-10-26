from django import forms
from captcha.fields import CaptchaField

GROUPS_CHOICES = (
    (1, "Manager"),
    (2, "Teacher"),
    (3, "Student"),
)


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control',  'placeholder': "Password"}))
    captcha = CaptchaField(label='验证码')


class UserRegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control',  'placeholder': "Password"}))
    password2 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control',  'placeholder': "Password"}))
    group = forms.ChoiceField(choices=GROUPS_CHOICES)
    captcha = CaptchaField(label='验证码')
