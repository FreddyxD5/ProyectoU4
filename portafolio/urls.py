from django.urls import path
from portafolio.views import Index
urlpatterns = [
    path('', Index.as_view(), name='index'),
]
