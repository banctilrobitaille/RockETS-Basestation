import configparser


class SlackConfigurationProvider(object):
    __INSTANCE = None
    SLACK_CONFIGURATION_FILE = "slack_configurations.ini"
    SLACK_AUTHENTICATION_CONFIGURATION_SECTION = "SLACK_AUTHENTICATION"
    SLACK_CLIENT_ID_PROPERTIES = "SLACK_CLIENT_ID"
    SLACK_CLIENT_SECRET_PROPERTIES = "SLACK_CLIENT_SECRET"
    SLACK_OAUTH_TOKEN_PROPERTIES = "SLACK_OAUTH_TOKEN"

    def __init__(self):
        self.configuration = configparser.ConfigParser()
        self.configuration.read("slack/slack_configurations.ini")

    def get_client_id(self):
        return self.configuration[self.SLACK_AUTHENTICATION_CONFIGURATION_SECTION][self.SLACK_CLIENT_ID_PROPERTIES]

    def get_client_secret(self):
        return self.configuration[self.SLACK_AUTHENTICATION_CONFIGURATION_SECTION][self.SLACK_CLIENT_SECRET_PROPERTIES]

    def get_oauth_token(self):
        return self.configuration[self.SLACK_AUTHENTICATION_CONFIGURATION_SECTION][self.SLACK_OAUTH_TOKEN_PROPERTIES]

    @staticmethod
    def get_instance():
        if SlackConfigurationProvider.__INSTANCE is None:
            SlackConfigurationProvider.__INSTANCE = SlackConfigurationProvider()
        return SlackConfigurationProvider.__INSTANCE
