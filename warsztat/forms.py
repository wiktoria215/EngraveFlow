from django import forms
from .models import Obraczka

class ObraczkaForm(forms.ModelForm):
    class Meta:
        model = Obraczka
        fields = '__all__'