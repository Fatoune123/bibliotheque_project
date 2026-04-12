from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('produits/', views.liste_produits, name='liste_produits'),
    path('contact/', views.contact, name='contact'),
]