import twingly_search
import datetime
import pytz

client = twingly_search.Client()
query = client.query()
query.pattern = '"hello world"'
query.start_time = datetime.datetime.now(pytz.utc) - datetime.timedelta(hours=1)
results = query.execute()

for post in results.posts:
    print(post.url)
