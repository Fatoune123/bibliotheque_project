from django.shortcuts import render
from .models import Produit

def accueil(request):
    """Page d'accueil de la boutique"""
    produits_populaires = Produit.objects.all()[:4]  # 4 premiers produits
    return render(request, 'boutique/accueil.html', {
        'produits_populaires': produits_populaires
    })

def liste_produits(request):
    """Page de tous les produits"""
    produits = Produit.objects.all()
    return render(request, 'boutique/produits.html', {'produits': produits})

def contact(request):
    """Page de contact"""
    return render(request, 'boutique/contact.html')