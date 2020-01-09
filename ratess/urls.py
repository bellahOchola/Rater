from django.urls import path, include
from . import views

urlpatterns = [
    path('api/project/', views.ProjectList.as_view())
]