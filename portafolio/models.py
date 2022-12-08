from django.db import models

# Create your models here.
class Portafolio(models.Model):
    image_url = models.URLField('IMAGE URL del proyecto')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    tags = models.CharField(max_length=200)
    repo_url = models.URLField('Repositorio GIT_URL')
    