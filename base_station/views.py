from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base_station.models import Rocket


def index(request):
    return HttpResponse(Rocket.objects.all()[0].name)

#
# @api_view(['GET'])
# def post_collection(request):
#    if request.method == 'GET':
#        return Response()
