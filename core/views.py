from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Rocket


def index(request):
    return render_to_response('core/base_template.html', None, RequestContext(request))

#
# @api_view(['GET'])
# def post_collection(request):
#    if request.method == 'GET':
#        return Response()
