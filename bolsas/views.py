from django.shortcuts import render, get_object_or_404
from .models import Bolsa, Universidade
from django.contrib.auth.decorators import login_required

def lista_bolsas(request):
    bolsas = Bolsa.objects.all().order_by('-criado_em')
    return render(request, 'bolsas/lista_bolsas.html', {'bolsas': bolsas})

def pagina_universidade(request, slug):
    universidade = get_object_or_404(Universidade, slug=slug)
    bolsas = Bolsa.objects.filter(universidade=universidade)
    return render(request, 'bolsas/pagina_universidade.html', {
        'universidade': universidade,
        'bolsas': bolsas
    })

@login_required
def painel(request):
    universidade = get_object_or_404(Universidade, usuario=request.user)
    bolsas = Bolsa.objects.filter(universidade=universidade)
    return render(request, 'bolsas/painel.html', {'bolsas': bolsas})

# Create your views here.
