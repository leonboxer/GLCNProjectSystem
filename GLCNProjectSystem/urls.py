from django.conf.urls import include
from django.urls import path
# from projects import views
from projects.views import ProjectList
from django.contrib import admin
from rest_framework import routers
from projects import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-projects/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('materials/', include('materials.urls')),
    path('projects/', include('projects.urls')),
    path('modules/', include('modules.urls')),
    path('', ProjectList.as_view(), name='index'),
    path('account/', include('account.urls')),
]
