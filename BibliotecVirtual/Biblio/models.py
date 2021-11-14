from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class Post(models.Model):
    ramo = models.CharField(max_length=8)
    archvio = models.FileField(upload_to="myfolder/", blank=True, null=True) 

    def __str__(self):
        return self.ramo
    