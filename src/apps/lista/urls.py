from django.conf.urls.defaults import patterns, url
from lista import views


urlpatterns = patterns('',

    url(r'^$', views.ver_lista),
)
