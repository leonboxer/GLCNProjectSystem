from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

'''class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


def list(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'list.html', context)'''


@api_view(['GET', 'POST'])
def product_list(request):
    """
    List  products, or create a new product.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        products = Project.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ProjectSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages,
                         'nextlink': '/api/products/?page=' + str(nextPage),
                         'prevlink': '/api/products/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def detail(request, project_id):
    # target_project = Project.objects.get(id=project_id)
    selected_project = Project.objects.get(id=project_id)
    context = {'selected_project': selected_project}
    return render(request, 'detail.html', context)
