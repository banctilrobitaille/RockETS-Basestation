from __future__ import unicode_literals
import abc
from mongoengine import *


class Team(Document):
    name = StringField(max_length=200)
    team_id = StringField(max_length=20)
    bot_user_id = StringField(max_length=20)
    bot_access_token = StringField(max_length=100)


class SlackMessage(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, title, event_timestamp):
        self.__title = title
        self.__event_timestamp = event_timestamp

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def event_timestamp(self):
        return self.__event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, event_timestamp):
        self.__event_timestamp = event_timestamp


class StateChangeSlackMessage(SlackMessage):
    def __init__(self, title, event_timestamp, from_state, to_state):
        super(StateChangeSlackMessage, self).__init__(title, event_timestamp)
        self.__from_state = from_state
        self.__to_state = to_state


class ApogeeReachedSlackMessage(SlackMessage):
    def __init__(self, title, event_timestamp, apogee_altitude):
        super(ApogeeReachedSlackMessage, self).__init__(title, event_timestamp)
        self.__apogee_altitude = apogee_altitude
