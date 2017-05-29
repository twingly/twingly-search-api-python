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
            raise TwinglySearchException(e)

        if 'error' == doc.tag:
            self._handle_error(doc)

        if 'twinglydata' != doc.tag:
            self._handle_non_xml_document(doc)

        return self._create_result(doc)

    def _create_result(self, data_node):
        result = Result()

        result.number_of_matches_returned = int(data_node.attrib['numberOfMatchesReturned'])
        result.seconds_elapsed = float(data_node.attrib['secondsElapsed'])
        result.number_of_matches_total = int(data_node.attrib['numberOfMatchesTotal'])
        result.incomplete_result = data_node.attrib['incompleteResult'].lower() == 'true'

        result.posts = []

        for p in data_node.findall('post'):
            result.posts.append(self._parse_post(p))

        return result

    def _parse_post(self, element):
        list_tags = {'tags': 'tag', 'links': 'link', 'images': 'image'}
        post_params = {'tags': [], 'links': [], 'images': []}
        for child in element:
            if child.tag in list_tags.keys():
                post_params[child.tag] = self._parse_list_tag(child, list_tags[child.tag])
            elif child.tag == 'coordinates':
                post_params[child.tag] = self._parse_coordinates(child)
            else:
                post_params[child.tag] = child.text

        post = Post()
        post.set_values(post_params)
        return post

    def _parse_list_tag(self, element, tag):
        list_tags = []
        for child_element in element.findall(tag):
            list_tags.append(child_element.text)
        return list_tags

    def _parse_coordinates(self, element):
        latitude_element = element.find('latitude')
        longitude_element = element.find('longitude')

        if latitude_element == None or longitude_element == None:
            return {}

        return {
            'latitude': float(latitude_element.text),
            'longitude': float(longitude_element.text),
        }

    def _handle_error(self, error_element):
        code = error_element.attrib['code']
        message = error_element.find('message').text
        error = Error(code, message)
        self._raise_error(error)

    def _raise_error(self, error):
        TwinglySearchException.from_api_response_message(error)

    def _handle_non_xml_document(self, document):
        response_text = ''.join(document.itertext())
        raise TwinglySearchException(response_text)
