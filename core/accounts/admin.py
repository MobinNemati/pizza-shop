from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ("phone_number", "is_superuser", "is_verified")
    list_filter = ("phone_number", "is_superuser", "is_verified")
    serching_fields = ('phone_number',)
    ordering = ('phone_number',)

    fieldsets = (
        ('Authentication', {
            "fields": (
                'phone_number', 'password'
            ),
        }),

        ('Permissions', {
            "fields": (
                'is_staff', 'is_superuser', 'is_verified'
            ),
        }),
        ('Group permission', {
            "fields": (
                'groups', 'user_permissions'
            ),
        }),
        ('Important dates', {
            "fields": (
                'last_login',
            ),
        }),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_verified')}
        ),
    )
    



admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)