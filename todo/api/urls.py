'''
urls for accesing Api
'''
from django.urls import path
from .views import TaskList,TaskDetail,SubTaskList,SubTaskCreate


urlpatterns = [

#the urls used for accessing the api endpoints
   #lists tasks
    path("tasks/", TaskList.as_view(), name="task_list"),
  #lists task with id as a parameter
    path("tasks/<int:pk>/", TaskDetail.as_view() , name="task_detail"),
  #lists subtasks ..can create a subtask using POST
    path("subtask/", SubTaskList.as_view(), name="subtask_list"),
  #creates a subtask using POST method 
    path("createsubtask/", SubTaskCreate.as_view(), name="create_subtask"),

]
