from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

import deprecation
from pytz import utc

import twingly_search
from twingly_search.constants import POST_DATE_TIME_FORMAT


class Post(object):
    """
    A blog post

    Attributes:
        url           (string) the post URL
        title         (string) the post title
        text          (string) the blog post text
        summary       (string) DEPRECATED - see text
        language_code (string) ISO two letter language code for the language that the post was written in
        published_at  (datetime.datetime) the time, in UTC, when this post was published
        published     (datetime.datetime) DEPRECATED - see published_at
        indexed_at    (datetime.datetime) the time, in UTC, when this post was indexed by Twingly
        indexed       (datetime.datetime) DEPRECATED - see indexed_at
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
        coordinates   (dict) DEPRECATED - see latitude and longitude
        latitude      (float) latitude coordinate
        longitude     (float) longitude coordinate
    """

    def __init__(self):
        self.DEFAULT_DATE = self._parse_time("1970-01-01T00:00:00Z")
        self.url = ''
        self.title = ''
        self.text = ''
        self.language_code = ''
        self.published_at = self.DEFAULT_DATE
        self.indexed_at = self.DEFAULT_DATE
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
        self.reindexed_at = self.DEFAULT_DATE
        self.links = []
        self.images = []
        self.coordinates = ''
        self.latitude = None
        self.longitude = None

    @property
    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Use 'indexed_at' field instead")
    def indexed(self):
        return self.indexed_at

    @property
    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Use 'published_at' field instead")
    def published(self):
        return self.published_at

    @property
    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Use 'text' field instead")
    def summary(self):
        return self.text

    def set_values(self, params):
        """
        Sets all instance variables for the Post, given a dict.

        :param params: (dict) containing blog post data
        """
        self.url = params.get("url", "") or ""
        self.title = params.get("title", "") or ""
        self.text = params.get("text", "") or ""
        self.language_code = params.get("languageCode", "") or ""
        self.published_at = self._parse_time(params["publishedAt"]) or self.DEFAULT_DATE
        self.indexed_at = self._parse_time(params["indexedAt"]) or self.DEFAULT_DATE
        self.blog_url = params.get("blogUrl", "") or ""
        self.blog_name = params.get("blogName", "") or ""
        self.blog_id = params.get("blogId", "") or ""
        self.authority = int(params["authority"])
        self.blog_rank = int(params["blogRank"])
        self.tags = params.get("tags", [])
        self.id = params.get("id", "") or ""
        self.author = params.get("author", "") or ""
        self.location_code = params.get("locationCode", "") or ""
        self.inlinks_count = int(params["inlinksCount"])
        self.reindexed_at = self._parse_time(params["reindexedAt"]) or self.DEFAULT_DATE
        self.links = params.get("links", [])
        self.images = params.get("images", [])
        self.coordinates = params.get("coordinates", {})
        self.latitude = self.coordinates.get("latitude", None)
        self.longitude = self.coordinates.get("longitude", None)

    def _parse_time(self, time):
        parsed_time = datetime.datetime.strptime(time, POST_DATE_TIME_FORMAT)
        return utc.localize(parsed_time)

    def __unicode__(self):
        return "%s %s" % (self.title, self.url)

    def __str__(self):
        return self.__unicode__()
