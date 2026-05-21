from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField(default=6)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    link_docente_lusofona = models.URLField(blank=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    acronymo = models.CharField(max_length=10, blank=True)
    logotipo = models.ImageField(upload_to='Tecnologias/', blank=True, null=True)
    link_website = models.URLField(blank=True)
    nivel_interesse = models.IntegerField(default=1, help_text="Escala de 1 a 5")
    relevancia = models.TextField(blank=True) 

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
    tecnologias = models.ManyToManyField(Tecnologia)
    
    def __str__(self):
        return self.titulo

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=200) 
    ano = models.IntegerField()
    resumo = models.TextField()
    imagem = models.ImageField(upload_to='tfc/', blank=True, null=True)
    link_relatorio = models.URLField(blank=True)
    link_github = models.URLField(blank=True)
    video_demo = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    logotipo = models.ImageField(upload_to='competencias/', blank=True, null=True)
    projetos = models.ManyToManyField(Projecto, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.nome

class Formacao(models.Model): 
    titulo = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    ano_inicio = models.IntegerField()
    ano_fim = models.IntegerField(blank=True, null=True) 
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class MakingOf(models.Model):
    data = models.DateField()
    etapa = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='makingof/', blank=True, null=True)
    decisao = models.TextField(blank=True)
    uso_ia = models.TextField(blank=True)

    def __str__(self):
        return f"{self.data} - {self.etapa}"

class Interesse(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Interesse")
    descricao = models.TextField(verbose_name="Descrição", default="")
    icone = models.ImageField(upload_to='interesses/', blank=True, null=True)
    
    # As novas relações que o exercício pede
    projetos = models.ManyToManyField(Projecto, blank=True)
    disciplinas = models.ManyToManyField(UnidadeCurricular, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    
    # Campo para identificar a área preferida (Ponto 4.4 do exercício)
    e_preferido = models.BooleanField(default=False, verbose_name="É a área preferida?")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Interesse"
        verbose_name_plural = "Interesses"