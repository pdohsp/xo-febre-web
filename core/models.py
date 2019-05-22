# import
from django.db import models
from django.db.models import fields_all


# Definição da classe pessoa
class Pessoa(models.Model):
    objects = models.Manager()
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__ (self):
        return self.nome
    
# Definição da classe consulta
class Consulta(models.Model):
    objects = models.Manager()
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    dataHora = models.DateTimeField(auto_now=True)
    temperatura = models.DecimalField(decimal_places=1, max_digits=3)
    dias = models.IntegerField()
    coriza = models.BooleanField()
    diagnostico = models.CharField(max_length=200, blank=True, null=False)

    def __str__ (self):
        return self.pessoa