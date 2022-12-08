from django import forms

class ProyectoForm(forms.Form):    
    Titulo= forms.CharField(label='Titulo del proyecto')
    Descripcion = forms.CharField(label='Descripcion del proyecto')
    image_url = forms.URLField(label='')
    tags = forms.CharField(max_length=200)
    repo_url = forms.URLField()



