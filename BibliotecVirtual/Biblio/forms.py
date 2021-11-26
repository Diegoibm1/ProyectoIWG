from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }

class PostForm(forms.ModelForm):
	ramo = forms.CharField(label="", max_length=7,widget=forms.Textarea(attrs={'rows':1,'placeholder': "Ingresar ramo en formato FIS-100", 'required': True,}) )
	titulo = forms.CharField(label="", widget=forms.Textarea(attrs={ 'rows':1, 'placeholder': "Ingresa el titulo", 'required': True,}))
	archivo = forms.FileField(label="", required=True)
	
	class Meta:
		model = Post
		fields = ['titulo','ramo','archivo']