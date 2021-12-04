from django.shortcuts import get_object_or_404, redirect, render
from Biblio.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, PostForm
# Create your views here.


def inicio(request):
    return render(request, "base.html")

def equipo(request):
    return render(request, "equipo.html")

def register(request):
    if request.method == 'POST':
        print(request)
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('http://127.0.0.1:8000/inicio/')
        else:
            print("\n no \n")
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registro.html', context)


def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.archivo = request.FILES["archivo"]
            post.save()
            messages.success(request, "Archivo subido")
            return redirect('http://127.0.0.1:8000/inicio/')
    else:
        form = PostForm()
    return render(request, 'archivos.html', {'form': form})


def VerArchivos(request, asignatura):
    if request.method == 'POST':
        post_liked = Post.objects.get(id=request.POST.get('post'))
        if request.user in post_liked.likes.all():
            post_liked.likes.remove(request.user)
        else:
            post_liked.likes.add(request.user)
    posts = Post.objects.all().filter(ramo=asignatura)
    context = {'posts': posts, 'user': request.user}
    return render(request, "ramos.html", context)


def archivos(request):
    ramos = list(Post.objects.values_list('ramo', flat=True).distinct())
    context = {'ramos': ramos}
    return render(request, "RamosTotales.html", context)


def ranking(request):
    usuarios = list(Post.objects.values_list('user', flat=True).distinct())
    post = list(Post.objects.values_list('likes',flat=True).distinct())
    print(usuarios)
    print(post)
    context = {}
    return render(request, "ranking.html", context)

