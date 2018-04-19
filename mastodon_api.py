from mastodon import Mastodon, StreamListener

class MastodonApi():
    """MastodonのAPIを叩くためのクライアント"""

    def __init__(self, client_id_filename, access_token_filename, api_base_url):
        self.mastodon = Mastodon(
            client_id = client_id_filename,
            access_token = access_token_filename,
            api_base_url = api_base_url
        )

    def toot(self, text):
        self.mastodon.toot(text)

    def stream_local(self):
        listener = Listener()
        self.mastodon.stream_local(listener)

class Listener(StreamListener):
    """Mastodonのstreaming apiのListener

    https://github.com/halcy/Mastodon.py/blob/master/mastodon/streaming.py
    """

    def on_update(self, status):
        print(status)

    def on_delete(self, status_id):
        print("delete: " + str(status_id))

if __name__ == "__main__":
    mastodon = MastodonApi(
        "utakata_test_app_pawoo.client_id",
        "utakata_test_app_pawoo.access_token",
        "https://pawoo.net"
    )
    mastodon.stream_local()
