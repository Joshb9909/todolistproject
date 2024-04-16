from rest_framework import serializers
from .models import toDoList

class ToDoListSerializer(serializers.ModelSerializer):

    class Meta:

        model = toDoList
        fields = ['user_id', 'title', 'id']
