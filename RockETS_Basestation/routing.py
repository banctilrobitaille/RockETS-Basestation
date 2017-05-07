from channels.routing import route
from telemetry import consumers as telemetry_consumers

channel_routing = [
    route("websocket.connect", telemetry_consumers.ws_connect,
          path=r"^/telemetry/(?P<sensor_uuid>[\w\-]{0,50})/(?P<measure>[\w\-]{0,50})$"),
    route("websocket.disconnect", telemetry_consumers.ws_disconnect, path=r"^/telemetry$")
]
