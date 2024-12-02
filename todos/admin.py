from django.contrib import admin

# Register your models here.
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "user",
        "created_at",
        "updated_at",
        "done"
    ]

    list_filter = [
        "user",
        "created_at",
        "updated_at", 
        "done"
    ]

admin.site.register(Todo, TodoAdmin)
