from django.urls import path
from .views import list, MaterialDetail, material_upload

urlpatterns = [
    path('list/', list, name='material_list'),
    path('upload-csv/', material_upload, name='contact_upload'),
    path('<pk>/', MaterialDetail.as_view(), name='material_detail')

]
