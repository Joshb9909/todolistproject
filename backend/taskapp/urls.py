from django.urls import path
from .views import *

urlpatterns = [
    path('createtask/', CreateTask.as_view(), name='createtask'),
    path('deletetask/', DeleteTask.as_view(), name='deletetask'),
]