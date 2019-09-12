from django import forms


class ProjectForm(forms.Form):
    project_number = forms.CharField(max_length=100)
