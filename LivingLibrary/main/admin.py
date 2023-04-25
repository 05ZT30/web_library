from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

from .models import *

class RollAdmin(BaseUserAdmin):
    list_display = ('id', 'title', 'picture',)
    list_per_page = 20
    list_filter = ('title',)
    fieldsets = (
        ('基本信息', {'fields': ('id', 'title', 'picture')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'title', 'picture',),
        }),
    )
    # del BaseUserAdmin.search_fields
    ordering = ['id']
    filter_horizontal = ()

admin.site.register(News)
admin.site.register(roll,RollAdmin)