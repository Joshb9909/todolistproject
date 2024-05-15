from rest_framework import serializers
from .models import SubTask

class SubTaskSerializer(serializers.ModelSerializer):

    class Meta:

        model = SubTask
        fields = ['task_id', 'sub_task_text', 'id']