from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_obraczek, name='lista_obraczek'),
    path('dodaj/', views.dodaj_obraczke, name='dodaj_obraczke'),
    path('usun/<int:pk>/', views.usun_obraczke, name='usun_obraczke'),
    path('edytuj/<int:pk>/', views.edytuj_obraczke, name='edytuj_obraczke'),
]