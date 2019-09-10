from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list, name='material_list'),
    path('<pk>', views.MaterialDetail.as_view(), name='material_detail'),
]
