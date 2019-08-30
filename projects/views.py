from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import generics


# Create your views here.

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


def list(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'list.html', context)


def detail(request, project_id):
    # target_project = Project.objects.get(id=project_id)
    selected_project = Project.objects.get(id=project_id)
    context = {'selected_project': selected_project}
    return render(request, 'detail.html', context)
