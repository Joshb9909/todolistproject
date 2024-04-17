from django.db import models
from todolistapp.models import ToDoList

# Create your models here.

class Task(models.Model):

    to_do_list_id = models.ForeignKey(ToDoList, blank = False, null = False, on_delete = models.CASCADE, related_name = 'task')
    task_text = models.CharField(max_length = 50, blank = False, null = False)
    is_done = models.BooleanField(default=False, blank=False, null=False)