from __future__ import unicode_literals

from django.db import models
from mongoengine import *


class Rocket(Document):
    name = StringField()
