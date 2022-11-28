from django.contrib import admin

from .models import Todo, Exercise

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "user", "user_id")


admin.site.register(Todo, TodoAdmin)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "reps", "sets", "weight", "time", "user", "user_id")


admin.site.register(Exercise, ExerciseAdmin)
