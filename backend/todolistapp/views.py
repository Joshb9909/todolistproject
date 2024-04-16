from django.shortcuts import render, get_object_or_404
from .models import ToDoList
from .serializers import ToDoListSerializer
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

class CreateToDoList(APIView):
    authentication_classes = [HttpOnlyToken]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        user = request.user
        post_data ={
            'user_id' : user.id,
            'title' : request.data.get('title')
        }
        serializer = ToDoListSerializer(data=post_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class DeleteToDoList(APIView):
    authentication_classes = [HttpOnlyToken]
    permission_classes = [IsAuthenticated]

    def delete(self, request):

        to_do_list_id = request.data.get('list_id')
        to_do_list = get_object_or_404(ToDoList, pk=to_do_list_id)

        if request.user != to_do_list.user_id:

            return Response(status= HTTP_403_FORBIDDEN)
        
        to_do_list.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    