from django.urls import path
from .views import task_list,task_detail


urlpatterns = [
    path("tasks/", task_list, name="polls_list"),
    path("tasks/<int:pk>/", task_detail, name="polls_detail")

]
