monitoring
==========

A Django monitoring system app.

How to install
==============

1. Clone this app into your django project as an app.
2. Update your django project settings.py to add monitoring app.
3. Update your django project urls.py to serve the monitoring requests.
4. Restart your django server.

settings.py 
===========
```python
INSTALLED_APPS += ('monitoring', )
```

urls.py
=======
```python
urlpatterns = patterns('',
    url(r'^monitoring/', include('monitoring.urls')),
)
```

Test
====
test1: 
```python
http://yourhost/monitoring/test1/
```
test2: 
```python
http://yourhost/monitoring/test2/123/
```
