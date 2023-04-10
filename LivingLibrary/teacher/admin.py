from django.contrib.admin import ModelAdmin, site
from .models import MyTeacher
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

class TeacherCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyTeacher
        fields = ('username','email', 'date_of_birth')

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


class TeacherChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyTeacher
        fields = ('card_id','username','email', 'password', 'date_of_birth',
                  'is_active', 'is_admin')


class ProxyResource(resources.ModelResource):
    class Meta:
        model = MyTeacher
        # export_order：设置导出字段的顺序
        export_order = ('id', 'username')

class TeacherAdmin(BaseUserAdmin,ImportExportActionModelAdmin):
    # The forms to add and change user instances
    form = TeacherChangeForm
    add_form = TeacherCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'card_id','username', 'catagory', 'email','phone')
    list_per_page = 20
    list_display_links = ('id',)
    list_filter = ('catagory','username')
    fieldsets = (
        (None, {'fields': ('card_id','username','email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('card_id','username','catagory','email', 'phone', 'password1', 'password2'),
        }),
    )
    ordering = ['id']
    filter_horizontal = ()
    resource_class = ProxyResource

site.register(MyTeacher,TeacherAdmin )
