import twingly_search, os, datetime

class SearchPostStream:
    def __init__(self, keyword, language=None):
        self.client = twingly_search.Client(os.environ.get("API_KEY"), "MyCompany/1.0")
        self.query = self.client.search.query(
                "sort-order:asc sort:published %s" % keyword,
                start_time=datetime.datetime.utcnow() - datetime.timedelta(hours=48),
                language=language)

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
    print(post.url)



