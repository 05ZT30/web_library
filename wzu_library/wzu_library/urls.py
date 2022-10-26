"""wzu_library URL Configuration

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
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path, include

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.models import AbstractBaseUser

from typing import List

UserModel = get_user_model()


class UsersListView(LoginRequiredMixin, ListView):
    http_method_names = ['get', ]

    def get_queryset(self):
        return UserModel.objects.all().exclude(id=self.request.user.id)

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
    path('users/', UsersListView.as_view(), name='users_list'),
    path('login/', login_views.login_view),
    # path('login_teacher/', login_views.login_teacher),
    # path('login_manager/', login_views.login_manager),
    path('register', login_views.register_view),
    # path('register_student/', login_views.register_student),
    # path('register_teacher/', login_views.register_teacher),
    path('logout/', login_views.logout_view),
    re_path(r'', include('django_private_chat2.urls',
            namespace='django_private_chat2')),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
