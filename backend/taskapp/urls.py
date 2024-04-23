from django.urls import path
from .views import *

urlpatterns = [
    path('createtask/', CreateTask.as_view(), name='createtask'),
    path('deletetask/', DeleteTask.as_view(), name='deletetask'),
    path('gettasks/', GetAllTasks.as_view(), name='gettasks'),
    path('getonetask/', GetOneTask.as_view(), name='getonetask'),
]