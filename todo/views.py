from rest_framework.viewsets import ModelViewSet
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer


class TodoItemCRUDViewSet(ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer