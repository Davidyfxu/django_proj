from django.urls import path
from .views import user_create, user_login, user_init

urlpatterns = [
    # 用于创建新用户的路由
    path('no_auth/register/', user_create, name='user-create'),
    path('init/', user_init, name='user-init'),

    # 用于用户登录的路由
    path('no_auth/login/', user_login, name='user-login'),
]
