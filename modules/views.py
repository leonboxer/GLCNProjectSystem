from django.shortcuts import render
from rest_framework import generics
from .models import Module


# Create your views here.
class list(generics.ListCreateAPIView):
    queryset = Module.objects.all()
