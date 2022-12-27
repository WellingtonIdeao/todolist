from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo.views import TodoItemCRUDViewSet

urlpatterns = [
    path('todos/', TodoItemCRUDViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('todos/<int:pk>/', TodoItemCRUDViewSet.as_view(
        {'get': 'retrieve', 'put': 'update','patch': 'partial_update', 'delete': 'destroy'}))
]

urlpatterns = format_suffix_patterns(urlpatterns)