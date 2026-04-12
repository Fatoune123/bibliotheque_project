from django.contrib import admin
from .models import Auteur, Livre, Tag, Emprunt, ProfilLecteur

admin.site.register(Auteur)
admin.site.register(Livre)
admin.site.register(Tag)
admin.site.register(Emprunt)
admin.site.register(ProfilLecteur)