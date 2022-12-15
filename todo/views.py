from rest_framework.generics import ListAPIView
from todo.models import Task
from todo.serializers import TaskSerializer

class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
