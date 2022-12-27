from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo.views import TodoItemList, TodoItemDetail


urlpatterns = [
    path('todos/', TodoItemList.as_view()),
    path('todos/<int:pk>/',TodoItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)