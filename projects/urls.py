from django.urls import path

from projects import views

urlpatterns = [
    path('list', views.ProjectList.as_view()),
    path('<int:project_id>/', views.detail)
]
