from django.urls import path
from portafolio.views import (
    Index, ListarPortafolio, EditarPortafolioView, 
    CreatePortafolioView, EliminarItemPortafolio)


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('crear_item', CreatePortafolioView.as_view(),  name='crear_item'),
    path('listar_items', ListarPortafolio.as_view(), name='listar_proyectos'),
    path('edit_item/<pk>', EditarPortafolioView.as_view(), name='edit_proyecto'),
    path('eliminar_item/<pk>', EliminarItemPortafolio.as_view(),name='eliminar_item')
]
