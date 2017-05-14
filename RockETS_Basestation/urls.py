from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from telemetry.views import Telemetry, TelemetryMonitoredObjects, TelemetrySensors, TelemetryTransmitters, \
    TelemetryTransmitterStart, TelemetryTransmitterStop
from dashboards.views import Dashboards, Widgets
from core.views import Core

__BASE_PATH = "rest/api/"
__API_VERSION = "v1/"

schema_view = get_swagger_view(title='RockETS base station API ' + __API_VERSION)

urlpatterns = [
    url(r'^api/documentation$', schema_view),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation"), Core.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/telemetry/sensor"), TelemetrySensors.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/telemetry/monitored-object"),
        TelemetryMonitoredObjects.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/telemetry/transmitter"),
        TelemetryTransmitters.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/telemetry/transmitter/start"),
        TelemetryTransmitterStart.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/telemetry/transmitter/stop"),
        TelemetryTransmitterStop.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/telemetry"), Telemetry.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/dashboards/widget"), Widgets.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/dashboards"), Dashboards.as_view()),
    url(r'^{}{}{}$'.format("", "", "telemetry"), Telemetry.as_view()),
    url(r'^{}{}{}$'.format("", "", "telemetry/monitored-object"), TelemetryMonitoredObjects.as_view()),
    url(r'^{}{}{}$'.format("", "", "telemetry/sensor"), TelemetrySensors.as_view()),
    url(r'^{}{}{}$'.format("", "", "telemetry/transmitter"), TelemetryTransmitters.as_view()),
    url(r'^{}{}{}$'.format("", "", "telemetry/transmitter/start"), TelemetryTransmitterStart.as_view()),
    url(r'^{}{}{}$'.format("", "", "telemetry/transmitter/stop"), TelemetryTransmitterStop.as_view()),
    url(r'^{}{}{}$'.format("", "", "dashboards"), Dashboards.as_view()),
    url(r'^{}{}{}$'.format("", "", "dashboards/widget"), Widgets.as_view()),
    url(r'^{}{}{}'.format("", "", ""), Core.as_view()),
]
