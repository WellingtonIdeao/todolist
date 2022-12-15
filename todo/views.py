from rest_framework.generics import ListAPIView
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer

class TodoItemList(ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
