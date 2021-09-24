from django.urls import path, include
from projects import views
from rest_framework import routers
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('', include(router.urls)),
    path('', views.ProjectList.as_view()),
    # path('<project_number>/', detail),
]
