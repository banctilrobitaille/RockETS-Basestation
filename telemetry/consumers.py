from channels import Group

from telemetry.models import Sensor


def ws_connect(message, sensor_uuid, measure):
    message.reply_channel.send({"accept": True})
    try:
        sensor = Sensor.objects(uuid=sensor_uuid).first()

        if sensor.is_local():
            Group(sensor_uuid + "-" + measure).add(message.reply_channel)
        else:
            sensor_node = Sensor.objects(uuid=sensor_uuid).first().node
            Group(sensor_node + "-" + measure).add(message.reply_channel)
    except Exception as e:
        Group("main-" + measure).add(message.reply_channel)


def ws_disconnect(message):
    Group("telemetry").discard(message.reply_channel)
