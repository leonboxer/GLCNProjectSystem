from django.shortcuts import render
from rest_framework import generics
from .models import Module
from django.views import generic


# Create your views here.
class ModuleList(generic.ListView):
    queryset = Module.objects.all()


class ModuleDetail(generic.DetailView):
    model = Module
    template_name = 'modules/module_detail.html'
    # queryset = Module.objects.get(id=module_id)
