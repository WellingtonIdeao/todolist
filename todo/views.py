from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from todo.filters import IsOwnerFilterBackend
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer


class TodoItemCRUDViewSet(ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [IsOwnerFilterBackend]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
