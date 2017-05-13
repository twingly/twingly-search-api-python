#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class Result(object):
    """
    Represents a result from a Query to the Search API

    Attributes:
        number_of_matches_returned (int) number of Posts the Query returned
        number_of_matches_total    (int) total number of Posts the Query matched
        seconds_elapsed            (float) number of seconds it took to execute the Query
        posts                      (list of Post) all Posts that matched the Query
    """

    def __init__(self):
        self.number_of_matches_returned = 0
        self.number_of_matches_total = 0
        self.seconds_elapsed = 0.0
        self.incomplete_result = False
        self.posts = []

    def all_results_returned(self):
        """
        :return: (boolean) returns True if this result includes all Posts that
            matched the query, False if there are more Posts to fetch from the API
        """
        return self.number_of_matches_total == self.number_of_matches_returned

    def __repr__(self):
        matches = "posts, "
        matches += "number_of_matches_returned=%d, " % self.number_of_matches_returned
        matches += "number_of_matches_total=%d" % self.number_of_matches_total

        return "#<%s:0x%s %s>" % (self.__class__.__name__, id(self), matches)

    def __unicode__(self):
        return "Number of matches returned: %d Seconds elapsed: %.3f Number of matches total: %d" % (
            self.number_of_matches_returned,
            self.seconds_elapsed,
            self.number_of_matches_total
        )

    def __str__(self):
        return self.__unicode__()
