from django.shortcuts import redirect, render
from Biblio.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def inicio(request):
    titulo = "Bienvenidos"
    form = Post(request.FILES or None)
    return render(request,"base.html")

def fis110(request):
    posts = Post.objects.all()
    context= {'posts': posts}
    return render(request,"base.html",context)


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('feed')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'registro.html', context)
