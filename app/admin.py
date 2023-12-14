from django.contrib import admin


from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "due_date", "completed")
    list_filter = ("due_date",)
    search_fields = ("title", "description")
    ordering = ("due_date",)


admin.site.register(Task, TaskAdmin)
