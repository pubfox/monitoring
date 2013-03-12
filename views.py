from django.http import HttpResponse
import json

def json_view(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return HttpResponse(json.dumps(result), mimetype='application/json')
    return wrapper

@json_view
def test1(request):
    return {'result': 'ok'}

@json_view
def test2(request, id):
    return {'result': id}
