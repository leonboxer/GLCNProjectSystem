from django.shortcuts import render
from rest_framework import filters
from rest_framework.response import Response
from django.utils import timezone
from django.views import generic
from rest_framework import generics

from rest_framework.viewsets import ModelViewSet

from .serializers import BrandSerializer
from .forms import BrandAddForm
from .models import Brand
from rest_framework.filters import OrderingFilter


# Create your views here.
class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    ordering_fields = ('id', 'brand_name', 'description')
    search_fields = ('brand_name', 'description')

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Brand.objects.all()
        brandname = self.request.query_params.get('brand_name')
        if brandname is not None:
            queryset = queryset.filter(brand_name=brandname)
        return queryset


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['id']


class BrandList(generic.ListView):
    model = Brand


class BrandDetail(generic.DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AddBrand(generic.CreateView):
    template_name = 'brands/add.html'
    form_class = BrandAddForm
