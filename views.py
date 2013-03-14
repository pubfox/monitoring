from django.http import HttpResponse
import json

def json_view(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return HttpResponse(json.dumps(result), mimetype='application/json')
    return wrapper

@json_view
def phosts(request, phost_id=None):
    all_phosts = {'phost1':'phost1', 'phost2':'phost2', }
    if phost_id==None:
        return all_phosts
    return all_phosts.get(phost_id, {})

@json_view
def get_current(request, phost_id, name):
    return {'result': id}

@json_view
def get_average(request, phost_id, name):
    return {'result': id}