from .models import Medidor, Loteo
from .serializers import MedidorSerializer, LoteoSerializer
from rest_framework import viewsets, permissions

class LoteoViewSet(viewsets.ModelViewSet):
    queryset = Loteo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LoteoSerializer

class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.select_related()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedidorSerializer