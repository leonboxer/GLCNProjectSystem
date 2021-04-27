from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserViewSet, CustomAuthToken, UserInfo, GroupViewSet, UserDetail, current_user
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('info/', UserViewSet.as_view({'get': 'retrieve'})),
    path('info/', current_user),
    # path('info/<int:pk>/', UserDetail.as_view()),
    #     path('api-token-auth/', CustomAuthToken.as_view()),
    #     # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #     path('', include('rest_framework.urls')),#login logout
    #     path('', include(router.urls))
]
