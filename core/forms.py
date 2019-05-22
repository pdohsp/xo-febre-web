from django.forms import ModelForm
from .models import Pessoa, Consulta

#Definição da classe PessoaForm que herda os atributos da classe pessoa
class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

#Definição da classe ConsultaForm que herda os atributos da classe consulta
class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'