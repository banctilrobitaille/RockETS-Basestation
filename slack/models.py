from __future__ import unicode_literals

from mongoengine import *


class Team(Document):
    name = StringField(max_length=200)
    team_id = StringField(max_length=20)
    bot_user_id = StringField(max_length=20)
    bot_access_token = StringField(max_length=100)
