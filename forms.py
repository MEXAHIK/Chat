# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import User

class LoginForm(forms.Form):
	email = forms.EmailField(label = "E-mail", required = True)
	password = forms.CharField(label = "Пароль", widget = forms.PasswordInput)
	
	def __init__(self, *args, **kwargs):
		self.user_cache = None
		super(LoginForm, self).__init__(*args, **kwargs)
	
	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		
		if email and password:
			self.user_cache = authenticate(username=email, password=password)
			if self.user_cache is None:
				raise forms.ValidationError("Пожалуйста, введите правильный адрес электронной почты и пароль.")
			elif not self.user_cache.is_active:
				raise forms.ValidationError("This account is inactive.")
		else:
			raise forms.ValidationError("Для входа необходимо заполнить все поля")
	def get_user(self):
		return self.user_cache

class RegisterForm(forms.Form):
	email = forms.EmailField(label = "E-mail")
	password1 = forms.CharField(label = "Пароль", widget = forms.PasswordInput)
	password2 = forms.CharField(label  = "Повторите пароль", widget = forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ('email',)
	
	def __init__(self, *args, **kwargs):
		self.email = None
		self.password2 = None
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
		
	def clean_email(self):
		self.email = self.cleaned_data.get('email')
		try:
			User.objects.get(email = self.email)
		except User.DoesNotExist:
			return self.email
		raise forms.ValidationError("Пользователь с таким Email уже существует")
	
	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		self.password2 = self.cleaned_data.get('password2')
		if password1 != self.password2:
			raise forms.ValidationError("Пароли не совпадают")
		return self.password2
	
	def save(self, commit = True):
		user = super(RegisterForm, self).save(commit = False)
		user.set_password(self.clean_password["password1"])
		user.username(self.clean_email["email"])
		if commit:
			user.save()
		return user
