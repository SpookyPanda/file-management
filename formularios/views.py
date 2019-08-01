from django.shortcuts import render
from .forms import UserForm, userinfoForm

# Create your views here.
def index(request):
	return render(request, 'home/index.html')

def register(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = userinfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit=False)
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user_info = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']


			profile.save()
			registered = True

		else:
			print(user_form.errors,profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = userinfoForm()

	return render(request, 'formularios/formapp.html',
											{'user_form':UserForm,
											 'profile_form':userinfoForm,
											 'registered':registered})

