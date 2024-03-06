from django import forms

from app.models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model = PolicyData
        fields = ['slug','geeks_field','active']
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'geeks_field': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'slug' : 'Enter Name:',
            'geeks_field': 'Enter a Content: ',
            'active': "Use thsi template"
        }