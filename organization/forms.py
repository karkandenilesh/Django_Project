from django.forms import ModelForm
from .models import Organization
from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV File', widget=forms.FileInput(attrs={'accept': '.csv'}))


