# Generated by Django 4.1 on 2022-09-06 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="done",
            field=models.BooleanField(default=False),
        ),
    ]