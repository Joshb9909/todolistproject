from django.db import models
from todolistapp.models import toDoList

# Create your models here.

class Task(models.Model):

    to_do_list_id = models.ForeignKey(toDoList, blank = False, null = False, on_delete = models.CASCADE, related_name = 'task')
    task_text = models.CharField(max_length = 50, blank = False, null = False)