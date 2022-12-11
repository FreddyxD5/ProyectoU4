from django.shortcuts import render, redirect
from django.views.generic import CreateView
from users.forms import RegisterNewUserForm

# Create your views here.
class RegisterNewUserView(CreateView):
    template_name = 'users/registration/register.html'
    form_class = RegisterNewUserForm


    def form_valid(self, form):        
        form.save()        
        return redirect('login')        
    