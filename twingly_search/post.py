from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

from pytz import utc


class Post(object):
    """
    A blog post

    Attributes:
        url           (string) the post URL
        title         (string) the post title
        text          (string) the blog post text
        language_code (string) ISO two letter language code for the language that the post was written in
        published_at  (datetime.datetime) the time, in UTC, when this post was published
        indexed_at    (datetime.datetime) the time, in UTC, when this post was indexed by Twingly
        blog_url      (string) the blog URL
        blog_name     (string) name of the blog
        blog_rank     (int) the rank of the blog, based on authority and language
                      (https://developer.twingly.com/resources/search/#authority)
        blog_id       (string) the ID of the blog
        authority     (int) the blog's authority/influence
                      (https://developer.twingly.com/resources/search/#authority)
        tags          (list of string) tags
        id            (string) the post ID
        location_code (string) ISO two letter location code
                      (https://developer.twingly.com/resources/search-language/#supported-locations)
        inlinks_count (int) amount of the inlinks
        reindexed_at  (datetime.datetime) the time, in UTC, when this post was re-indexed by Twingly
        links         (list of string) links
        images        (list of string) images
        coordinates   (string) coordinates
                              
    """

    def __init__(self):
        self.url = ''
        self.title = ''
        self.text = ''
        self.language_code = ''
        self.published_at = self._parse_time("1970-01-01T00:00:00Z")
        self.indexed_at = self._parse_time("1970-01-01T00:00:00Z")
        self.blog_url = ''
        self.blog_name = ''
        self.blog_id = ''
        self.authority = 0
        self.blog_rank = 0
        self.tags = []
        self.id = ''
        self.author = ''
        self.location_code = ''
        self.inlinks_count = 0
        self.reindexed_at = self._parse_time("1970-01-01T00:00:00Z")
        self.links = []
        self.images = []
        self.coordinates = ''

    def set_values(self, params):
        """
        Sets all instance variables for the Post, given a dict.

        :param params: (dict) containing blog post data
        """
        self.url = params['url']
        self.title = params['title']
        self.text = params['text']
        self.language_code = params['languageCode']
        self.published_at = self._parse_time(params['publishedAt'])
        self.indexed_at = self._parse_time(params['indexedAt'])
        self.blog_url = params['blogUrl']
        self.blog_name = params['blogName']
        self.blog_id = params['blogId']
        self.authority = int(params['authority'])
        self.blog_rank = int(params['blogRank'])
        self.tags = params['tags']
        self.id = params['id']
        self.author = params['author']
        self.location_code = params['locationCode']
        self.inlinks_count = int(params['inlinksCount'])
        self.reindexed_at = self._parse_time(params['reindexedAt'])
        self.links = params['links']
        self.images = params['images']
        self.coordinates = params['coordinates']

    def _parse_time(self, time):
        parsed_time = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
        return utc.localize(parsed_time)

    def __unicode__(self):
        return "%s %s" % (self.title, self.url)

    def __str__(self):
        return self.__unicode__()
