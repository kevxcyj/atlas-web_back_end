#!/usr/bin/env python3
""" unitest """
import unittest
import utils
from parameterized import parameterized
from unittest.mock import patch
from utils import memoize
from utils import get_json
from fixtures import test_payload

class TestAccessNestedMap(unittest.TestCase):
    """ access_nested_map test """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, *path), expected)

class TestGetJson(unittest.TestCase):
    """ get_json test """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """ test_momoize test """
    def test_memoize(self):

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()


        test_instance = TestClass()
        result1 = test_instance.a_property
        self.assertEqual(result1, 42)
        result2 = test_instance.a_property
        self.assertEqual(result2, 42)

        with patch.object(TestClass, 'a_method') as mock_method:
            test_instance.a_property
            test_instance.a_property
            mock_method.assert_called_once()



if __name__ == '__main__':
    unittest.main()
