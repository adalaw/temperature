from django import forms
from .models import *

class NewDataForm(forms.ModelForm):
    class Meta:
        model = Temperature
        fields = '__all__'

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ['file',]