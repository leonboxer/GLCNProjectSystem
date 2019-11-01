from django.conf.urls import include
from django.urls import path
# from projects import views
from projects.views import ProjectList
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materials/', include('materials.urls')),
    path('projects/', include('projects.urls')),
    path('modules/', include('modules.urls')),
    path('', ProjectList.as_view(), name='index'),
]
