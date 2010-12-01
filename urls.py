from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('Chat.views',
    (r'^$', 'main_page', {'email': 'email'}),
    (r'^main/$', 'main_page', {'email': 'email'}),
    (r'^logout_user/$', 'logout_user'),
    (r'^login/$', 'login_user'),
    (r'^admin/', include(admin.site.urls)),
    (r'^register/$', 'view_regiser'),
    (r'^create-room/$', 'create_room'),
    (r'^autch/' , 'autch'),
    url(r'^chat-room/(?P<id>\d+)/$', 'chat_room_details', name = 'chat_room_details'),
    (r'^send-message/$', 'send_message'),
    (r'^update-message/$', 'update_message'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
	(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 
	'django.views.static.serve', 
	{'document_root': settings.MEDIA_ROOT}),
	)
