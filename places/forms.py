from django import forms
from .models import Place

class Placeform (forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'location', 'description']
