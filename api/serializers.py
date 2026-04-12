from rest_framework import serializers
from .models import Auteur, Livre, Tag, Emprunt, ProfilLecteur

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class LivreSerializer(serializers.ModelSerializer):
    auteur_nom = serializers.SerializerMethodField()

    class Meta:
        model = Livre
        fields = '__all__'

    def get_auteur_nom(self, obj):
        return obj.auteur.nom

    def validate_isbn(self, value):
        clean = value.replace('-', '')
        if not clean.isdigit() or len(clean) != 13:
            raise serializers.ValidationError("ISBN invalide")
        return value


class LivreDetailSerializer(serializers.ModelSerializer):
    auteur = AuteurSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Livre
        fields = '__all__'


class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = '__all__'


class ProfilLecteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilLecteur
        fields = '__all__'