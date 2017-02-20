from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello world !")

#
# @api_view(['GET'])
# def post_collection(request):
#    if request.method == 'GET':
#        return Response()
