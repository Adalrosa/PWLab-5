from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular

admin.site.register(Licenciatura)
admin.site.register(UnidadeCurricular)
from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular, Projecto  # Adiciona o Projecto aqui

admin.site.register(Licenciatura)
admin.site.register(UnidadeCurricular)
admin.site.register(Projecto)  