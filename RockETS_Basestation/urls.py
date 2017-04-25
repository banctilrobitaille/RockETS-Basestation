from django.conf.urls import url

from telemetry.views import Telemetry
from dashboards.views import Dashboards, Widgets
from sensors.views import Sensors
from core.views import Core

__BASE_PATH = "rest/api/"
__API_VERSION = "v1/"

urlpatterns = [
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation"), Core.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/telemetry"), Telemetry.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/sensors"), Sensors.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/dashboards/widget"), Widgets.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/dashboards"), Dashboards.as_view()),
    url(r'^{}{}{}$'.format("", "", "telemetry"), Telemetry.as_view()),
    url(r'^{}{}{}$'.format("", "", "sensors"), Sensors.as_view()),
    url(r'^{}{}{}$'.format("", "", "dashboards"), Dashboards.as_view()),
    url(r'^{}{}{}$'.format("", "", "dashboards/widget"), Widgets.as_view()),
    url(r'^{}{}{}'.format("", "", ""), Core.as_view()),
]
