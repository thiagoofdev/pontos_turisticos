from django.contrib import admin
from .models import Comentarios

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'comentarios', 'data', 'aprovado')


admin.site.register(Comentarios, ComentariosAdmin)
