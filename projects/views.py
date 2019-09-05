from django.shortcuts import render
from django.views import generic
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import generics, status
from rest_framework.response import responses


# Create your views here.

class ProjectList(generic.ListView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


def home(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'list.html', context)


def list(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'list.html', context)


def detail(request, project_id):
    # target_project = Project.objects.get(id=project_id)
    selected_project = Project.objects.get(id=project_id)
    context = {'selected_project': selected_project}
    return render(request, 'detail.html', context)
