from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Portafolio


from portafolio.forms import ProyectoForm

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):       
        context = super().get_context_data(**kwargs)        
        context['portafolio'] = Portafolio.objects.all()
        return context


class CreatePortafolioView(LoginRequiredMixin, CreateView):    
    model = Portafolio
    template_name = 'portafolio/crear_item_portafolio.html'
    fields= ['title', 'description', 'tags', 'image_url', 'repo_url']
    success_url = reverse_lazy('index')

class EditarPortafolioView(LoginRequiredMixin, UpdateView):
    model = Portafolio
    template_name = 'portafolio/crear_item_portafolio.html'
    fields= ['title', 'description', 'tags', 'image_url', 'repo_url']
    success_url = reverse_lazy('listar_proyectos')
        

def verdader():
    return True


#@login_required
# def create_item_portafolio(request):
#     form = ProyectoForm()
#     if request.method == 'POST':
#         form = ProyectoForm(request.POST)        
#         if form.is_valid():            
#             Portafolio.objects.create(
#                 title = form.cleaned_data['title'],
#                 description = form.cleaned_data['description'],
#                 image_url = form.cleaned_data['image_url'],
#                 tags = form.cleaned_data['tags'],
#                 repo_url = form.cleaned_data['repo_url'],
#             )
#             return redirect('index')
#         else:
#             return redirect('crear_item')
#     return render(request, 'portafolio/crear_item_portafolio.html',context={'form':form})


class EliminarItemPortafolio(LoginRequiredMixin, DeleteView):
    model = Portafolio
    success_url = '/'


class ListarPortafolio(LoginRequiredMixin, ListView):
    model = Portafolio
    template_name = 'portafolio/listar_items.html'
    context_object_name = 'items_portafolio'