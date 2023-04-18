"""LivingLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView, ListView
from main import views as main_views
from login import views as login_views
from teacher import views as teacher_views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path, include

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import views as auth_views
from typing import List
from login.models import MyUser

UserModel = get_user_model()


class UsersListView(LoginRequiredMixin, ListView):
    http_method_names = ['get', ]

    def get_queryset(self):
        if self.request.user.is_teacher:
            return UserModel.objects.filter(is_teacher=False).exclude(id=self.request.user.id)
        else:
            return UserModel.objects.filter(is_teacher=True).exclude(id=self.request.user.id)
        # return UserModel.objects.all().exclude(id=self.request.user.id)

    def render_to_response(self, context, **response_kwargs):
        users: List[AbstractBaseUser] = context['object_list']

        data = [{
            "username": user.get_username(),
            "pk": str(user.pk)
        } for user in users]
        return JsonResponse(data, safe=False, **response_kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', login_required(TemplateView.as_view(template_name='base.html')), name='home'),
    path('index/', main_views.index),
    path('index/<int:num>/',main_views.detail,name='detail'),
    path('teacher/', teacher_views.index),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('login/', login_views.login_view),
    path('register/', login_views.register_view),
    # path('change_password/', login_views.ChangePasswordView.as_view(), name='change_password'),
    # path('password_reset/', include('password_reset.urls')),
    path('captcha/', include('captcha.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', login_views.logout_view),
    re_path(r'', include('django_private_chat2.urls',
            namespace='django_private_chat2')),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
