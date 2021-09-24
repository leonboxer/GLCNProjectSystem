from django import forms
from .models import Brand


class BrandAddForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
