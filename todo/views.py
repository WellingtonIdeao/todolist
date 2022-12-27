from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer


class TodoItemList(ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer