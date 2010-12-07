#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class ChatRoom(models.Model):
	name = models.CharField("Название комнаты", max_length = 100)
	author_name = models.CharField("Автор", max_length = 100, blank = True)
	notes = models.CharField("Описание", max_length = 100, blank = True)
		
	def __unicode__(self):
		return "%s %s %s" % (self.name, self.author_name, self.notes)
	
	class Meta:
		ordering = ["id"]

class ChatRoomForm(ModelForm):
	
	class Meta:
		model = ChatRoom
		fields = ["name", "author_name", "notes"]
