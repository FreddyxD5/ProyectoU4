from django import forms

class ProyectoForm(forms.Form):    
    title= forms.CharField(label='Titulo del proyecto', help_text='Titulo')
    description = forms.CharField(label='Descripcion del proyecto')
    image_url = forms.URLField(label='')    
    tags = forms.CharField(max_length=200)
    repo_url = forms.URLField()    



