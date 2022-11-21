from rest_framework.generics import ListAPIView
from .models import Task
from .serializers import TaskSerializer

class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
