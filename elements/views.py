from django.shortcuts import render
from django.views import generic
from .models import Element


class ElementDetail(generic.DetailView):
    model = Element
    template_name = 'elements/element_detail.html'
