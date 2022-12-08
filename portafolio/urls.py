from django.urls import path
from portafolio.views import Index, CreateItemPortafolio, ListarPortafolio


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('crear_item', CreateItemPortafolio, name='crear_item'),
    path('listar_items', ListarPortafolio.as_view(), name='listar_proyectos'),
]
