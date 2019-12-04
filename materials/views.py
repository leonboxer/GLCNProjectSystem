import csv, io
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Material
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from tablib import Dataset


# from django.http import  HttpResponse
class MaterialDetail(generic.DetailView):
    model = Material
    template_name = 'materials/material_detail.html'


# Create your views here.
def detail(request, material_id):
    return HttpResponse("You are looking at material %s" % material_id)


def list(request):
    material_list = Material.objects.all()
    context = {'material_list': material_list}
    return render(request, 'list.html', context)





