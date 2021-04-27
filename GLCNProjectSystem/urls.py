from django.conf.urls import include, url
from django.urls import path
# from projects import views
# from projects.views import ProjectList
from django.contrib import admin
from rest_framework import routers
from projects import views
# from account.views import  UserViewSet

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
# router.register(r'vue-element-admin/user', UserViewSet, basename='info')
urlpatterns = [
    url(r'auth/', include('djoser.urls')),
    url(r'auth/', include('djoser.urls.authtoken')),
    url(r'vue-element-admin/user/', include('account.urls')),
    # path('', include(router.urls)),
    # path('api-projects/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # path('materials/', include('materials.urls')),
    # path('projects/', include('projects.urls')),
    # path('modules/', include('modules.urls')),
    # # path('', ProjectList.as_view(), name='index'),
    # path('account/', include('account.urls')),
    # path('vue-element-admin/user/', include('user.urls'))
]
