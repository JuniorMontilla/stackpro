from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from stackpro.apps.employee.models import advert, answer 

urlpatterns = patterns('stackpro.apps.employee.views',
             url(r'^$',
                  ListView.as_view(
                      queryset = 	advert.objects.filter(status=True),
                      context_object_name = 'latest_advert_list',
                      template_name='index/index.html',
                  ),	
                  name='url_index'
                  ),
            url(r'^details/(?P<pk>\d+)/$',
                DetailView.as_view(
                    model=advert,
                    template_name='details/details.html',
               ),
              name='url_details'
              ),
            url(r'^work/','view_work',name='url_work'),
            url(r'^answer/$','view_answer',name='url_answer'),
)