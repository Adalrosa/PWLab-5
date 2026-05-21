from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from django.db.models import Count  
from .models import Projecto, Competencia, Interesse, UnidadeCurricular, Tecnologia, MakingOf, Licenciatura, TFC, Formacao

# Definição dos formulários
ProjectoForm = modelform_factory(Projecto, fields='__all__')
InteresseForm = modelform_factory(Interesse, fields='__all__')

# --- Views da Home ---
def home_page_view(request):
    context = {
        'projectos': Projecto.objects.all(),
        'competencias': Competencia.objects.all(),
        'interesses': Interesse.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)

# --- Views de Projetos ---
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

def projectos_list_view(request):
    projectos = Projecto.objects.all()
    return render(request, 'portfolio/projectos.html', {'projectos': projectos})

def detalhe_projecto_view(request, projecto_id):
    projecto = get_object_or_404(Projecto, id=projecto_id)
    return render(request, 'portfolio/projecto_detail.html', {'projecto': projecto})

# --- Views de Interesses ---
def interesses_view(request):
    interesses = Interesse.objects.annotate(num_projetos=Count('projetos')).order_by('-num_projetos')
    interesse_preferido = Interesse.objects.filter(e_preferido=True).first()
    context = {
        'interesses': interesses,
        'interesse_preferido': interesse_preferido
    }
    return render(request, 'portfolio/interesses.html', context)

def detalhe_interesse_view(request, interesse_id):
    interesse = get_object_or_404(Interesse, id=interesse_id)
    return render(request, 'portfolio/interesse_detail.html', {'interesse': interesse})

def editar_interesse_view(request, interesse_id=None):
    if interesse_id:
        interesse = get_object_or_404(Interesse, id=interesse_id)
    else:
        interesse = None
    form = InteresseForm(request.POST or None, request.FILES or None, instance=interesse)
    if form.is_valid():
        form.save()
        return redirect('portfolio:interesses')
    return render(request, 'portfolio/object_form.html', {'form': form})

def sobre_view(request):
    return render(request, 'portfolio/sobre.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from django.db.models import Count  
from .models import Projecto, Competencia, Interesse

# Definição dos formulários
ProjectoForm = modelform_factory(Projecto, fields='__all__')
InteresseForm = modelform_factory(Interesse, fields='__all__')

# --- Views da Home ---
def home_page_view(request):
    context = {
        'projectos': Projecto.objects.all(),
        'competencias': Competencia.objects.all(),
        'interesses': Interesse.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)

# --- Views de Projetos ---
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

def projectos_list_view(request):
    projectos = Projecto.objects.all()
    return render(request, 'portfolio/projectos.html', {'projectos': projectos})

def detalhe_projecto_view(request, projecto_id):
    projecto = get_object_or_404(Projecto, id=projecto_id)
    return render(request, 'portfolio/projecto_detail.html', {'projecto': projecto})

# --- Views de Interesses ---
def interesses_view(request):
    interesses = Interesse.objects.annotate(num_projetos=Count('projetos')).order_by('-num_projetos')
    interesse_preferido = Interesse.objects.filter(e_preferido=True).first()
    context = {
        'interesses': interesses,
        'interesse_preferido': interesse_preferido
    }
    return render(request, 'portfolio/interesses.html', context)

def detalhe_interesse_view(request, interesse_id):
    interesse = get_object_or_404(Interesse, id=interesse_id)
    return render(request, 'portfolio/interesse_detail.html', {'interesse': interesse})

def editar_interesse_view(request, interesse_id=None):
    if interesse_id:
        interesse = get_object_or_404(Interesse, id=interesse_id)
    else:
        interesse = None
    form = InteresseForm(request.POST or None, request.FILES or None, instance=interesse)
    if form.is_valid():
        form.save()
        return redirect('portfolio:interesses')
    return render(request, 'portfolio/object_form.html', {'form': form})

# --- Views de Páginas Estáticas e Extras ---
def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def sobre_view(request):
    return render(request, 'portfolio/sobre.html')

def tecnologias_view(request):
    return render(request, 'portfolio/tecnologias.html')

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all().order_by('-nivel_interesse')
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})  
    
def makingof_view(request):

    registos = MakingOf.objects.all().order_by('-data')
    return render(request, 'portfolio/makingof.html', {'makingof_list': registos})      