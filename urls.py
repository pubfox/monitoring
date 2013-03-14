from django.conf.urls.defaults import *

urlpatterns = patterns('monitoring.views',
    url(r'^phosts/$', 'phosts', name='all_phosts'),
    url(r'^phosts/(\w+)/$', 'phosts', name='single_phost'),
    url(r'^phosts/(\w+)/get_current/(\w+)/$', 'get_current', name='get_current'),
    url(r'^phosts/(\w+)/get_average/(\w+)/$', 'get_average', name='get_average'),
)
