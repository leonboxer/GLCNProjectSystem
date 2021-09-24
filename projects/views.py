from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from .models import Project
from .serializers import ProjectSerializer
from projects.forms import ProjectModelForm
from rest_framework import viewsets, permissions

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created')
    serializer_class = ProjectSerializer
    filter_fields = ('project_number',)
    ordering_fields = ['id', 'project_number']
    #
    # # @method_decorator(vary_on_cookie)
    # # @method_decorator(cache_page(60 * 0.1))
    # def dispatch(self, *args, **kwargs):
    #     return super(ProjectViewSet, self).dispatch(*args, **kwargs)


#
class ProjectList(generic.ListView):
    queryset = Project.objects.all()
    # serializer_class = ProjectSerializer


# def home(request):
#     project_list = Project.objects.all()
#     context = {'project_list': project_list}
#     return render(request, 'list.html', context)
#
#
# def list(request):
#     project_list = Project.objects.all()
#     context = {'project_list': project_list}
#     return render(request, 'list.html', context)
#
#
def detail(request, project_number):
    # target_project = Project.objects.get(id=project_id)
    selected_project = Project.objects.get(project_number=project_number)
    if request.method == 'POST':
        form = ProjectModelForm(request)
    else:
        form = ProjectModelForm()
    context = {'selected_project': selected_project, 'form': form}
    return render(request, 'projects/detail.html', context)
