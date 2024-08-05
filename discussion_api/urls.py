from django.urls import path
from .views import get_all_discussion_data

urlpatterns = [
    path('discussion/get_all_discussion_data', get_all_discussion_data, name='get_all_discussion_data'),
]
