from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers
from .models import Task

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-task_date')
    serializer_class = TaskSerializers

class UncompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-task_date').filter(task_completed=False)
    serializer_class = TaskSerializers

class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-task_date').filter(task_completed=True)
    serializer_class = TaskSerializers