from django.shortcuts import get_object_or_404, redirect, render
from Biblio.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, PostForm
# Create your views here.

def inicio(request):
    return render(request,"base.html")

def fis110(request):
    posts = Post.objects.all()
    context= {'posts': posts}
    return render(request,"ramos.html",context)

def register(request):
	if request.method == 'POST':
		print(request)
		form = UserCreationForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('http://127.0.0.1:8000/inicio/')
		else:
			print("\n no \n")
	else:
		form = UserCreationForm()

	context = { 'form' : form }
	return render(request, 'registro.html', context)

def post(request):
	current_user= get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form=PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.archivo = request.FILES["archivo"]
			post.save()
			messages.success(request, "Archivo subido")
			return redirect('http://127.0.0.1:8000/inicio/')
	else:
		form=PostForm()
	return render(request, 'archivos.html', {'form': form})