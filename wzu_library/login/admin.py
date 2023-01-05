# 必须使用这个绝对路径进行引入，不然启动报错
from login.models import Person as UserModel 
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin

class ProxyResource(resources.ModelResource):
    class Meta:
        model = UserModel
        # export_order：设置导出字段的顺序
        export_order = ('id', 'username')

# 注册小区表
class UserManage(ImportExportActionModelAdmin):
    list_per_page = 5
    resource_class = ProxyResource

admin.site.register(UserModel, UserManage)
admin.site.site_header="管理后台"
admin.site.site_title="真人图书馆管理后台"
admin.site.index_title="后台主页"