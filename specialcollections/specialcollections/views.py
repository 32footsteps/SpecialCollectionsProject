from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def login_view(request):

	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		auth = authenticate(username=username, password=password)

		if auth is not None:
			login(request, auth)
			return HttpResponseRedirect(reverse('collections:index'))

		else:
			messages.add_message(request, messages.INFO, "Authentication Failure")
			return HttpResponseRedirect(reverse('home'))


	return render(request, 'home.html')

def home_view(request):

	if request.user.is_authenticated():
		print("user is auth: " + str(request.user.is_authenticated()))

	return render(request, 'dashhome.html')

def logout_view(request):
	logout(request)
	return render(request, 'dashhome.html')