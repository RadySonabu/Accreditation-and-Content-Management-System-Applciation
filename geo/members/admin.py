from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.forms import ReadOnlyPasswordHashField

from members.models import MyUser, Role, College, Program
from import_export.admin import ImportExportModelAdmin


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('employee_number', 'first_name', 'middle_initial',
                  'last_name', 'contact', 'email', 'role',  'college', 'program', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['college'].queryset = MyUser.objects.none()
        self.fields['program'].queryset = MyUser.objects.none()

        if 'role' in self.data:
            try:
                role_id = int(self.data.get('role'))
                self.fields['college'].queryset = College.objects.filter(
                    role_id=role_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['college'].queryset = self.instance.role.college_set

        if 'college' in self.data:
            try:
                college_id = int(self.data.get('college'))
                self.fields['program'].queryset = Program.objects.filter(
                    college_id=college_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['program'].queryset = self.instance.role.program_set

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
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('employee_number', 'first_name', 'middle_initial',
                  'last_name', 'contact', 'email', 'role',  'college', 'program',  'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('employee_number',  'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('employee_number', 'password')}),
        ('Personal info', {'fields': (
            'first_name', 'middle_initial', 'last_name', 'contact', 'email', 'role',  'college', 'program')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('employee_number', 'first_name', 'middle_initial', 'last_name', 'contact', 'email',  'password1', 'password2' 'role',  'college', 'program')}
         ),
    )
    search_fields = ('last_name',)
    ordering = ()
    filter_horizontal = ()


# Now register the new UserAdmin...
# admin.site.register(MyUser, UserAdmin)


@admin.register(MyUser)
class ViewAdmin(ImportExportModelAdmin):
    pass


    # ... and, since we're not using Django's built-in permissions,
    # unregister the Group model from admin.
admin.site.unregister(Group)
admin.site.register(Role)
admin.site.register(College)
admin.site.register(Program)
