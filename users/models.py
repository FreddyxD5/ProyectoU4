from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=250)
    biografia = models.TextField()
    twitter = models.URLField()
    facebook = models.URLField()
    github = models.URLField()
    linked_in = models.URLField()


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        
    def __str__(self):
        return f'{self.user.username } - {self.nombres} - {self.apellidos}'