# 必须使用这个绝对路径进行引入，不然启动报错
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats
from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group, AbstractBaseUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

from login.models import MyUser
# UserModel: AbstractBaseUser = get_user_model()


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username = forms.CharField(label='用户名', max_length=30, required=True)
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='确认密码', widget=forms.PasswordInput)
    is_teacher = forms.BooleanField(required=False, label='是否为老师')
    is_admin = forms.BooleanField(required=False, label='是否为能访问管理界面')
    is_superuser = forms.BooleanField(required=False, label='是否能管理数据')
    email = forms.EmailField(required=False, label=("邮箱"))
    card_id = forms.CharField(required=True, label=("学工号"))
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
    card_id = forms.CharField(required=True, label=("学工号"))
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
                  'is_active', 'is_admin', 'is_superuser')


class ProxyResource(resources.ModelResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_id = MyUser.objects.all().order_by('-id').first().id + 1

    def before_import_row(self, row, **kwargs):
        # assert False, 'before_import_row was called'
        print(f'Row data: {row}')
        value = row['password']
        encrypted_password = make_password(value)
        print(f'Encrypted password: {encrypted_password}')
        row['password'] = encrypted_password
        super().before_import_row(row, **kwargs)

    class Meta:
        model = MyUser
        # export_order：设置导出字段的顺序
        export_order = ('is_teacher', 'id', 'username')
        exclude = ('is_active',)
        skip_unchanged = True
        report_skipped = False


class CardIdListFilter(admin.SimpleListFilter):
    title = _('班级')
    parameter_name = 'card_id'

    def lookups(self, request, model_admin):
        return (
            ('202206', _('2022级6班')),
            ('202205', _('2022级5班')),
            ('202204', _('2022级4班')),
            ('202203', _('2022级3班')),
            ('202202', _('2022级2班')),
            ('202201', _('2022级1班')),
            ('202106', _('2021级6班')),
            ('202105', _('2021级5班')),
            ('202104', _('2021级4班')),
            ('202103', _('2021级3班')),
            ('202102', _('2021级2班')),
            ('202101', _('2021级1班')),
            ('202006', _('2020级6班')),
            ('202005', _('2020级5班')),
            ('202004', _('2020级4班')),
            ('202003', _('2020级3班')),
            ('202002', _('2020级2班')),
            ('202001', _('2020级1班')),
            ('201906', _('2019级6班')),
            ('201905', _('2019级5班')),
            ('201904', _('2019级4班')),
            ('201903', _('2019级3班')),
            ('201902', _('2019级2班')),
            ('201901', _('2019级1班')),
            ('201806', _('2018级6班')),
            ('201805', _('2018级5班')),
            ('201804', _('2018级4班')),
            ('201803', _('2018级3班')),
            ('201802', _('2018级2班')),
            ('201801', _('2018级1班')),
            ('201706', _('2017级6班')),
            ('201705', _('2017级5班')),
            ('201704', _('2017级4班')),
            ('201703', _('2017级3班')),
            ('201702', _('2017级2班')),
            ('201701', _('2017级1班')),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(card_id__startswith=self.value())


class UserAdmin(BaseUserAdmin, ImportExportActionModelAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    formats = (base_formats.XLS,base_formats.XLSX )

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'is_teacher', 'card_id', 'username',
                    'email', 'phone', 'category', 'is_admin', 'introduction')
    list_per_page = 20
    list_filter = ('username', 'is_teacher', 'category',CardIdListFilter)

    fieldsets = (
        ('基本信息', {'fields': ('card_id', 'username', 'password')}),
        ('个人信息', {'fields': ('date_of_birth', 'phone',
         'email', 'category', 'photo', 'introduction',)}),
        ('权限', {'fields': ('is_admin', 'is_superuser', 'is_teacher')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'is_teacher', 'is_admin', 'is_superuser', 'card_id', 'email',
                'date_of_birth',
                'phone',
                'email',
                'category',
                'photo',
                'introduction',
            ),
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
