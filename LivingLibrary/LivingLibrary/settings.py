"""
Django settings for LivingLibrary project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECURE_CROSS_ORIGIN_OPENER_POLICY = 'None'
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_rqr#y!7y!-oba7&z)o+b#qen$he!p0sb2*(-3gm4218^m^0_w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False 

ALLOWED_HOSTS = ['*']
# ALLPWED_HOST = ['110.40.190.72']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'import_export',
    'ckeditor',
    'ckeditor_uploader',#带图片上传的ckeditor``
    # 'password_reset',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'chat',
    'django_private_chat2',

    'main',
    'login',
    # 'teacher',

    'bootstrap4',
    'captcha',
    'channels',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LivingLibrary.urls'
LOGIN_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LivingLibrary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '110.40.190.72',
        'PORT': '3306',
        'USER': 'zyt',
        'PASSWORD': 'PYENN4mNihXtcxPF',
        'NAME': 'livinglibrarydb',
    },
    # # 取消对外键的检查
    # 'OPTIONS': {
    #     "init_command": "SET foreign_key_checks = 0;",
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'login.MyUser'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False
# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# simple ui
SIMPLEUI_LOGO = 'http://www.wzu.edu.cn/__local/0/E8/06/4670119A4E453581250C1D4D924_0AFE2605_4FDA.png'

# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False

# 修改左侧菜单首页设置
# SIMPLEUI_HOME_PAGE = '/index/'  # 指向页面
# SIMPLEUI_HOME_TITLE = '首页' # 首页标题
# SIMPLEUI_HOME_ICON = 'fa fa-code' # 首页图标

# 设置右上角Home图标跳转链接，会以另外一个窗口打开
SIMPLEUI_INDEX = '/index/'

# Channels
ASGI_APPLICATION = 'LivingLibrary.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/').replace('\\', '/')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'molly_zheng253@163.com'
# EMAIL_HOST_PASSWORD = 'zyt+0530!'
EMAIL_HOST_PASSWORD = 'YCFCAHSKGOZXJYPD'
DEFAULT_FROM_EMAIL = 'molly_zheng253@163.com'

CORS_ALLOW_ALL_ORIGINS = True

# SESSION_COOKIE_DOMAIN = '110.40.190.72'
SESSION_SAVE_EVERY_REQUEST = True

# 使用ck的工具栏并修改，宽度自适应
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        'width': 'auto',
        'height': '300px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 工具栏按钮
        'toolbar_Custom': [
            # 预览、表情
            ['Preview', 'Smiley'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 格式、字体、大小
            ['Format', 'Font', 'FontSize'],
            # 链接
            ['Link', 'Unlink'],
            # 列表
            ['Image', 'NumberedList', 'BulletedList'],
            # 居左，居中，居右
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            # 最大化
            ['Maximize']
        ],
        # 加入代码块插件
        'extraPlugins': ','.join(['codesnippet', 'image2', 'filebrowser', 'widget', 'lineutils']),
    },
    # 评论
    'comment': {
        # 编辑器宽度自适应
        'width': 'auto',
        'height': '140px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 工具栏按钮
        'toolbar_Custom': [
            # 表情 代码块
            ['Smiley', 'CodeSnippet'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 链接
            ['Link', 'Unlink'],
            # 列表
            ['NumberedList', 'BulletedList'],
        ],
        # 加入代码块插件
        'extraPlugins': ','.join(['codesnippet']),
    }
}

CKEDITOR_UPLOAD_PATH = "uploads/"#文件保存为止，因为上边配置了media， 图片将保存至media/uploads下