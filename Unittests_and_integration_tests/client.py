#!/usr/bin/env python3
"""
GitHub client to fetch organization repositories.

Classes:
    GithubOrgClient: Small wrapper around the GitHub API for org data.
"""

from typing import Any, Dict, List, Mapping, Optional
from utils import get_json, memoize


class GithubOrgClient:
    """
    Lightweight client for GitHub organization data and repositories.
    """

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org: str) -> None:
        """Initialize client with organization slug."""
        self._org: str = org

    @property
    @memoize
    def org(self) -> Dict[str, Any]:
        """Return the organization payload from GitHub API."""
        url = self.ORG_URL.format(org=self._org)
        return get_json(url)

    @property
    def _public_repos_url(self) -> str:
        """
        Return the API URL listing public repos for the organization.

        Derived from the `repos_url` field in the organization payload.
        """
        return self.org.get("repos_url")  # type: ignore[return-value]

    def public_repos(self, license: Optional[str] = None) -> List[str]:
        """
        Return the list of public repository names.

        Args:
            license: Optional license key to filter repositories.

        Returns:
            A list of repository names (strings).
        """
        repos_payload = get_json(self._public_repos_url)
        names: List[str] = []
        for repo in repos_payload:
            if license is None or self.has_license(repo, license):
                names.append(repo.get("name"))  # type: ignore[arg-type]
        return names

    @staticmethod
    def has_license(repo: Mapping[str, Any], license_key: str) -> bool:
        """
        Check whether a repository has the given license key.

        Args:
            repo: Repository payload dictionary.
            license_key: License key to check for (e.g., 'apache-2.0').

        Returns:
            True if repo.license.key == license_key, else False.
        """
        license_info = repo.get("license") or {}
        return license_info.get("key") == license_key
