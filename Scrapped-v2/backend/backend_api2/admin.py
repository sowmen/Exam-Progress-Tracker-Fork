from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Course, Deadline, User, Teacher, Committee


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password", "last_login")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )

    list_display = ("email", "is_staff", "last_login")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(User, UserAdmin)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Deadline)


@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    readonly_fields = ("committee_id",)
