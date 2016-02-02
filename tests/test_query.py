from __future__ import unicode_literals
import unittest

import datetime
import requests_mock

import twingly_search
import os

class QueryTest(unittest.TestCase):
    def test_query_new(self):
        q = twingly_search.Client(os.environ.get('API_KEY')).query()
        self.assertIsInstance(q, twingly_search.Query)

    def test_query_without_client(self):
        with self.assertRaises(Exception):
            q = twingly_search.Query()

    def test_query_with_valid_pattern(self):
        q = twingly_search.Client(os.environ.get('API_KEY')).query()
        q.pattern = "christmas"
        self.assertIn("xmloutputversion=2", q.url())

    def test_query_without_valid_pattern(self):
        with self.assertRaises(twingly_search.TwinglyQueryException):
            q = twingly_search.Client(os.environ.get('API_KEY')).query()
            q.url()

    def test_query_with_empty_pattern(self):
        with self.assertRaises(twingly_search.TwinglyQueryException):
            q = twingly_search.Client(os.environ.get('API_KEY')).query()
            q.pattern = ""
            q.url()

    def test_query_should_add_language(self):
        q = twingly_search.Client(os.environ.get('API_KEY')).query()
        q.pattern = "spotify"
        q.language = "en"
        self.assertEqual(q.request_parameters()['documentlang'], "en")

    def test_query_should_add_start_time(self):
        q = twingly_search.Client(os.environ.get('API_KEY')).query()
        q.pattern = "spotify"
        q.start_time = datetime.datetime(2012, 12, 28, 9, 01, 22)
        self.assertEqual(q.request_parameters()['ts'], "2012-12-28 09:01:22")

    def test_query_should_add_end_time(self):
        q = twingly_search.Client(os.environ.get('API_KEY')).query()
        q.pattern = "spotify"
        q.end_time = datetime.datetime(2012, 12, 28, 9, 01, 22)
        self.assertEqual(q.request_parameters()['tsTo'], "2012-12-28 09:01:22")

    def test_query_should_encode_url_parameters(self):
        q = twingly_search.Client(os.environ.get('API_KEY')).query()
        q.pattern = "spotify"
        q.end_time = datetime.datetime(2012, 12, 28, 9, 01, 22)
        self.assertIn("tsTo=2012-12-28+09%3A01%3A22", q.url_parameters())

    def test_query_pattern(self):
        q = twingly_search.Client(os.environ.get('API_KEY')).query()
        q.pattern = "spotify"
        self.assertIn("searchpattern=spotify", q.url_parameters())

    def test_query_when_searching_for_spotify(self):
        q = twingly_search.Client(os.environ.get('API_KEY')).query()
        q.pattern = "spotify page-size:10"
        q.language = "en"
        r = q.execute()
        self.assertGreater(len(r.posts), 0)