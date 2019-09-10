from django.shortcuts import render
from django.views import generic
from .models import Brand


# Create your views here.

class BrandList(generic.ListView):
    model = Brand
