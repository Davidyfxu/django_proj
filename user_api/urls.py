from django.urls import path
from .views import user_create, user_login

urlpatterns = [
    # 用于创建新用户的路由
    path('users/create/', user_create, name='user-create'),

    # 用于用户登录的路由
    path('users/login/', user_login, name='user-login'),
]
