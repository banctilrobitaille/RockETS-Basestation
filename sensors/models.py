from __future__ import unicode_literals

from django.db import models
from mongoengine import *


class Sensor(Document):
    name = StringField()
    uuid = UUIDField()
    alias = ListField()
