from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('projecto/<int:projecto_id>/editar/', views.editar_projecto_view, name='editar_projecto'),
    path('projecto/<int:projecto_id>/apagar/', views.apagar_projecto_view, name='apagar_projecto'),
]
