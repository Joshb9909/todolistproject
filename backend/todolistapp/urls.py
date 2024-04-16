from django.urls import path
from .views import *

urlpatterns = [
    path('create_list/', CreateToDoList.as_view(), name='createlist'),
    path('delete_list/', DeleteToDoList.as_view(), name='deletelist'),
    path('get_one_list/', GetOneList.as_view(), name ='getonelist'),
    path('get_all_lists/', GetAllLists.as_view(), name ='getalllists'),
]