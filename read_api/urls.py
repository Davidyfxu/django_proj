from django.urls import path

from read_api.views import get_all_read_data

urlpatterns = [
    path('read/get_all_read_data', get_all_read_data, name='get_all_read_data'),
]
