from django.urls import path
from .views import *

urlpatterns = [
    path('create-account/', CreateAccount.as_view(), name='createaccount'),
]
