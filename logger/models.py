from __future__ import unicode_literals

from datetime import datetime
from mongoengine import *


class LogData(Document):
    log_time = DateTimeField(default=datetime.now())
    device_type = StringField(required=True)
    measures = DictField()
