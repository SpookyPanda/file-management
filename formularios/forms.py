from django import forms
from django.contrib.auth.models import User
from .models import userinfo
from django.forms import ModelForm
from django.contrib.auth import views as auth_view


class UserForm(forms.ModelForm):
	contraseña = forms.CharField(widget=forms.PasswordInput())
	confirme_contraseña = forms.CharField(widget=forms.PasswordInput())
	usuario = 'username'

	class Meta():
		model = User
		fields = ('email','username', 'contraseña', 'confirme_contraseña')


class userinfoForm(forms.ModelForm):
	class Meta():
		model = userinfo
		fields = ('portfolio_site', 'profile_pic')