from mastodon import Mastodon

# TODO divide config
mastodon = Mastodon(
    client_id = "utakatatestapp_pawoo.secret",
    api_base_url = "https://pawoo.net"
)

mastodon.log_in(
    "email",
    "password",
    to_file = "utakatatestapp_pawoo_yutakata.secret"
)
