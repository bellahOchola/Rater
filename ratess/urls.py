from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/project/', views.ProjectList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('signup/', views.signup, name='signup' ),
    path('account/', include('django.contrib.auth.urls')),
    path('index/', views.index, name='index')
]