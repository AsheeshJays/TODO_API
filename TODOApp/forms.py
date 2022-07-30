from dataclasses import fields
from django import forms
from .models import TODO

class TODOFORM(forms.ModelForm):
    class Meta:
        model = TODO
        fields = '__all__'

        widgets = {
            'item':forms.TextInput(attrs={'class':'form-control'}),
            
        }