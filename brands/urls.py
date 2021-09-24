from django.urls import path
from .views import AddBrand, BrandDetail, BrandListView

urlpatterns = [
    path('brand-list-view/',BrandListView.as_view(),name='brand-list')
]
