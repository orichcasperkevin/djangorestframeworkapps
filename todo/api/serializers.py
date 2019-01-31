'''
    serializers for the two models
'''
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import serializers

from todo.models import Task,SubTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task','created_by','pub_date','completionstatus')


class SubTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True, required=False)

    class Meta:
        model = SubTask
        fields = ('subtask','associated_task','pub_date','completionstatus')

#Authetication .. this endpoint is for createin a new user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
    #tokens are created when user is created in UserCreate view
        Token.objects.create(user=user)
        user.save()
        return user
