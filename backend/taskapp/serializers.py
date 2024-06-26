from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:

        model = Task
        fields = ['to_do_list_id', 'task_text','is_done', 'id']