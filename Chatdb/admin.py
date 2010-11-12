from django.contrib import admin
from Chat.Chatdb.models import ChatRoom 

class ChatRoomAdmin(admin.ModelAdmin):
	list_display = ('name', 'author_name')
	
admin.site.register(ChatRoom, ChatRoomAdmin)
