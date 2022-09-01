from django.urls import path

from . import views

urlpatterns = [
    path("class/<int:pk>/", views.DetailTodo.as_view(), name="class_todo_detail"),
    path(
        "functional/<int:pk>/", views.DetailTodo.as_view(), name="function_todo_detail"
    ),
    path("class_list/", views.ListTodo.as_view(), name="class_todo_list"),
    path("functional_list/", views.listTodo, name="function_todo_list"),
    path("create_todo/", views.createTodo, name="create_todo"),
]
