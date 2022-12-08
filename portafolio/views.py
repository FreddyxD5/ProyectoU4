from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Portafolio


from portafolio.forms import ProyectoForm

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

def CreateItemPortafolio(request):
    form = ProyectoForm()

    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            Portafolio.objects.create(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                image_url = form.cleaned_data['image_url'],
                tags = form.cleaned_data['tags'],
                repo_url = form.cleaned_data['repo_url'],
            )
            return redirect('index')
        else:
            return redirect('crear_item')
    return render(request, 'portafolio/crear_item_portafolio.html',context={'form':form})