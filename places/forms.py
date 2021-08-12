from django import forms
from .models import Place, Feedback

class Placeform (forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'location', 'description']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('place', 'text')

