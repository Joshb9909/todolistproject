from django.db import models
from userapp.models import User

class toDoList(models.Model):
    user_id = models.ForeignKey(User, related_name = 'todolist', on_delete = models.CASCADE, blank = False, null = False)
    title = models.CharField(max_length = 50, blank = False, null = False)
    
