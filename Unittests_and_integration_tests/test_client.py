#!/usr/bin/env python3
"""
Unit and integration tests for client.py (GithubOrgClient).
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
from client import GithubOrgClient
from fixtures import (
    org_payload,
    repos_payload,
    expected_repos,
    apache2_repos,
)


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient methods."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """org property calls get_json once with expected URL and returns it."""
        expected = {"login": org_name}
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """_public_repos_url derives from org payload."""
        payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        with patch(
            "client.GithubOrgClient.org",
            new_callable=Mock,
            return_value=payload,
        ):
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """public_repos returns repo names; URL and get_json called once."""
        mock_get_json.return_value = [
            {"name": "truth", "license": {"key": "apache-2.0"}},
            {"name": "re2", "license": {"key": "bsd-3-clause"}},
        ]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=Mock,
            return_value="https://api.github.com/orgs/google/repos",
        ) as mock_url:
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["truth", "re2"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """has_license returns True iff license key matches."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected
        )


@parameterized_class([{
    "org_payload": org_payload,
    "repos_payload": repos_payload,
    "expected_repos": expected_repos,
    "apache2_repos": apache2_repos,
}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient.public_repos.
    Only external HTTP (requests.get) is mocked.
    """

    @classmethod
    def setUpClass(cls):
        """Patch requests.get so .json() returns fixtures based on URL."""
        def _mock_get(url):
            mock_resp = Mock()
            org_url = (
                f"https://api.github.com/orgs/"
                f"{cls.org_payload['login']}"
            )
            if url == org_url:
                mock_resp.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_resp.json.return_value = cls.repos_payload
            else:
                mock_resp.json.return_value = {}
            return mock_resp

        cls.get_patcher = patch("client.requests.get", side_effect=_mock_get)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stop requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """public_repos returns the expected list of names."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """public_repos supports filtering by license key."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos,
        )


if __name__ == "__main__":
    unittest.main()
