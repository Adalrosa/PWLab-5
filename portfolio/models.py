from django.db import models

class Licenciatura(models.Model):
 nome=models.CharField(max_length=100)
 apresentacao=models.TextField()

 def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
 nome= models.CharField(max_length=100)
 ano=models.IntegerField()
 semestre=models.CharField(max_length=20)
 ects=models.IntegerField(default=6)
 imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
 link_docente_lusofona = models.URLField(blank=True)
 licenciatura= models.ForeignKey(Licenciatura, on_delete=models.CASCADE)

 def __str__(self):
    return self.nome

class Projecto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField(blank=True) 
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    link_github = models.URLField(blank=True)
    video_demo = models.URLField(blank=True)
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField('tecnologia')
    def __str__(self):
        return self.titulo

class tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    acronymo = models.CharField(max_length=10, blank=True)
    logotipo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    link_website = models.URLField(blank=True)
    def __str__(self):
        return self.nome