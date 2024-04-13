from django.urls import path
from .views import *

urlpatterns = [
    path('create-account/', CreateAccount.as_view(), name='createaccount'),
    path('login/', LogIn.as_view(), name="login"),
    path('logout/', LogOut.as_view(), name="logout"),
    path('deleteaccount/', DeleteAccount.as_view(), name="deleteaccount"),
]
