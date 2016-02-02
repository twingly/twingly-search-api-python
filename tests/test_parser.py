from __future__ import unicode_literals
import unittest

import twingly_search

class ParserTest(unittest.TestCase):
    def test_with_valid_result(self):
        data = open("./tests/fixtures/valid_result.xml", 'r').read()
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)

    def test_with_valid_result_containing_non_blogs(self):
        data = open("./tests/fixtures/valid_non_blog_result.xml", 'r').read()
        if hasattr(data, 'decode'):
            data = data.decode("utf-8")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)
        self.assertEqual(len(r.posts), 1)

    def test_with_nonexistent_api_key_result(self):
        with self.assertRaises(twingly_search.TwinglyAuthException):
            data = open("./tests/fixtures/nonexistent_api_key_result.xml", 'r').read()
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            r = twingly_search.Parser().parse(data)

    def test_with_unauthorized_api_key_result(self):
        with self.assertRaises(twingly_search.TwinglyAuthException):
            data = open("./tests/fixtures/unauthorized_api_key_result.xml", 'r').read()
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            r = twingly_search.Parser().parse(data)

    def test_with_service_unavailable_result(self):
        with self.assertRaises(twingly_search.TwinglyServerException):
            data = open("./tests/fixtures/service_unavailable_result.xml", 'r').read()
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            r = twingly_search.Parser().parse(data)

    def test_with_undefined_error_result(self):
        with self.assertRaises(twingly_search.TwinglyServerException):
            data = open("./tests/fixtures/undefined_error_result.xml", 'r').read()
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            r = twingly_search.Parser().parse(data)

    def test_with_undefined_error_result(self):
        with self.assertRaises(twingly_search.TwinglyServerException):
            data = open("./tests/fixtures/non_xml_result.xml", 'r').read()
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            r = twingly_search.Parser().parse(data)