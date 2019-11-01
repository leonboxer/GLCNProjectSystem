from django import forms
from django.forms import ModelForm
from .models import Project


class ProjectForm(forms.Form):
    project_number = forms.CharField(label='project number', max_length=100)


class ProjectModelForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_number', 'machinery_type']
