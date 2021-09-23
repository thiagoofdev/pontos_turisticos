from django.contrib import admin
from .models import Enderecos

class EnderecosAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'complemento', 'bairro', 'cidade', 'estado', 'pais', 'latitude', 'longitude')

admin.site.register(Enderecos, EnderecosAdmin)