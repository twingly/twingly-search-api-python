from __future__ import unicode_literals
import unittest
import twingly_search
import os
import requests_mock

class SearchTest(unittest.TestCase):
    def test_service_unavailable(self):
        with requests_mock.Mocker() as m:
            with self.assertRaises(twingly_search.TwinglyAuthException):
                m.get('https://api.twingly.com/analytics/Analytics.ashx', text=open("./tests/fixtures/service_unavailable_result.xml").read())
                c = twingly_search.Client()
                query = c.search.query('github page-size:10')
                result = query.execute()

    def test_search_unauthorized_api_key(self):
        with requests_mock.Mocker() as m:
            with self.assertRaises(twingly_search.TwinglyAuthException):
                m.get('https://api.twingly.com/analytics/Analytics.ashx', text=open("./tests/fixtures/unauthorized_api_key_result.xml").read())
                c = twingly_search.Client()
                query = c.search.query('github page-size:10')
                result = query.execute()

    def test_search_with_wrong_api_key(self):
        with requests_mock.Mocker() as m:
            with self.assertRaises(twingly_search.TwinglyAuthException):
                m.get('https://api.twingly.com/analytics/Analytics.ashx', text=open("./tests/fixtures/nonexistent_api_key_result.xml").read())
                c = twingly_search.Client()
                query = c.search.query('github page-size:10')
                result = query.execute()

    def test_search_undefined_error(self):
        with requests_mock.Mocker() as m:
            with self.assertRaises(twingly_search.TwinglyAuthException):
                m.get('https://api.twingly.com/analytics/Analytics.ashx', text=open("./tests/fixtures/undefined_error_result.xml").read())
                c = twingly_search.Client()
                query = c.search.query('github page-size:10')
                result = query.execute()

    def test_search_with_non_xml_result(self):
        with requests_mock.Mocker() as m:
            with self.assertRaises(twingly_search.TwinglyServerException):
                m.get('https://api.twingly.com/analytics/Analytics.ashx', text=open("./tests/fixtures/non_xml_result.xml").read())
                c = twingly_search.Client(os.environ.get('API_KEY'))
                query = c.search.query('github page-size:10')
                result = query.execute()