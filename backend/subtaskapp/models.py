from django.db import models
from taskapp.models import Task

# Create your models here.

class SubTask(models.Model):

    task_id = models.ForeignKey(Task, related_name = 'subtask', on_delete = models.CASCADE, blank = False, null = False)
    sub_task_text = models.CharField(max_length = 50, blank = False, null = False)