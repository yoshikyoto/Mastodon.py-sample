from mastodon_app_manager import MastodonAppManager
import config_pawoo

manager = MastodonAppManager()
manager.create_app(
    config_pawoo.INSTANCE_NAME,
    config_pawoo.API_BASE_URL
)
manager.log_in(
    config_pawoo.INSTANCE_NAME,
    config_pawoo.API_BASE_URL,
    config_pawoo.USER_EMAIL,
    config_pawoo.USER_PASSWORD
)
