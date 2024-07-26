from django.shortcuts import render, redirect
from .models import Estudante, Disciplina, Professor
from .forms import EstudanteForm, DisciplinaForm, ProfessorForm

def home(request):
    return render(request, 'core/home.html')

def listar_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'core/listar_estudantes.html', {'estudantes': estudantes})

def adicionar_estudante(request):
    if request.method == 'POST':
        form = EstudanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudantes')
    else:
        form = EstudanteForm()
    return render(request, 'core/adicionar_estudante.html', {'form': form})

def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'core/listar_disciplinas.html', {'disciplinas': disciplinas})

def adicionar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_disciplinas')
    else:
        form = DisciplinaForm()
    return render(request, 'core/adicionar_disciplina.html', {'form': form})

def listar_professores(request):
    professores = Professor.objects.all()
    return render(request, 'core/listar_professores.html', {'professores': professores})

def adicionar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_professores')
    else:
        form = ProfessorForm()
    return render(request, 'core/adicionar_professor.html', {'form': form})
