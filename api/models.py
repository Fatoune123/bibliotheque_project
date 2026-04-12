from django.db import models
from django.contrib.auth.models import User


class Auteur(models.Model):
    nom = models.CharField(max_length=200)
    biographie = models.TextField(blank=True, null=True)
    nationalite = models.CharField(max_length=100, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom


class Livre(models.Model):
    CATEGORIES = [
        ('roman', 'Roman'),
        ('essai', 'Essai'),
        ('poesie', 'Poésie'),
        ('bd', 'BD'),
        ('science', 'Science'),
    ]

    titre = models.CharField(max_length=300)

    # ✅ ISBN simplifié (évite erreur "invalide")
    isbn = models.CharField(max_length=17, unique=True)

    annee_publication = models.IntegerField()

    categorie = models.CharField(max_length=20, choices=CATEGORIES)

    auteur = models.ForeignKey(
        Auteur,
        on_delete=models.CASCADE,
        related_name='livres'
    )

    tags = models.ManyToManyField(Tag, blank=True)

    disponible = models.BooleanField(default=True)

    cree_par = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Emprunt(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

    date_emprunt = models.DateField(auto_now_add=True)
    date_retour_prevue = models.DateField()

    rendu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.livre.titre}"


class ProfilLecteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    date_naissance = models.DateField()

    livres_favoris = models.ManyToManyField(Livre, blank=True)

    def __str__(self):
        return self.user.username