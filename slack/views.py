from django_slack import slack_message
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from slackclient import SlackClient

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


class SlackMessage(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        sc = SlackClient(SlackConfigurationProvider.get_instance().get_oauth_token())

        sc.api_call(
                "chat.postMessage",
                channel="#basestation",
                attachments='[{'
                            '"text":"The rocket went from ON PAD to ON FLIGHT",'
                            '"title" : "Rocket state changed",'
                            '"color": "#36a64f"}]')
        return Response(status=status.HTTP_200_OK)
