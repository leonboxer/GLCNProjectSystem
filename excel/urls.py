from django.urls import path

from .views import *

app_name = 'excel'  # 设置命名空间

urlpatterns = [

    path('test_django_excel_upload', TestDjangoExcelUpload.as_view(), name='test_django_excel_upload'),

    path('test_django_excel_download', TestDjangoExcelDownload.as_view(), name='test_django_excel_download'),
]