from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/project/', views.ProjectList.as_view())
    path('api-token-auth/', obtain_auth_token)
]