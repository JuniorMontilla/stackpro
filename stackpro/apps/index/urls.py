from django.conf.urls import patterns, url


urlpatterns = patterns('stackpro.apps.index.views',
            url(r'^$','view_index',name='url_index'),
)