# agendamentos/forms.py

from django import forms
from .models import Agendamento, DiaDisponivel

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'data', 'horario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Isso garante que o campo será exibido como um seletor de data
        }
        
class DiaDisponivelForm(forms.ModelForm):
    class Meta:
        model = DiaDisponivel
        fields = ['data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Isso garante que o campo será exibido como um seletor de data
        }


