from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Portafolio(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)    
    title = models.CharField('Titulo del proyecto', max_length=200)
    description = models.TextField('Descripcion',max_length=200)
    tags = models.CharField('Tags',max_length=200)
    image_url = models.URLField('Imagen del Proyecto (URL)')
    repo_url = models.URLField('Repositorio Git (URL)')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)    
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    

    def __str__(self):
        return f"{self.id} - {self.title}"