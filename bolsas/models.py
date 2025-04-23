from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Universidade(models.Model):
    nome = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logos/")
    slug = models.SlugField(unique=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Bolsa(models.Model):


    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    curso = models.CharField(max_length=150)
    descricao = models.TextField()
    valor_original = models.DecimalField(max_digits=10, decimal_places=2)
    valor_com_bolsa = models.DecimalField(max_digits=10, decimal_places=2)
    link_inscricao = models.URLField()
    data_limite = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    visualizacoes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.curso} - {self.universidade.nome}"
    
# Create your models here.
