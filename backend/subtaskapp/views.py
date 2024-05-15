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

class CreateSubTask(APIView):
    authentication_classes = [HttpOnlyToken]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        sub_task_data = {
            'task_id': request.data.get('task_id'),
            'sub_task_text': request.data.get('sub_task_text')
        }
        serializer = SubTaskSerializer(data=sub_task_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
