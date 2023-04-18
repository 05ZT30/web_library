# 必须使用这个绝对路径进行引入，不然启动报错
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group, AbstractBaseUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from login.models import MyUser
# UserModel: AbstractBaseUser = get_user_model()


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username = forms.CharField(label='用户名', max_length=30)
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='确认密码', widget=forms.PasswordInput)
    is_teacher = forms.BooleanField(required=False,label='是否为老师')
    is_admin = forms.BooleanField(required=False,label='是否为管理员')
    email = forms.EmailField(required=False, label=("邮箱"))
    card_id = forms.CharField(required=False, label=("卡号"))
    date_of_birth = forms.DateField(required=False, label=("出生日期"))
    phone = forms.CharField(required=False, label=("联系电话"))
    category = forms.CharField(required=False, label=("专业领域"))
    photo = forms.ImageField(required=False, label=("照片"))
    introduction = forms.CharField(
        widget=forms.Textarea, required=False, label=("简介"))

    def clean(self):
        cleaned_data = super().clean()
        is_teacher = cleaned_data.get('is_teacher')
        category = cleaned_data.get('category')
        if is_teacher and not category:
            self.add_error('category', '当该用户为老师时，该字段必填')

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'date_of_birth')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField(label=("密码"),
                                         help_text=("未存储原始密码，因此无法查看此用户的密码，但您可以使用<a href=\"../password/\">此表单</a>更改密码。"))
    email = forms.EmailField(required=False, label=("邮箱"))
    card_id = forms.CharField(required=False, label=("卡号"))
    date_of_birth = forms.DateField(required=False, label=("出生日期"))
    phone = forms.CharField(required=False, label=("联系电话"))
    category = forms.CharField(required=False, label=("专业领域"))
    photo = forms.ImageField(required=False, label=("照片"))
    introduction = forms.CharField(
        widget=forms.Textarea, required=False, label=("简介"))

    def clean(self):
        cleaned_data = super().clean()
        is_teacher = cleaned_data.get('is_teacher')
        category = cleaned_data.get('category')
        if is_teacher and not category:
            self.add_error('category', '当该用户为老师时，该字段必填')

    class Meta:
        model = MyUser
        fields = ('card_id', 'username', 'email', 'password', 'date_of_birth', 'is_teacher', 'phone', 'category', 'photo', 'introduction',
                  'is_active', 'is_admin')


class ProxyResource(resources.ModelResource):
    class Meta:
        model = MyUser
        # export_order：设置导出字段的顺序
        export_order = ('is_teacher', 'id', 'username')


class UserAdmin(BaseUserAdmin, ImportExportActionModelAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'is_teacher', 'card_id', 'username',
                    'email', 'phone', 'category', 'is_admin', 'introduction')
    list_per_page = 20
    list_filter = ('card_id', 'username', 'is_teacher', 'category')
    fieldsets = (
        ('基本信息', {'fields': ('card_id', 'username', 'password')}),
        ('个人信息', {'fields': ('date_of_birth', 'phone',
         'email', 'category', 'photo', 'introduction',)}),
        ('权限', {'fields': ('is_admin', 'is_teacher')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'username', 'password1', 'password2', 'is_teacher','is_admin','card_id','email', 'date_of_birth', 'phone', 'email', 'category', 'photo', 'introduction',),
        }),
    )
    del BaseUserAdmin.search_fields
    ordering = ['id']
    filter_horizontal = ()
    resource_class = ProxyResource


admin.site.site_header = "管理后台"
admin.site.site_title = "真人图书馆管理后台"
admin.site.index_title = "后台主页"
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
# admin.site.unregister(AbstractBaseUser)
