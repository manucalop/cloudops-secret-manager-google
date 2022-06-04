from cloudops_google_secretmanager import SecretManager


class TestSecretManager:
    def test_get_secret(self):
        secret_manager = SecretManager("test-project", "test-secret")
        secret = secret_manager.pull()
        assert secret == "test-secret-value"
