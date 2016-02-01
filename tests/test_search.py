from __future__ import unicode_literals
import unittest
import twingly_search
import os
import requests_mock

class SearchTest(unittest.TestCase):
    def test_search_valid_result(self):
        with requests_mock.Mocker() as m:
            data = open("./tests/fixtures/valid_result.xml", 'r').read()
            if hasattr(data, 'decode'):
                data = data.decode("utf-8")
            m.get('https://api.twingly.com/analytics/Analytics.ashx', text=data)
            c = twingly_search.Client(os.environ.get('API_KEY'))
            query = c.search.query('github page-size:10')
            result = query.execute()
            self.assertEqual(result.number_of_matches_returned, len(result.posts))

    def test_search_non_blog_result(self):
        with requests_mock.Mocker() as m:
            m.get('https://api.twingly.com/analytics/Analytics.ashx', text=open("./tests/fixtures/valid_non_blog_result.xml").read())
            c = twingly_search.Client(os.environ.get('API_KEY'))
            query = c.search.query('github page-size:10')
            result = query.execute()
            self.assertEqual(len(result.posts), 1)

    def test_search_with_empty_query(self):
        with self.assertRaises(twingly_search.TwinglyQueryException):
            c = twingly_search.Client(os.environ.get('API_KEY'))
            query = c.search.query('')
            result = query.execute()