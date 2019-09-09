from django.shortcuts import render
from rest_framework import generics
from .models import Module
from django.views import generic


# Create your views here.
class ModuleList(generic.ListView):
    queryset = Module.objects.all()


class ModuleDetail(generic.DetailView):
    model = Module
    template_name = 'detail.html'
    # queryset = Module.objects.get(id=module_id)


def detail(request, module_id):
    # target_project = Project.objects.get(id=project_id)
    selected_project = Module.objects.get(id=module_id)
    context = {'selected_project': selected_project}
    return render(request, 'detail.html', context)
