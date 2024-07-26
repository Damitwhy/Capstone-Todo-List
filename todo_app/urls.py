from django.urls import path
from django.contrib import admin
from .views import TaskList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskList.as_view(), name='tasks'),
]