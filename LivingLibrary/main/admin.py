from django.contrib import admin
from django.utils.html import format_html
from .models import *

admin.site.register(News)
@admin.register(roll)
class main(admin.ModelAdmin):
    def shpic(self,obj):
        return format_html('<img src="/media/%s" height="188px" />' % obj.picture)
    list_display=("title","shpic","add_date")
    shpic.short_description=u'图片预览'
    list_per_page=3
