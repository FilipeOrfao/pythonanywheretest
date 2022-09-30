from django.contrib import admin

from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "user", "user_id")
    # pass


admin.site.register(Todo, TodoAdmin)
