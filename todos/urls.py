from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views

urlpatterns = [
    path("class/<int:pk>/", views.DetailTodo.as_view(), name="class_todo_detail"),
    # path("func/<int:pk>/", views.detailTodo, name="function_todo_detail"),
    path("class_list/<int:user_id>/", views.ListTodo.as_view(), name="class_todo_list"),
    path("func_list/<int:user_id>/", views.listTodo, name="function_todo_list"),
    path("class_create_todo/", views.CreateTodo.as_view(), name="create_todo"),
    # path("func_create_todo/", views.createTodo, name="create_todo"),
    path("class_edit_todo/<int:pk>", views.EditTodo.as_view(), name="edit_todo"),
    path("users/", views.UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user"),
    # auth
    # path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/refresh/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # exercise
    # path("redirect/<str:exercise_name>", views.redirect_to_frontend, name="redirect"),
    path(
        "list_exercises/<int:user_id>", views.list_all_exercises, name="list_exercises"
    ),
    path("create_exercise/", views.create_exercise, name="create_exercise"),
    path(
        "CRUD_exercise/<int:pk>/",
        views.CRUD_exercise.as_view(),
        name="CRUD_exercise",
    ),
]
