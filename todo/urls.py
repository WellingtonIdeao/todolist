from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from todo.views import TodoItemCRUDViewSet

router = DefaultRouter()
router.register(r'todos', TodoItemCRUDViewSet, basename='todo')

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='scheme'),
    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='scheme'),
        name='swagger-ui',
    ),
]
urlpatterns += router.urls
