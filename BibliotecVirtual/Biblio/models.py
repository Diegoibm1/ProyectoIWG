from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    titulo=models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestap = models.DateTimeField(default=timezone.now)
    ramo = models.CharField(max_length=7)
    archivo = models.FileField(upload_to="myfolder/", blank=True, null=True)
    class meta:
        ordering = ['-timestap']

    def __str__(self):
        return f'{self.user.username}: {self.ramo}: {self.archivo}'
