"""RockETS_Basestation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from core.views import Core
from dashboards.views import Dashboards, Widgets
from sensors.views import Sensors
from django.conf.urls import url

__BASE_PATH = "rest/api/"
__API_VERSION = "v1/"

urlpatterns = [
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation"), Core.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/sensors"), Sensors.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/dashboards/widget"), Widgets.as_view()),
    url(r'^{}{}{}$'.format(__BASE_PATH, __API_VERSION, "basestation/dashboards"), Dashboards.as_view()),
    url(r'^{}{}{}$'.format("", "", "sensors"), Sensors.as_view()),
    url(r'^{}{}{}$'.format("", "", "dashboards"), Dashboards.as_view()),
    url(r'^{}{}{}$'.format("", "", "dashboards/widget"), Widgets.as_view()),
    url(r'^{}{}{}'.format("", "", ""), Core.as_view()),
]
