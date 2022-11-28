from dataclasses import field
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Todo, Exercise


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ("id", "title", "body")
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username")
