import debug_toolbar
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from brands.views import BrandViewSet
from elements.views import ElementViewSet
from projects.views import ProjectViewSet
from account.views import UserViewSet
from materials.views import MaterialViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('brands', BrandViewSet)
router.register(r'elements',ElementViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'users', UserViewSet)
router.register('materials', MaterialViewSet)
urlpatterns = router.urls
urlpatterns = [
    # path('api/brand/', include('brands.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token/', include('djoser.urls.authtoken')),
    path('api-userinfo/', include('account.urls')),
    path('api/', include(router.urls)),

    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS

    # url(r'vue-element-admin/user/', include('account.urls')),

    # path('materials/', include('materials.urls')),
    # path('projects/', include('projects.urls')),
    # path('excel/', include('excel.urls')),
    # path('modules/', include('modules.urls')),
    # # path('', ProjectList.as_view(), name='index'),

    # path('brands/', include('brands.urls'))
    # path('vue-element-admin/user/', include('user.urls'))
]
