import os
from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RockETS_Basestation.settings")

channel_layer = get_channel_layer()
