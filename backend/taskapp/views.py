from django.shortcuts import render, get_object_or_404
from .models import Task
from .serializers import TaskSerializer
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

class CreateTask(APIView):
    authentication_classes = [HttpOnlyToken]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        task_data ={
            'to_do_list_id' : request.data.get('to_do_list_id'),
            'task_text' : request.data.get('task_text'),
        }
        serializer = TaskSerializer(data=task_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

