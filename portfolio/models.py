from django.db import models

class Licenciatura(models.Model):
 nome=models.CharField(max_length=100)
 apresentação=models.TextField()

class UnidadeCurricular(models.Model):
 nome= models.CharField(max_length=100)
 ano=models.IntegerField()
 licenciatura= models.ForeignKey(Licenciatura, on_delete=models.CASCADE)

class Projecto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
