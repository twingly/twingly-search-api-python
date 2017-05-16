from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

import twingly_search


class SearchPostStream:
    def __init__(self, keyword, language=''):
        self.client = twingly_search.Client(user_agent="MyCompany/1.0")
        self.q = self.client.query()
        self.q.search_query = "%s sort-order:asc sort:published " % keyword
        self.q.language = language
        self.q.start_date = datetime.datetime.utcnow() - datetime.timedelta(weeks=10)
        self.keyword = keyword

    def each(self):
        while True:
            query_string = self.q.build_query_string()
            result = self.client.execute_query(query_string)

            for post in result.posts:
                yield post

            if result.all_results_returned():
                break

            last_published_date = result.posts[-1].published_at
            self.q.start_date = last_published_date


stream = SearchPostStream("(github) AND (hipchat OR slack)")
for post in stream.each():
    print(post.url.encode('utf-8'))
