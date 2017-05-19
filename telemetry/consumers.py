from channels import Group

from telemetry.models import Sensor


def ws_connect(message, sensor_uuid, measure):
    message.reply_channel.send({"accept": True})
    try:
        sensor_node = Sensor.objects(uuid=sensor_uuid).first().node
        Group(sensor_node + "-" + measure).add(message.reply_channel)
    except Exception as e:
        pass


def ws_disconnect(message):
    Group("telemetry").discard(message.reply_channel)
