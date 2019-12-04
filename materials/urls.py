from django.urls import path
from .views import list, MaterialDetail

urlpatterns = [
    path('list/', list, name='material_list'),
    path('<pk>/', MaterialDetail.as_view(), name='material_detail')

]
