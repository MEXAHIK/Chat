# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect
from Chat.forms import LoginForm, RegisterForm
from django.contrib.auth.forms import User

def main_page(request, email):
	if request.user.is_authenticated():
		return render_to_response('main.html', context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

def view_regiser(request):
	register_form = RegisterForm()
	register_form_errors = False
	if request.method == "POST":
		reg_form = RegisterForm(request.POST)
		if reg_form.is_valid():
			passw = reg_form.password2
			user = User.objects.create_user(username=reg_form.email, email=reg_form.email, password=passw)
			user.is_staff = True
			user.save()
			return HttpResponseRedirect('/main/')
		else:
			register_form_errors = RegisterForm(request.POST)
			register_form = RegisterForm(request.POST, initial = {'email': reg_form.email})
	return render_to_response('register.html', {'register_form': register_form, 'form_errors': register_form_errors}, context_instance = RequestContext(request))

def logout_user(request):
	auth.logout(request)
	return HttpResponseRedirect('/main/')

def login_user(request):
	login_form = LoginForm()
	if request.method == "POST":
		login_user = LoginForm(request.POST)
		if login_user.is_valid():
			user = login_user.user_cache
			auth.login(request, user)
			return HttpResponseRedirect('/main/')
		else:
			login_form = LoginForm(request.POST, initial = {'email': request.POST.get('email')})
	return render_to_response('login.html', {'login_form': login_form}, context_instance = RequestContext(request))
