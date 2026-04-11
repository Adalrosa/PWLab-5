from django.db import models
class Licenciatura(models.Model):
 nome=models.CharField(max_length=100)
 apresentação=models.TextField()

class UnidadeCurricular(models.Model):
 nome= models.CharField(max_length=100)
 ano=models.IntegerField()
 licenciatura= models.ForeignKey(Licenciatura, on_delete=models.CASCADE)