from mastodon import Mastodon
import config_pawoo

class MastodonAppManager():
    """マストドンのAPIを叩くために必要なclient_idやaccess_tokenを発行する
    """

    """Mastodonに登録するアプリ名"""
    app_name = "utakata_test_app"

    def get_client_id_filename(self, instance_name):
        """client_idを保存するファイル名を取得する
        """
        return self.app_name + "_" + instance_name + ".client_id"

    def create_app(self, instance_name, api_base_url):
        """Mastodonにアプリを登録してclient_idをファイルに出力する
        """
        Mastodon.create_app(
            self.app_name,
            api_base_url = api_base_url,
            to_file = self.get_client_id_filename(instance_name)
        )

    def get_access_token_filename(self, instance_name):
        """access_tokenを保存するファイル名を取得する
        """
        return self.app_name + "_" + instance_name + ".access_token"

    def log_in(self, instance_name, api_base_url, user_email, user_password):
        """access_tokenを取得する

        予め対応したclient idを取得してファイルに出力しておく必要がある。
        """
        mastodon = Mastodon(
            client_id = self.get_client_id_filename(instance_name),
            api_base_url = api_base_url
        )
        mastodon.log_in(
            user_email,
            user_password,
            to_file = self.get_access_token_filename(instance_name)
        )
