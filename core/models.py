from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacao
from enderecos.models import Enderecos

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracoes)
    comentarios = models.ManyToManyField(Comentarios)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(Enderecos, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)

    def __sts__(self):
        return self.nome