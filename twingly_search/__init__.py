#!/usr/bin/env python

"""A library provides Python interface to the Twingly Search API"""
from __future__ import absolute_import

__author__ = 'Twingly AB'
__version__ = '1.0'

from .client import Client
from .errors import TwinglyAuthException
from .errors import TwinglyQueryException
from .errors import TwinglyServerException