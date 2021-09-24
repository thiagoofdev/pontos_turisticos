from django.contrib import admin
from django.db import models
from .models import PontoTuristico

class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'aprovado')

admin.site.register(PontoTuristico, PontoTuristicoAdmin)