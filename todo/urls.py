from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

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
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += router.urls
