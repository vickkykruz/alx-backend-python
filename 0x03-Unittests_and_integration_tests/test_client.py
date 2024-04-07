#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ This is a test class that handke the given methods """

    @patch('client.get_json', return_value={'login': 'test_org'})
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    def test_org(self, org_name, mock_get_json):
        """ This is a method that return the ..."""

        client = GithubOrgClient(org_name)
        org_info = client.org()
        self.assertEqual(org_info['login'], 'test_org')
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")
