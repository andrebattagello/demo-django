from django.conf.urls.defaults import patterns, url
from lista import views


urlpatterns = patterns('',

    url(r'^(?P<item_id>\d+)/$',
        views.ver_detalhes_item,
        name='ver_detalhes_item'),

    url(r'^adicionar_item/$',
        views.adicionar_item,
        name='adicionar_item'),

    url(r'^$',
        views.ver_lista,
        name='ver_lista'),
)
