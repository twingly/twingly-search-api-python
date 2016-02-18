from __future__ import unicode_literals
import unittest

import twingly_search

class ParserTest(unittest.TestCase):
    def get_fixture(self, fixture_name):
        file_path = "./tests/fixtures/%s.xml" % fixture_name
        fixture = open(file_path, 'r').read()
        return fixture

    def test_with_valid_result(self):
        data = self.get_fixture("valid_result")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)

    def test_with_valid_result_containing_non_blogs(self):
        data = self.get_fixture("valid_non_blog_result")
        if hasattr(data, 'decode'):
            data = data.decode("utf-8")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)
        self.assertEqual(len(r.posts), 1)

    def test_with_nonexistent_api_key_result(self):
        with self.assertRaises(twingly_search.TwinglyAuthException):
            data = self.get_fixture("nonexistent_api_key_result")
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            r = twingly_search.Parser().parse(data)

    def test_with_unauthorized_api_key_result(self):
        with self.assertRaises(twingly_search.TwinglyAuthException):
            data = self.get_fixture("unauthorized_api_key_result")
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            r = twingly_search.Parser().parse(data)

    def test_with_service_unavailable_result(self):
        with self.assertRaises(twingly_search.TwinglyServerException):
            data = self.get_fixture("service_unavailable_result")
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            r = twingly_search.Parser().parse(data)

    def test_with_undefined_error_result(self):
        with self.assertRaises(twingly_search.TwinglyServerException):
            data = self.get_fixture("undefined_error_result")
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            r = twingly_search.Parser().parse(data)

    def test_with_undefined_error_result(self):
        with self.assertRaises(twingly_search.TwinglyServerException):
            data = self.get_fixture("non_xml_result")
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            r = twingly_search.Parser().parse(data)
