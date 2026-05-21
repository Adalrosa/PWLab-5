from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('projecto/<int:projecto_id>/editar/', views.editar_projecto_view, name='editar_projecto'),
    path('projecto/<int:projecto_id>/apagar/', views.apagar_projecto_view, name='apagar_projecto'),
    path('interesses/', views.interesses_view, name='interesses'),
    path('interesses/<int:interesse_id>/', views.detalhe_interesse_view, name='detalhe_interesse'),
    path('interesses/novo/', views.editar_interesse_view, name='novo_interesse'),
    path('interesses/<int:interesse_id>/editar/', views.editar_interesse_view, name='editar_interesse'),
    path('projectos/', views.projectos_list_view, name='projectos'),
    path('projecto/<int:projecto_id>/', views.detalhe_projecto_view, name='detalhe_projecto'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('makingof/', views.makingof_view, name='makingof'),
    path('ucs/', views.ucs_view, name='ucs'),

]