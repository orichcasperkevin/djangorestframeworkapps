from django.db import models
from django.contrib.auth.models import User
# The  specific task model
class Task(models.Model):
    task = models.CharField(max_length=100)
    '''
        a task is created by a registered user to the system.
    '''
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    completionstatus = models.BooleanField(default = True)

    def __str__(self):
        return self.task
# a subtask associated to a task
class SubTask(models.Model):
    subtask = models.CharField(max_length=100)
    '''
        every SubTask has an associated task and "subtasks is the name used to acces it"
    '''
    associated_task = models.ForeignKey(Task ,on_delete=models.CASCADE, related_name = "subtasks")
    pub_date = models.DateTimeField(auto_now=True)
    completionstatus = models.BooleanField(default = True)


    def __str__(self):
        return self.subtask
