from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog import views
urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^$', views.foo),
)
