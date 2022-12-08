from django.urls import path
from portafolio.views import Index, CreateItemPortafolio


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('crear_item', CreateItemPortafolio, name='crear_item')
]
