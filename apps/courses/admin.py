from django.contrib import admin

from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'price',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'title',
        'description',
    )
