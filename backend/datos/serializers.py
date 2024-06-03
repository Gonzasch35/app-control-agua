from rest_framework import serializers
from .models import Medidor, Loteo

class LoteoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loteo
        fields = '__all__'

class MedidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = '__all__'