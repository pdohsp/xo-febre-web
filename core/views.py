from django.shortcuts import render, redirect
from .models import Pessoa, Consulta

from .forms import PessoaForm, ConsultaForm

# função que retorna as páginas home,consultae sobre
def home(request):
    form = PessoaForm()
    formularioPessoa = {'form':form}
    return render(request, 'core/home.html', formularioPessoa)

def consulta(request):
    form = ConsultaForm()
    formularioConsulta = {'form':form}
    return render(request, 'core/consulta.html', formularioConsulta)

def sobre(request):
    return render(request, 'core/sobre.html')
#---------------------------------------------------------

# função que cadastra pessoas no banco de dados
def cadastrarPessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_consulta')

# função que cadastra as consultas no banco de dados
def cadastrarConsulta(request):
    form = ConsultaForm(request.POST or None)

    mutable = request.POST._mutable
    request.POST._mutable = True
    
    if request.POST.get('temperatura') >= '36' and request.POST.get('temperatura') <= '37.2':
        request.POST['diagnostico'] = 'Temperatura normal!'
    
    elif request.POST.get('temperatura') >= '37.3' and request.POST.get('temperatura') <= '37.8':
            request.POST['diagnostico'] = 'Você está apenas com uma febrícula, tome um antitérmico!'

    elif request.POST.get('temperatura') < '40.3':
        
        if request.POST.get('dias') <= '1':
            
            if request.POST.get('coriza') == True:
                request.POST['diagnostico'] = 'Você pode estar com febre em decorrência de uma virose ou gripe. Tome um antitérmico, beba bastante líquido e repouse!'
            
            else:
                request.POST['diagnostico'] = 'Você pode estar com febre em decorrência de uma inflamação, siga para o pronto socorro mais próximo!'
        
        else:
            request.POST['diagnostico'] = 'Siga para o pronto socorro mais próximo imediatamente!'

    else:
        request.POST['diagnostico'] = 'Siga para o pronto socorro mais próximo imediatamente!'

    request.POST._mutable = mutable

    if form.is_valid():
        form.save()
        return redirect('core_listaConsulta')
#--------------------------------------------------------------

# função que retorna as pessoas cadastradas no banco de dados
def listaPessoas(request):
    pessoas = Pessoa.objects.all()
    listaResponse = {'pessoas':pessoas}
    return render(request, 'core/listaPessoas.html', listaResponse)

#função que retorna as consultas cadastradas no banco de dados
def listaConsulta(request):
    consulta = Consulta.objects.all()
    return render(request, 'core/listaConsulta.html', {'consulta':consulta})
#-------------------------------------------------------------------------------

# função que deleta os registros do bancode dados
def deletarPessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect('core_listaPessoas')

def deletarConsulta(request, id):
    consulta = Consulta.objects.get(id=id)
    consulta.delete()
    # o retorno da função que redireciona novamente para página 
    return redirect('core_listaConsulta')
#-------------------------------------------------------------------------------