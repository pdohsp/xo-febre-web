from django.conf.urls import url, include
from .views import (
    home,
    cadastrarPessoa,
    listaPessoas,
    consulta,
    cadastrarConsulta,
    listaConsulta,
    deletarPessoa,
    deletarConsulta,
    sobre
)
    
#lista de urls que fazem parte da app core
urlpatterns = [
    url('^$', home, name='core_home'),
    url('^cadastrarPessoa/$', cadastrarPessoa, name='core_cadastrarPessoa'),
    url('^listaPessoas/$', listaPessoas, name='core_listaPessoas'),
    url('^deletarPessoa/(?P<id>[0-9]+)/$', deletarPessoa, name='core_deletarPessoa'),

    url('^consulta/$', consulta, name='core_consulta'),
    url('^cadastrarConsulta/$', cadastrarConsulta, name='core_cadastrarConsulta'),
    url('^listaConsulta/$', listaConsulta, name='core_listaConsulta'),
    url('^deletarConsulta/(?P<id>[0-9]+)/$', deletarConsulta, name='core_deletarConsulta'),

    url('^sobre/$', sobre, name='core_sobre'),
]
