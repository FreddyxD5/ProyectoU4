from django import forms

class ProyectoForm(forms.Form):    
    title = forms.CharField()
    description = forms.CharField()
    image_url = forms.URLField()
    tags = forms.CharField(max_length=200)
    repo_url = forms.URLField()



