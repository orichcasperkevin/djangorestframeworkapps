'''
    api views for the apps API
'''
from rest_framework import generics,viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

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
    def get_queryset(self):
        queryset = SubTask.objects.filter(associated_task_id = self.kwargs["pk"])
        return queryset
    serializer_class = SubTaskSerializer
#subtask creation view
class SubTaskCreate(APIView):
    def post(self,request,pk,subtask_pk):
        created_by = request.data.get("created_by")
        data = {'SubTask': subtask_pk, 'Task': pk, 'created_by': created_by}
        serializer = SubTaskSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
