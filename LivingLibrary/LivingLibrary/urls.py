"""
URL configuration for LivingLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import views as auth_views
from typing import List
from django.conf.global_settings import MEDIA_ROOT
from django.views.static import serve
from django_private_chat2 import consumers

UserModel = get_user_model()


class UsersListView(LoginRequiredMixin, ListView):
    http_method_names = [
        "get",
    ]

    def get_queryset(self):
        if ~self.request.user.is_teacher:
            return UserModel.objects.filter(is_teacher=True).exclude(
                id=self.request.user.id
            )
        # return UserModel.objects.filter(is_teacher=True).exclude(id=self.request.user.id)
        # return UserModel.objects.all().exclude(id=self.request.user.id)

    def render_to_response(self, context, **response_kwargs):
        users: List[AbstractBaseUser] = context["object_list"]

        data = [{"username": user.username, "pk": str(user.pk)} for user in users]
        return JsonResponse(data, safe=False, **response_kwargs)


urlpatterns = [
    re_path("admin/", admin.site.urls),
    re_path(
        r"", include("django_private_chat2.urls", namespace="django_private_chat2")
    ),
    path("chat2/", include("chat2.urls")),
    path(
        "chat/",
        login_required(TemplateView.as_view(template_name="chat.html")),
        name="chat_home",
    ),
    path("index/", main_views.index),
    path("index/<int:num>/", main_views.detail, name="detail"),
    path("teacher/", teacher_views.index),
    path("teacher/teacherDetail", teacher_views.teacherDetail),
    path("users/", UsersListView.as_view(), name="users_list"),
    path("login/", login_views.login_view),
    path("register/", login_views.register_view),
    # path('change_password/', login_views.ChangePasswordView.as_view(), name='change_password'),
    # path('password_reset/', include('password_reset.urls')),
    path("captcha/", include("captcha.urls")),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("logout/", login_views.logout_view),
    # 上传media的文件可以被查看，这个很重要，更后边的一个bug有关
    re_path(r"^index/static/media/(?P<path>.*)$", serve, {"document_root": MEDIA_ROOT}),
    # ckckeditor图片上传
    path("ckeditor/", include("ckeditor_uploader.urls")),
    # re_path(r"^chat_ws$", consumers.ChatConsumer.as_asgi()),
] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
