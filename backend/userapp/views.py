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
from .utilities import HttpOnlyToken

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

class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            life_time = datetime.now() + timedelta(days=30)
            format_life_time = life_time.strftime("%a, %d %b %Y %H:%M:%S CST")
            user_serializer = UserSerializer(user)
            response = Response({"user":{**user_serializer.data}})
            response.set_cookie(key="token", value=token.key, httponly=True, secure=True, samesite="Lax", expires = format_life_time)
            return response
            # return Response({"token": token.key, **user_serializer.data})
        else:
            return Response("No user matching credentials", status=HTTP_404_NOT_FOUND)
        
class LogOut(APIView):
    authentication_classes = [HttpOnlyToken]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
class DeleteAccount(APIView):
    authentication_classes = [HttpOnlyToken]
    permission_classes = [IsAuthenticated]

    def delete(self, request):

        request.user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

