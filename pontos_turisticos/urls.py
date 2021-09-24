from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from atracoes.api.viewsets import AtracaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from enderecos.api.viewsets import EnderecoViewSet

router = routers.DefaultRouter()
router.register(r'enderecos', EnderecoViewSet, basename='Endereco')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
