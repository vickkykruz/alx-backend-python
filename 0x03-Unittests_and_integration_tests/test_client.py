#!/usr/bin/env python3
""" This is a module that run the test for client.py file """


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ This is a test class that handke the given methods """

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ This is a method that return the ..."""

        client = GithubOrgClient(org_name)
        org_info = client.org()
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """ This function define a known payload and run test """
        known_payload = {
                'repos_url': 'https://api.github.com/orgs/test_org/repos'
                }

        # Patch GithubOrgClient.org to return the known payload
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock, return_value=known_payload):
            # Instantiate the GithubOrgClient
            client = GithubOrgClient('test_org')

            # Access the _public_repos_url property
            public_repos_url = client._public_repos_url

            # Assert that the result is the expected one based on the mocked
            self.assertEqual(
                    public_repos_url,
                    'https://api.github.com/orgs/test_org/repos')
