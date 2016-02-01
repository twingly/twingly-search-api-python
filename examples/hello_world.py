import twingly_search, os, datetime

client = twingly_search.Client(os.environ.get('API_KEY'))
query = client.search.query('"hello world"')
query.start_time = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
results = query.execute()

for post in results.posts:
    print(post.url)