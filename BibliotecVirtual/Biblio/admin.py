from django.contrib import admin

from Biblio.views import register
from .models import Post, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)