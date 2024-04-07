#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ This is a test class that handle the test methods """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ This is a method that test if function access_nested_map
        return the value as expected """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_key):
        """ This is a method that test the function test_access_nested_map_
        exception and return the value as expected """

        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_key}'")


class TestGetJson(unittest.TestCase):
    """ This is a class that handle the given methods """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ This method return the json of the test_url """

        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ This is a test class that handle the given test methods """

    def test_memoize(self):
        """ This is a method that handle the nested class test """
        class TestClass:
            """ This is a test class that handle the nested methods """
            def a_method(self):
                """ This is a method that return 42 """
                return 42

            @memoize
            def a_property(self):
                """ This is a method that return the self.a_method """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_object = TestClass()
            result1 = test_object.a_property()
            result2 = test_object.a_property()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
