from rest_framework import serializers
from .models import Medidor, Loteo

class MedidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = '__all__'


class LoteoSerializer(serializers.ModelSerializer):
    medidores = MedidorSerializer(many=True, read_only=True, source='medidor_loteo')

    class Meta:
        model = Loteo
        fields = '__all__'
