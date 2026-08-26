from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):

    # نمایش ستون های مورد نظر
    list_display = (
        "email",
        "phone",
        "username",
        "is_staff",
    )

    # فیتر کردن کاربران برای نمایش مدیر یا فقط کاربر
    list_filter = (
        "is_staff",
    )

    # آخرین لاگین را فقط در پنل ادمین نمایش بده
    readonly_fields = (
        "last_login",
    )

    fieldsets = (
        (
            "Main Information", # اطلاعات اصلی
            {
                "fields": (
                    "email",
                    "phone",
                    "username",
                    "password",
                )
            }
        ),
        (
            "Permissions", # دسترسی ها
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "is_superuser",
                    "last_login",
                    "groups",
                    "user_permissions",
                )
            }
        ),
    )

    search_fields = ("email", "username", "phone") # امکان جست و جو بر اساس این فیلد ها
    ordering = ("username",) # نحوه نمایش کاربران
    filter_horizontal = ("groups", "user_permissions") # تنظیم لیست ها برای شلوغ نشدن


admin.site.register(User, UserAdmin)