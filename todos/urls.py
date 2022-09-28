from django.urls import path

from . import views

urlpatterns = [
    path("class/<int:pk>/", views.DetailTodo.as_view(), name="class_todo_detail"),
    path("func/<int:pk>/", views.detailTodo, name="function_todo_detail"),
    path("class_list/", views.ListTodo.as_view(), name="class_todo_list"),
    path("func_list/", views.listTodo, name="function_todo_list"),
    path("class_create_todo/", views.CreateTodo.as_view(), name="create_todo"),
    path("func_create_todo/", views.createTodo, name="create_todo"),
    path("class_edit_todo/<int:pk>", views.EditTodo.as_view(), name="edit_todo"),
    path("users/", views.UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user"),
]
