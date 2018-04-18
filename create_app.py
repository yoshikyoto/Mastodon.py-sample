from mastodon_app_manager import MastodonAppManager
import config_pawoo

# create app
# アプリ作成時に一回だけやればいい
mastodon_app_manager = MastodonAppManager(config_pawoo)
mastodon_app_manager.create_app()
