from django.urls import path
from . import views

urlpatterns = [
    path('<order_number>', views.MaterialDetail.as_view(), name='material_detail'),
    path('list', views.list, name='material_list')
]
