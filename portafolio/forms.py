from django import forms

class ProyectoForm(forms.Form):
    image_url = forms.URLField('IMAGE URL del proyecto')
    title = forms.CharField()
    description = forms.CharField()
    tags = forms.CharField(max_length=200)
    repo_url = forms.URLField('Repositorio GIT_URL')
    


