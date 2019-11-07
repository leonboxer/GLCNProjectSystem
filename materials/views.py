import csv, io
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Material
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from tablib import Dataset
from .resources import MaterialResource


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


@permission_required('admin.can_add_log_entry')
def material_upload(request):
    template = "materials/material_upload.html"
    prompt = {
        'order': 'order fo the CSV should be'
    }
    if request.method == 'GET':
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Material.objects.update_or_create(
            order_number=column[0],
            type=column[1],
            brand=column[2],
            created_time=column[3],
            update_time=column[4]
        )
    context = {}
    return render(request, template, context)


def simple_upload(request):
    if request.method == 'POST':
        tag_resource = MaterialResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = tag_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            tag_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'materials/material_upload.html')
