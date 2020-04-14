from django.urls import path, include
from projects import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('Rapi-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.ProjectList.as_view()),
    path('<project_number>/', views.detail),

]
