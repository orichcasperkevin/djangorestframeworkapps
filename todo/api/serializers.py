'''
    serializers for the two models .
'''
from rest_framework import serializers

from todo.models import Task,SubTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class SubTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True, required=False)

    class Meta:
        model = SubTask
        fields = '__all__'
