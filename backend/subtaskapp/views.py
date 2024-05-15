from django.shortcuts import render, get_object_or_404
from .models import SubTask
from .serializers import SubTaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_403_FORBIDDEN
)
from userapp.utilities import HttpOnlyToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.
