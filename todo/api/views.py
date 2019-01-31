'''
    api views for the apps API
'''
from rest_framework import generics,viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate

from  todo.models import Task,SubTask
from  .serializers import TaskSerializer,SubTaskSerializer,UserSerializer

class TaskList(generics.ListCreateAPIView):
        queryset = Task.objects.all()
        serializer_class = TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
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
#subtask creation view API view is used for complete customization
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
#authentication .. a view for creating a new user
class UserCreate(generics.CreateAPIView):
#give exemption to UserCreate view for authentication by overriding the global setting
        authentication_classes = ()
        permission_classes = ()
        serializer_class = UserSerializer

#API to verify a user and get a token to identify them, we will call this endpoint /login/
class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
