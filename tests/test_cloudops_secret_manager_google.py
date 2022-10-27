import unittest

from cloudops.secret_manager.google import GoogleSecret


class TestSecretManager(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True, "I leave Python!")

    # def test_get_secret(self):
    #     secret_manager = GoogleSecret("manucalop", "test-secret")
    #     secret = secret_manager.pull()
    #     print(secret)
    #     assert secret["value"] == "test"
