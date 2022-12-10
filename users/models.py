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


class IpAddress(models.Model):
    pub_date=models.DateTimeField('Fecha de peticion')
    ip_address = models.GenericIPAddressField()

    class Meta:
        verbose_name = 'Direccion IP'
        verbose_name_plural = 'Direcciones de IP'
    def __str__(self):
        return f"{self.ip_address}"