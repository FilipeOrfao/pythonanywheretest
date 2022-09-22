from django.conf import settings
from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    date_ticked = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
