from django.conf.urls.defaults import *

urlpatterns = patterns('monitoring.views',
    url(r'^phosts/$', 'phosts', name='all_phosts'),
    url(r'^phosts/(?P<phost_id>\w+)/$', 'phosts', name='single_phost'),
    url(r'^phosts/(?P<phost_id>\w+)/get_current/(?P<name>\w+)/$', 'get_current', name='get_current'),
    url(r'^phosts/(?P<phost_id>\w+)/get_average/(?P<name>\w+)/$', 'get_average', name='get_average'),
)
