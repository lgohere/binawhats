from django.urls import path
from . import views

app_name = 'recebezap'

urlpatterns = [
    path('', views.recebezap, name='recebezap'),
]
