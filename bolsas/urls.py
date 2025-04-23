from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_bolsas, name='lista_bolsas'),
    path('painel/', views.painel, name='painel'),
    path('universidade/<slug:slug>/', views.pagina_universidade, name='pagina_universidade'),
]
