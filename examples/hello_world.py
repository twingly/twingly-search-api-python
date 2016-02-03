import twingly_search
import datetime

client = twingly_search.Client()
query = client.query()
query.pattern = '"hello world"'
query.start_time = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
results = query.execute()

for post in results.posts:
    print(post.url)
