from rest_framework.generics import ListAPIView
from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
