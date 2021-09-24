from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet

router = routers.DefaultRouter()
router.register(r'enderecos', EnderecoViewSet, basename='Endereco')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
