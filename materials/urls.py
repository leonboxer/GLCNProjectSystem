from django.urls import path
from . import views

urlpatterns = [
    path('', views.detail, name='material_detail'),
    path('list', views.list, name='material_list')
]
