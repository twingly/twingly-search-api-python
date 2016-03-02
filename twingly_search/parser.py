#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from twingly_search.post import Post
from twingly_search.result import Result

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from twingly_search.errors import *

class Parser:
    def parse(self, document):
        """
        Parse an API response body

        :param document: containing an API response XML
        :return: Result
        """
        try:
            doc = ET.XML(document)
        except Exception as e:
            raise TwinglyServerException(e)

        if doc.find('{http://www.twingly.com}operationResult') is not None:
            if doc.find('{http://www.twingly.com}operationResult').attrib['resultType'] == 'failure':
                self._handle_failure(doc.find('{http://www.twingly.com}operationResult'))

        if 'twinglydata' != doc.tag:
            self._handle_non_xml_document(doc)

        return self._create_result(doc)

    def _create_result(self, data_node):
        result = Result()

        result.number_of_matches_returned = int(data_node.attrib['numberOfMatchesReturned'])
        result.seconds_elapsed = float(data_node.attrib['secondsElapsed'])
        result.number_of_matches_total = int(data_node.attrib['numberOfMatchesTotal'])

        result.posts = []

        for p in data_node.findall('post[@contentType="blog"]'):
            result.posts.append(self._parse_post(p))

        return result

    def _parse_post(self, element):
        post_params = {'tags': []}
        for child in element:
            if child.tag == 'tags':
                post_params[child.tag] = self._parse_tags(child)
            else:
                post_params[child.tag] = child.text

        post = Post()
        post.set_values(post_params)
        return post

    def _parse_tags(self, element):
        tags = []
        for tag in element.findall('tag'):
            tags.append(tag.text)
        return tags

    def _handle_failure(self, failure):
        TwinglyException().from_api_response_message(failure.text)

    def _handle_non_xml_document(self, document):
        response_text = ''.join(document.itertext())
        raise TwinglyServerException(response_text)
