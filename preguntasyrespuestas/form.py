from django import forms
from preguntasyrespuestas.models import Pregunta

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta

