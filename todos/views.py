from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


# Create your views here.


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@api_view(["GET"])
def listTodo(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@api_view(["GET"])
def detailTodo(request, pk):
    todo = Todo.objects.filter(pk=pk)
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def createTodo(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
