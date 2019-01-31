'''
urls for accesing Api
'''
from django.urls import path
from .views import TaskList,TaskDetail,SubTaskList,SubTaskCreate,TaskViewSet,UserCreate,LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks',TaskViewSet,base_name='tasks')


urlpatterns = [

#the urls used for accessing the api endpoints
   #create a new user
    path("users/", UserCreate.as_view(), name="user_create"),
  # logging in User
    path("login/",LoginView.as_view(),name="login"),    
   #lists tasks
    path("tasks/", TaskList.as_view(), name="task_list"),
  #lists task with id as a parameter
    path("tasks/<int:pk>/", TaskDetail.as_view() , name="task_detail"),
  #lists subtasks ..can create a subtask using POST
    path("tasks/<int:pk>/subtasks/", SubTaskList.as_view(), name="subtask_list"),
  #creates a subtask using POST method.
    path("tasks/<int:pk>/subtasks/<int:subtask_pk>/create", SubTaskCreate.as_view(), name="create_subtask"),

]
urlpatterns += router.urls
