import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import test_payload, TEST_PAYLOAD

class TestGithubOrgClient(unittest.TestCase):
    """ GithubOrgClient test case """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):

        """ returns the correct value """
        expected_result = {"some": "data"}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_result)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )
        
    def test_public_repos_url(self):
        """ public_repos test case """

        known_payload: dict = {"repos_url": "https://example.com/test"}
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = known_payload
            request = GithubOrgClient("test")
            result = request._public_repos_url

            self.assertEqual(result, known_payload["repos_url"])

    @parameterized.expand([
        ( {"license": {"key": "my_license"}}, "my_license", True ),
        ( {"license": {"key": "other_license"}}, "my_license", False ),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ test_has_license test case """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ setupclass test case """
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        def side_effect(url, *args, **kwargs):
            class MockResponse:
                def __init__(self, payload):
                    self._payload = payload
                def json(self):
                    return self._payload
            if url == cls.org_payload["repos_url"]:
                return MockResponse(cls.repos_payload)
            return MockResponse(cls.org_payload)
        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

if __name__ == '__main__':
    unittest.main()
