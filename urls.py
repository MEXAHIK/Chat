from django.conf.urls.defaults import *
from django.contrib import admin
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
)
