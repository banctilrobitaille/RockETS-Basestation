import configparser
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from slack.configuration_providers import SlackConfigurationProvider
from slack.validators import SlackOAuthValidator


class SlackOAuth(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        SlackOAuthValidator.validate_get_parameters_from(request.query_params)
        params = {
            'code': request.query_params['code'],
            'client_id': SlackConfigurationProvider.get_instance().get_client_id(),
            'client_secret': SlackConfigurationProvider.get_instance().get_client_secret()
        }
