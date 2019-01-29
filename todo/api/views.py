'''
    api views for the apps API 
'''

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from  todo.models import Task,SubTask
from  .serializers import TaskSerializer

class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()[:20]
        data = TaskSerializer(tasks, many=True).data
        return Response(data)


class TaskDetail(APIView):
    def get(self, request, pk):
        tasks = get_object_or_404(Task, pk=pk)
        data = TaskSerializer(tasks).data
        return Response(data)
