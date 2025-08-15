#!/usr/bin/env python3
"""
Fixtures for integration tests of GithubOrgClient.

Contains:
    org_payload: Example org JSON with repos URL.
    repos_payload: Example list of repositories with licenses.
    expected_repos: Expected list of repository names.
    apache2_repos: Expected list filtered by 'apache-2.0'.
"""

org_payload = {
    "login": "google",
    "id": 1342004,
    "repos_url": "https://api.github.com/orgs/google/repos"
}

repos_payload = [
    {"id": 1, "name": "truth", "license": {"key": "apache-2.0"}},
    {"id": 2, "name": "guice", "license": {"key": "apache-2.0"}},
    {"id": 3, "name": "re2", "license": {"key": "bsd-3-clause"}},
    {"id": 4, "name": "tink", "license": {"key": "apache-2.0"}},
    {"id": 5, "name": "flatbuffers", "license": {"key": "apache-2.0"}},
    {"id": 6, "name": "some-mit", "license": {"key": "mit"}}
]

expected_repos = [r["name"] for r in repos_payload]

apache2_repos = [
    r["name"] for r in repos_payload
    if r.get("license", {}).get("key") == "apache-2.0"
]
