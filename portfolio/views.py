from django.shortcuts import render
from .models import Projecto, Competencia

# Verifica se o nome aqui é EXATAMENTE igual a home_page_view
def home_page_view(request):
    context = {
        'projetos': Projecto.objects.all(),
        'competencias': Competencia.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)