from __future__ import unicode_literals
import unittest

import twingly_search

class ResultTest(unittest.TestCase):
    def test_result(self):
        data = open("./tests/fixtures/valid_result.xml", 'r').read()
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r.posts, list)
        self.assertIsInstance(r.number_of_matches_returned, int)
        self.assertIsInstance(r.number_of_matches_total, int)
        self.assertIsInstance(r.seconds_elapsed, float)
        self.assertEqual(r.all_results_returned(), False)
