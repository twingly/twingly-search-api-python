#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

class Result(object):
    """
    Represents a result from a Query to the Search API

    Attributes:
        number_of_matches_returned  (int) number of Post the query returned
        number_of_matches_total     (int) total number of Post the query matched
        seconds_elapsed             (float) number of seconds it took to execute the query
        posts                       (list of Post) all posts that matched the query
    """

    number_of_matches_returned = 0
    seconds_elapsed = 0.0
    number_of_matches_total = 0

    posts = []

    def __init__(self):
        pass

    def all_results_returned(self):
        """
        :return: (boolean) returns True if this result includes all Posts that matched the query
        """
        return self.number_of_matches_total == self.number_of_matches_returned

    def __repr__(self):
        matches = "@posts, "
        matches += "@number_of_matches_returned=%d, " % self.number_of_matches_returned
        matches += "@number_of_matches_total=%d, " % self.number_of_matches_total

        return "#<%s:0x%s %s>" % (self.__class__.__name__, id(self), matches)

    def __unicode__(self):
        return "Number of matches returned: %d Seconds elapsed: %.3f Number of matches total: %d" % (
            self.number_of_matches_returned,
            self.seconds_elapsed,
            self.number_of_matches_total
        )

    def __str__(self):
        return self.__unicode__()