import configparser


class SlackConfigurationProvider(object):
    __INSTANCE = None
    SLACK_CONFIGURATION_FILE = "slack_configurations.ini"
    SLACK_AUTHENTICATION_CONFIGURATION_SECTION = "SLACK_AUTHENTICATION"
    SLACK_CLIENT_ID_PROPERTIES = "SLACK_CLIENT_ID"
    SLACK_CLIENT_SECRET_PROPERTIES = "SLACK_CLIENT_SECRET"

    def __init__(self):
        self.configuration = configparser.ConfigParser().read(self.SLACK_CONFIGURATION_FILE)

    def get_client_id(self):
        return self.configuration[self.SLACK_AUTHENTICATION_CONFIGURATION_SECTION][self.SLACK_CLIENT_ID_PROPERTIES]

    def get_client_secret(self):
        return self.configuration[self.SLACK_AUTHENTICATION_CONFIGURATION_SECTION][self.SLACK_CLIENT_SECRET_PROPERTIES]

    @staticmethod
    def get_instance():
        if SlackConfigurationProvider.__INSTANCE is None:
            SlackConfigurationProvider.__INSTANCE = SlackConfigurationProvider()
        return SlackConfigurationProvider.__INSTANCE
