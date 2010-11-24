from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from blog import views
urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^$', views.foo),
)
