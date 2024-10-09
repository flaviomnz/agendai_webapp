from django.shortcuts import render, redirect
from .models import Agendamento, Horario, DiaDisponivel
from .forms import AgendamentoForm, DiaDisponivelForm
def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendar')
    else:
        form = AgendamentoForm()

    dias_disponiveis = DiaDisponivel.objects.all()
    return render(request, 'agendamentos/agendar.html', {
        'form': form,
        'dias_disponiveis': dias_disponiveis,
        'horarios': Horario.objects.all(),
    })

def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos/listar_agendamentos.html', {'agendamentos': agendamentos})

def adicionar_dia_disponivel(request):
    if request.method == 'POST':
        form = DiaDisponivelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adicionar_dia_disponivel')  # Redirecione para a mesma página ou outra
    else:
        form = DiaDisponivelForm()
    
    dias_disponiveis = DiaDisponivel.objects.all()  # Para exibir dias já cadastrados
    return render(request, 'agendamentos/adicionar_dia.html', {'form': form, 'dias_disponiveis': dias_disponiveis})
