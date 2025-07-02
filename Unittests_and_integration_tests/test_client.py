import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized
from fixtures import test_payload

class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        expected_result = {"some": "data"}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_result)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )
        
    def test_public_repos_url(self):
        """ Tests that _public_repos_url returns mocked payload """

        known_payload: dict = {"repos_url": "https://example.com/test"}
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = known_payload
            request = GithubOrgClient("test")
            result = request._public_repos_url

            self.assertEqual(result, known_payload["repos_url"])

if __name__ == '__main__':
    unittest.main()
