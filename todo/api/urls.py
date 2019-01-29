'''
urls for accesing Api 
'''
from django.urls import path
from .views import TaskList,TaskDetail


urlpatterns = [

#the urls used for accessing the api endpoints

    path("tasks/", TaskList.as_view(), name="task_list"),
    path("tasks/<int:pk>/", TaskDetail.as_view() , name="task_detail")

]
