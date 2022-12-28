from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from todo.views import TodoItemCRUDViewSet

router = DefaultRouter()
router.register(r'todos',TodoItemCRUDViewSet, basename='todo')
urlpatterns = router.urls