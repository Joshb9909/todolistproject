from django.urls import path
from .views import *

urlpatterns = [
    path('create_list/', CreateToDoList.as_view(), name='createlist')
]