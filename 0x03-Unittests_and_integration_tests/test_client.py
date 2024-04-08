#!/usr/bin/env python3
""" This is a module that run the test for client.py file """


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url):
        """ This is a method that test the public_repos method """

        mock_public_repos_url.return_value = "test"
        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = [{"name": "test"}]
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class.public_repos(), ["test"])
            mock_get_json.assert_called_once_with("test")

    @parameterized.expand([
            ({'license': {'key': 'my_license'}}, 'my_license', True),
            ({'license': {'key': 'other_license'}}, 'my_license', False),
    ])
    def test_has_license(self, repo, license_key, expected_return) -> None:
        """ This a method that test the has_license method """
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.has_license(repo, license_key),
                         expected_return)


@parameterized_class((
    "org_payload",
    "repos_payload",
    "expected_repos",
    "apache2_repos"),
    [(
        TEST_PAYLOAD[0][0],
        TEST_PAYLOAD[0][1],
        TEST_PAYLOAD[0][2],
        TEST_PAYLOAD[0][3]
    )]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ This is a class that test the GithubOrgClient class """

    @classmethod
    def setUpClass(cls):
        """ This is a method that set up the class """
        config = {'return_value.json.side_effect': [
                    cls.org_payload,
                    cls.repos_payload,
                    cls.org_payload,
                    cls.repos_payload
                ]}
        cls.patcher = patch('requests.get', **config)
        cls.patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ This is a method to tear down the class """
        cls.patcher.stop()

    def test_public_repos(self):
        """ This is a method that test the public_repos method """
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("test"), [])

    def test_public_repos_with_license(self):
        """ This is a method that test the public_repos method
        with license """
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)
