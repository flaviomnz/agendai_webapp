# agendamentos/forms.py

from django import forms
from .models import Agendamento, DiaDisponivel

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'horario']  # Os campos que você deseja incluir no formulário
        widgets = {
            'data': forms.SelectDateWidget(),  # Para um seletor de data
        }
        
class DiaDisponivelForm(forms.ModelForm):
    class Meta:
        model = DiaDisponivel
        fields = ['data']


