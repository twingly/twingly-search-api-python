from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import twingly_search


class SearchPostStream:
    def __init__(self, keyword):
        self.client = twingly_search.Client(user_agent="MyCompany/1.0")
        self.q = "sort-order:asc sort:published %s" % keyword
        self.keyword = keyword

    def each(self):
        while True:
            result = self.client.execute_query(self.q)

            for post in result.posts:
                yield post

            if result.all_results_returned():
                break

            last_published_date = result.posts[-1].published_at
            self.q = "sort-order:asc sort:published %s start-date:%s" % (self.keyword, last_published_date)


stream = SearchPostStream("(github) AND (hipchat OR slack)")
for post in stream.each():
    print(post.url.encode('utf-8'))
