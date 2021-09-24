import csv, io
from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Material
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from tablib import Dataset

# from django.http import  HttpResponse
from .serializers import MaterialSerializer


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    ordering_fields = ('id', 'material_number', 'order_number', 'brand')
    search_fields = ('material_number', 'order_number')

    def get_queryset(self):
        queryset = Material.objects.all()
        brandname = self.request.query_params.get('brand_name')
        if brandname is not None:
            queryset = queryset.filter(brand__brand_name=brandname)
        return queryset


class MaterialDetail(generic.DetailView):
    model = Material
    template_name = 'materials/material_detail.html'


def list(request):
    material_list = Material.objects.all()
    context = {'material_list': material_list}
    return render(request, 'list.html', context)
