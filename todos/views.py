from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo, Exercise
from .serializers import TodoSerializer, UserSerializer, ExerciseSerializer

from .persimmions import IsAuthorOrReadOnly

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        token["email"] = user.email

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ListTodo(generics.ListAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Todo.objects.all()
    # queryset = Todo.objects.filter(user_id=kwargs)
    serializer_class = TodoSerializer


# class ListTodo(APIView):
#     def get_object(self, user_id):
#         try:
#             return Todo.objects.get(user_id=user_id)
#         except Todo.DoesNotExist:
#             raise {"message", "nothing here bud"}

#     def get(self, request, user_id, format=None):
#         snippet = self.get_object(user_id)
#         serializer = TodoSerializer(snippet, many=True)
#         return serializer.data


@api_view(["GET"])
@permission_classes([IsAuthorOrReadOnly])
def listTodo(request, user_id):
    todos = Todo.objects.filter(user_id=user_id)
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# @api_view(["GET"])
# def detailTodo(request, pk):
#     todo = Todo.objects.filter(pk=pk)
#     serializer = TodoSerializer(todo, many=True)
#     return Response(serializer.data)


class CreateTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# @api_view(["POST"])
# def createTodo(request):
#     serializer = TodoSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


class EditTodo(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthorOrReadOnly]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# exercise
# @api_view(["GET"])
# def redirect_to_frontend(request, exercise_name):
# this is for the nfc thing
# need to send variable name to the front end but don't know how to to that
# return redirect(f"http://localhost:5173/fefe/todo/", {"thing": exercise_name})


@api_view(["GET"])
@permission_classes([IsAuthorOrReadOnly])
def list_all_exercises(request, user_id):
    exercises = Exercise.objects.filter(user_id=user_id)
    serializer = ExerciseSerializer(exercises, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_exercise(request):
    serializer = ExerciseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response({"Error": "Invalid input"})


class CRUD_exercise(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
