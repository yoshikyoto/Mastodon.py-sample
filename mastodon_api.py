from mastodon import Mastodon

class MastodonApi():
    """マストドンのAPIを叩くクライアント

    このクライアントを継承して各種パラメータをオーバーライドすることで
    様々なマストドンインスタンスのAPIを叩くことができる
    """

    """Mastodonに登録するアプリ名"""
    app_name = "testapp"

    """Mastodon APIのbase_url

    https://pawoo.net
    https://friends.nico など
    継承したクラスでオーバーライドして利用する
    """
    api_base_url = ""

    """Mastodonのインスタンス名

    client_idやaccess_token保存のファイル名になるので
    インスタンスを識別できればよい
    継承したクラスでオーバーライドして利用する
    """
    instance_name = ""

    """ログインユーザーのemail

    継承したクラスでオーバーライドして利用する
    """
    user_email = ""

    """ログインユーザーのパスワード

    継承したクラスでオーバーライドして利用する
    """
    user_passwprd = ""

    def get_client_id_filename(self):
        """client_idを保存するファイル名を取得する
        """
        return self.app_name + "_" + self.config_name + ".client_id"

    def create_app(self):
        """Mastodonにアプリを登録してclient_idをファイルに出力する
        """
        Mastodon.create_app(
            self.app_name,
            api_base_url = self.api_base_url,
            to_file = self.get_client_id_filename()
        )

    def get_access_token_filename(self):
        """access_tokenを保存するファイル名を取得する
        """
        return self.app_name + "_" + self.config_name + ".access_token"

    def log_in(self):
        """access_tokenを取得する

        予め対応したclient idを取得してファイルに出力しておく必要がある。
        """
        mastodon = Mastodon(
            client_id = self.get_client_id_filename,
            api_base_url = self.api_base_url
        )
        mastodon.log_in(
            self.user_email,
            self.user_password,
            to_file = self.get_access_token_filename
        )
