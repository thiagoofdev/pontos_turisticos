from rest_framework import fields
from comentarios.models import Comentarios
from rest_framework.serializers import ModelSerializer

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ('id', 'usuario', 'comentarios', 'data', 'aprovado')
