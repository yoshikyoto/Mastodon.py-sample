from mastodon import Mastodon

class MastodonAppManager():

    def __init__(self, config):
        self.config_name = config.CONFIG_NAME
        self.app_name = config.APP_NAME
        self.api_base_url = config.API_BASE_URL
        self.user_name = config.USER_NAME
        self.user_email = config.USER_EMAIL
        self.user_password = config.USER_PASSWORD

    def app_secret_filename(self):
        return self.app_name + "_" + self.config_name + ".secret"

    def create_app(self):
        Mastodon.create_app(
            self.app_name,
            api_base_url = self.api_base_url,
            to_file = self.app_secret_filename()
        )
