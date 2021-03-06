from django import forms
from .models import *

''' MISUNDERSTANDING
class NewDataForm(forms.ModelForm):
    class Meta:
        model = Temperature
        fields = ['x', 'y', 'temperature']

class RemoveDataForm(forms.Form):
    x_value = forms.CharField(label='X', max_length=200, required=True)
    y_value = forms.CharField(label='Y', max_length=200, required=True)

'''

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ['file',]