# 必须使用这个绝对路径进行引入，不然启动报错
from login.models import User 
from import_export import resources
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin

# UserModel: AbstractBaseUser = get_user_model()

class ProxyResource(resources.ModelResource):
    class Meta:
        model = User
        # export_order：设置导出字段的顺序
        export_order = ('id', 'username')

class UserManage(ImportExportActionModelAdmin):
    list_display = ('id','username')
    list_per_page = 5
    resource_class = ProxyResource
    search_fields = ['username']

admin.site.register(User, UserManage)
admin.site.site_header="管理后台"
admin.site.site_title="真人图书馆管理后台"
admin.site.index_title="后台主页"