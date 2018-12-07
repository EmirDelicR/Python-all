from .models import Task
from rest_framework import serializers

class TaskSerializers(serializers.ModelSerializer):
    """Serialize data to JSON"""
    class Meta:
        model = Task
        """Set the fields that REST-api return"""
        fields = ('id', 'task_name', 'task_desc', 'task_completed')