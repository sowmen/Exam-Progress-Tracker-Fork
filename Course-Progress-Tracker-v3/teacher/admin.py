from teacher.models import Committee, Course, Deadline, Teacher
from django.contrib import admin

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Deadline)


@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    readonly_fields = ("committee_id",)
