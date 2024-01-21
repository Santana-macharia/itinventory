from django import forms
from .models import Import

class ImportForm(forms.ModelForm):
    file = forms.FileField(label='Select a CSV file')

    class Meta:
        model = Import
        fields = ['file']

        

  # or specify the fields you want to include
    
    








   
