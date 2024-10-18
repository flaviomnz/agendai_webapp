from django.shortcuts import render, redirect
from .models import Agendamento, Horario, DiaDisponivel, Servico
from .forms import AgendamentoForm, DiaDisponivelForm, ServicoForm


def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)  # Não salva ainda, pois vamos adicionar a data
            data_selecionada = request.POST.get('data')  # Captura a data do POST
            agendamento.data = data_selecionada  # Adiciona a data manualmente
            agendamento.save()  # Agora salva com a data
            return redirect('listar_agendamentos')  # Redireciona para a lista de agendamentos
    else:
        form = AgendamentoForm()

    dias_disponiveis = DiaDisponivel.objects.all()  # Para exibir os dias disponíveis
    horarios = Horario.objects.all()  # Exibe os horários disponíveis

    return render(request, 'agendamentos/agendar.html', {
        'form': form,
        'dias_disponiveis': dias_disponiveis,
        'horarios': horarios,
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
    
def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'agendamentos/listar_servicos.html', {'servicos': servicos})

def adicionar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_servicos')  # Redireciona para a lista de serviços
    else:
        form = ServicoForm()
    
    return render(request, 'agendamentos/adicionar_servico.html', {'form': form})

def editar_servico(request, pk):
    servico = Servico.objects.get(pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('listar_servicos')  # Redireciona para a lista de serviços
    else:
        form = ServicoForm(instance=servico)

    return render(request, 'agendamentos/editar_servico.html', {'form': form})
    