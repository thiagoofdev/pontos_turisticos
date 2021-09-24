from django.contrib import admin
from .models import Atracoes

class AtracoesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'horario_func', 'idade_minima')

admin.site.register(Atracoes, AtracoesAdmin)