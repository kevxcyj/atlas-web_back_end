#!/usr/bin/env python3
"""unitest"""
import unittest
import utils
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, *path), expected)


if __name__ == '__main__':
    unittest.main()
