from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import twingly_search

client = twingly_search.Client()
q = '"hello world" tspan:24h'
results = client.execute_query(q)

for post in results.posts:
    print(post.url)
