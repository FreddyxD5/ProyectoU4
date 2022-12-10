from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Perfil

class RegisterNewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    
    def save(self, commit = True):
        user = super(RegisterNewUserForm, self).save(commit=False)
        #aumentar el email
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Perfil.objects.create(user=user)
        return user
