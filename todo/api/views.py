'''
    api views for the apps API
'''
from rest_framework import generics

from  todo.models import Task,SubTask
from  .serializers import TaskSerializer,SubTaskSerializer

class TaskList(generics.ListCreateAPIView):
        queryset = Task.objects.all()
        serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveDestroyAPIView):
        queryset = Task.objects.all()
        serializer_class = TaskSerializer
#subtask for listing  subtask
class SubTaskList(generics.ListCreateAPIView):
        queryset = SubTask.objects.all()
        serializer_class = SubTaskSerializer
#subtask creation view
class SubTaskCreate(generics.CreateAPIView):
        queryset = SubTask.objects.all()
        serializer_class = SubTaskSerializer
