from rest_framework.serializers import ModelSerializer
from enderecos.models import Enderecos

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Enderecos
        fields = ('id', 'logradouro', 'complemento', 'bairro', 'cidade', 'estado', 'pais', 'latitude', 'longitude')