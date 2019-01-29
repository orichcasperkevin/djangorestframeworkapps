from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Task

def task_list(request):
    MAX_OBJECTS = 20
    tasks = Task.objects.all()[:MAX_OBJECTS]
    data = {"results": list(tasks.values("task", "created_by__username", "pub_date"))}
    return JsonResponse(data)


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    data = {"results": {
        "task": task.question,
        "created_by": task.created_by.username,
        "pub_date": task.pub_date
    }}
    return JsonResponse(data)
