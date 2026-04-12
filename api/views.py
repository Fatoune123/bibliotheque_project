from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Auteur, Livre, Emprunt
from .serializers import (
    AuteurSerializer,
    LivreSerializer,
    LivreDetailSerializer,
    EmpruntSerializer
)
from .permissions import EstProprietaireOuReadOnly
from .filters import LivreFilter
from .pagination import StandardPagination
class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nom', 'prenom']
    ordering_fields = ['nom', 'prenom']
class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = [EstProprietaireOuReadOnly]
    pagination_class = StandardPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LivreFilter

    search_fields = ['titre', 'auteur__nom']
    ordering_fields = ['titre', 'date_publication']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LivreDetailSerializer
        return LivreSerializer

    def perform_create(self, serializer):
        serializer.save(proprietaire=self.request.user)

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['livre__titre', 'utilisateur__username']
    ordering_fields = ['date_emprunt', 'date_retour']

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)