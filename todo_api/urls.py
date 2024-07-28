from django.urls import path
from . import views

urlpatterns = [
    path('test_connection/', views.test_connection),
    path('get_todos/', views.get_todos, name='get_todos'),
]
