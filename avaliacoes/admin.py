from django.contrib import admin
from .models import Avaliacao

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('user', 'comentario', 'nota', 'data')

admin.site.register(Avaliacao, AvaliacaoAdmin)