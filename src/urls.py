from django.conf.urls.defaults import *

from blog import views
urlpatterns = patterns('',
	(r'^$', views.foo),
)
