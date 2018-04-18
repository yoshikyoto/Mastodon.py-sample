from mastodon import Mastodon

class MastodonApi():

    # todo read from constructor
    mastodon = Mastodon(
        client_id = "utakatatestapp_pawoo.secret",
        access_token = "utakatatestapp_pawoo_yutakata.secret",
        api_base_url = "https://pawoo.net"
    )

    def toot(self, text):
        self.mastodon.toot(text)


if __name__ == "__main__":
    mastodon = MastodonApi()
    mastodon.toot("こんにちは")
