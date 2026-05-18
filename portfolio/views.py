from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from .models import Projecto, Competencia, Interesse

# O Django gera o ProjectoForm automaticamente com base no teu Modelo
ProjectoForm = modelform_factory(Projecto, fields='__all__')

def home_page_view(request):
    context = {
        'projectos': Projecto.objects.all(),
        'competencias': Competencia.objects.all(),
        'interesses': Interesse.objects.all(),   # Mantemos apenas os interesses
    }
    return render(request, 'portfolio/home.html', context)


def forms_projecto_view(request):
    form = ProjectoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:home')
    return render(request, 'portfolio/forms.html', {'form': form})


def apagar_projecto_view(request, projecto_id):
    projecto = get_object_or_404(Projecto, id=projecto_id)
    projecto.delete()
    return redirect('portfolio:home')


def editar_projecto_view(request, projecto_id):
    projecto = get_object_or_404(Projecto, id=projecto_id)
    form = ProjectoForm(request.POST or None, request.FILES or None, instance=projecto)
    if form.is_valid():
        form.save()
        return redirect('portfolio:home')
    return render(request, 'portfolio/forms.html', {'form': form})