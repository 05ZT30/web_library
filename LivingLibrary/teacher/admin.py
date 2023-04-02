from django.contrib.admin import ModelAdmin, site
from .models import MyTeacher


class TeacherModelAdmin(ModelAdmin):
    search_fields = ('id', 'username','catagory')
    list_display = ('id', 'username', 'catagory', 'email')
    list_display_links = ('id',)
    list_filter = ('catagory',)

site.register(MyTeacher,TeacherModelAdmin )
