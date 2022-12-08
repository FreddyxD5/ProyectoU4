from django.shortcuts import render
from django.views.generic import TemplateView
from portafolio.forms import ProyectoForm

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

def CreateItemPortafolio(request):
    form = ProyectoForm()
    return render(request, 'portafolio/crear_item_portafolio.html',context={'form':form})