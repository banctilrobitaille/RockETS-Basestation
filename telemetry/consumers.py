from channels import Group

from telemetry.models import RemoteSensor


def ws_connect(message, sensor_uuid):
    message.reply_channel.send({"accept": True})
    try:
        sensor_node = RemoteSensor.objects(uuid=sensor_uuid).first().node
        Group(sensor_node).add(message.reply_channel)
    except Exception as e:
        pass


def ws_disconnect(message):
    Group("telemetry").discard(message.reply_channel)
