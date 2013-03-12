from django.conf.urls.defaults import *

urlpatterns = patterns('monitoring.views',
    url(r'^test1/$', 'test1', name='test1'),
    url(r'^test2/(\d+)/$', 'test2', name='test2'),
)
