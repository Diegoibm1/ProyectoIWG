from django.shortcuts import render

from Biblio.models import Post

# Create your views here.

def inicio(request):
    titulo = "Bienvenidos"
    form = Post(request.FILES or None)
    return render(request,"base.html")

