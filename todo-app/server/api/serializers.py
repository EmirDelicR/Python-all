from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("title", "task", "done", "id", "changed_at")
        # fields = '__all__'
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.task = validated_data.get("task", instance.task)
        instance.save()
        return instance