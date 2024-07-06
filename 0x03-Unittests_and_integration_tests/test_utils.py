#!/usr/bin/env python3
"""Test a utils function"""


import unittest
from unittest.mock import patch
from parameterized import parameterized  # type: ignore
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


class TestAccessNestedMap(unittest.TestCase):
    """A Nested Map test case"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: int) -> None:
        """A Test case for nested map"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        '''Raising of an exception'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Work with the get json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, req):
        """test get_json in utils"""
        req.return_value.json.return_value = test_payload
        response = get_json(test_url)
        self.assertEqual(response, test_payload)
        req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Memoize testing"""

    def test_memoize(self):
        """Memoize testing"""
        class TestClass:
            """Test case"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock.assert_called_once()
