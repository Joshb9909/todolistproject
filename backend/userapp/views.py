from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from datetime import datetime, timedelta
# from .utilities import HttpOnlyToken

class CreateAccount(APIView):

    def post(self, request):

        try:
            user = User.objects.create_user(
                username = request.data["username"]
            )
            token = Token.objects.create(user = user)
            return Response(
                {"user": user.username, "token": token.key}, status= HTTP_201_CREATED
            )
        except:
            return Response(
                {"error": "A user with this username already exists."}, status= HTTP_400_BAD_REQUEST
            )
