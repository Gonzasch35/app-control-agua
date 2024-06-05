from .models import Medidor, Loteo
from .serializers import MedidorSerializer, LoteoSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

class LoteoViewSet(viewsets.ModelViewSet):
    queryset = Loteo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LoteoSerializer

class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.select_related('loteo_name')
    permission_classes = [permissions.AllowAny]
    serializer_class = MedidorSerializer