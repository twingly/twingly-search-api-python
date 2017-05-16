from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

import dateutil.parser
from dateutil.tz import *

import twingly_search

"""
Simple cli that lets you search in Twingly Search API using your local timezone

Example run:
    python examples/search_using_local_timezone.py
    > What do you want to search for? cupcakes
    > Start time (in CET): 2016-02-01 00:00:00
    > End time (in CET): 2016-02-10 00:00:00
    Search results ---------------------
    Published (in CET)  - Post URL
    2016-02-09 21:38:09 - http://www.heydonna.com/2016/02/smores-cupcakes
    2016-02-09 20:21:36 - http://www.attwentynine.com/2016/02/09/chocolate-cake-cupcake
    ...
"""


class SimpleSearchCli(object):
    CURRENT_TIMEZONE = tzlocal()
    CURRENT_TIMEZONE_NAME = datetime.datetime.now(CURRENT_TIMEZONE).tzname()

    def __init__(self):
        self.client = twingly_search.Client()

    def start(self):
        # See https://developer.twingly.com/resources/search-language/
        query = self.client.query()
        query.search_query = raw_input("What do you want to search for? ")
        query.start_date = self._read_time_from_stdin("Start time")
        query.end_date = self._read_time_from_stdin("End time")
        q = query.build_query_string()

        results = self.client.execute_query(q)

        self._print_results(results)

    def _read_time_from_stdin(self, time_label):
        prompt = "%s (in %s): " % (time_label, self.CURRENT_TIMEZONE_NAME)
        user_input = raw_input(prompt)
        parsed_time = self._parse_time_in_current_timezone(user_input)
        return parsed_time

    def _parse_time_in_current_timezone(self, time_input):
        parsed_time = dateutil.parser.parse(time_input)
        # Sets your local timezone on the parsed time object.
        # If no timezone is set, twingly_search assumes UTC.
        result = parsed_time.replace(tzinfo=self.CURRENT_TIMEZONE)
        return result

    def _print_results(self, result):
        print("Search results ---------------------")
        print("Published (in %s) - Post URL" % self.CURRENT_TIMEZONE_NAME)

        for post in result.posts:
            # The time returned from the API is always in UTC,
            # convert it to your local timezone before displaying it.
            local_datetime = post.published_at.astimezone(self.CURRENT_TIMEZONE)
            published_date_string = local_datetime.strftime("%Y-%m-%d %H:%M:%S")

            print("%s - %s" % (published_date_string, post.url))


SimpleSearchCli().start()
