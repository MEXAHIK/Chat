# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect
from Chat.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from Chatdb.models import ChatRoomForm, ChatRoom
from django.contrib.auth.decorators import permission_required
#from django.contrib


def main_page(request, email):
	if request.user.is_authenticated():
		rooms = ChatRoom.objects.all()
		return render_to_response('main.html', {'rooms': rooms}, context_instance = RequestContext(request))
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
			user.user_permissions.add(19)
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

@permission_required('Chatdb.add_chatroom', '/autch/')
def create_room(request):
	create_form = ChatRoomForm()
	if request.method == 'POST':
		form = ChatRoomForm(request.POST)
		if form.is_valid():
			save_room = ChatRoom.objects.create(name = request.POST.get('name'), author_name = request.user.username)
			return HttpResponseRedirect('/main/')
		else:
			create_form = ChatRoomForm(request.POST)
			render_to_response('create_room.html', {'create_form': create_form}, context_instance = RequestContext(request))
	return render_to_response('create_room.html', {'create_form': create_form}, context_instance = RequestContext(request))

def autch(request):
	form = request.user.user_permissions.add(19)
	return render_to_response('autch.html', {'form': form})

@permission_required('Chatdb.add_chatroom', '/autch/')
def chat_room_details(request, id):
	return render_to_response('chat_room_details.html', context_instance = RequestContext(request))
