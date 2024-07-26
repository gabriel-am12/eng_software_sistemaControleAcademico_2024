from django import forms
from .models import Estudante, Disciplina, Professor

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = '__all__'

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
