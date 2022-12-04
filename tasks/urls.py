from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tasks.views import TaskList


urlpatterns = [
    path('tasks/', TaskList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)