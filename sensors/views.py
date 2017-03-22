from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        return render_to_response('sensors/sensors-index.html', None, RequestContext(request))
