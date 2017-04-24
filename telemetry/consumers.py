from channels import Group


def ws_connect(message):
    message.reply_channel.send({"accept": True})

    Group("telemetry").add(message.reply_channel)


def ws_disconnect(message):
    Group("telemetry").discard(message.reply_channel)
