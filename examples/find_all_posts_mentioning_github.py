import twingly_search
import datetime

class SearchPostStream:
    def __init__(self, keyword, language=''):
        self.client = twingly_search.Client(user_agent="MyCompany/1.0")
        self.query = self.client.query()
        self.query.pattern = "sort-order:asc sort:published %s" % keyword
        self.query.start_time = datetime.datetime.utcnow() - datetime.timedelta(hours=48)
        self.query.language = language

    def each(self):
        while True:
            result = self.query.execute()

            for post in result.posts:
                yield post

            if result.all_results_returned():
                break

            self.query.start_time = result.posts[-1].published

stream = SearchPostStream("(github) AND (hipchat OR slack)")
for post in stream.each():
    print(post.url.encode('utf-8'))