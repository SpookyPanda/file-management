from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
	path('ingresar/',
		auth_views.LoginView.as_view(template_name='formularios/login.html'),
		name='login'),
	path('registrarse/', views.register, name = 'register')

]