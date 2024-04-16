from django.urls import path
from .views import *

urlpatterns = [
    path('create_list/', CreateToDoList.as_view(), name='createlist'),
    path('delete_list/', DeleteToDoList.as_view(), name='deletelist'),
]