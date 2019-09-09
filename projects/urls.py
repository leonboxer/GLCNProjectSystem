from django.urls import path
from projects import views

urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('<project_number>/', views.detail)
]
