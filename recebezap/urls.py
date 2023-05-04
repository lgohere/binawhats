from django.urls import path
from . import views

app_name = 'recebezap'

urlpatterns = [
    path('', views.recebezap, name='recebezap'),
    path('lista_chamadas/', views.lista_chamadas, name='lista_chamadas'),
    path('novas_chamadas/', views.novas_chamadas, name='novas_chamadas'),

    # path('', views.recebezap, name='novas_ligacoes'),
]
