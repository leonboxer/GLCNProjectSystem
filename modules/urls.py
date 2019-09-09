from django.urls import path
from modules import views

urlpatterns = [
    path('', views.ModuleList.as_view()),
    path('<pk>/', views.ModuleDetail.as_view(), name='module_detail')
]
