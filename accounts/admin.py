from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email',  'first_name', 'last_name', 'is_staff', 'is_active','date_joined')
    search_fields = ('email', 'first_name')
    readonly_fields = ('date_joined', )
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email','first_name', 'last_name','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Important dates', {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser,CustomUserAdmin)
