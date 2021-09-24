from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    # path('info/', UserViewSet.as_view({'get': 'retrieve'})),

    path('info/', current_user),
    path('info/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    #     path('api-token-auth/', CustomAuthToken.as_view()),
    #     # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #     path('', include('rest_framework.urls')),#login logout
    #     path('', include(router.urls))
    path('register/', UserRegister.as_view())
]
