from __future__ import unicode_literals
import unittest

import datetime

import twingly_search

try:
    unicode = unicode
except NameError:
    basestring = (str,bytes)
else:
    basestring = basestring

class PostTest(unittest.TestCase):
    def test_post(self):
        data = open("./tests/fixtures/valid_result.xml", 'r').read()
        r = twingly_search.Parser().parse(data)
        p = r.posts[0]
        self.assertIsInstance(p.url, basestring)
        self.assertIsInstance(p.title, basestring)
        self.assertIsInstance(p.summary, basestring)
        self.assertIsInstance(p.language_code, basestring)
        self.assertIsInstance(p.published, datetime.datetime)
        self.assertIsInstance(p.indexed, datetime.datetime)
        self.assertIsInstance(p.blog_url, basestring)
        self.assertIsInstance(p.blog_name, basestring)
        self.assertIsInstance(p.authority, int)
        self.assertIsInstance(p.blog_rank, int)
        self.assertIsInstance(p.tags, list)