from rest_framework import serializers
from todo.models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = [
            'title',
            'description',
            'done',
            'created_at',
            'updated_at'
        ]
         