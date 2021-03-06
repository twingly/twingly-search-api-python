import os

from betamax import Betamax

with Betamax.configure() as config:
    config.cassette_library_dir = './tests/fixtures/vcr_cassettes'
    if os.environ.get('TWINGLY_SEARCH_KEY') is None:
        os.environ['TWINGLY_SEARCH_KEY'] = 'test-key'

    config.define_cassette_placeholder('<TWINGLY-API-KEY>', os.environ.get('TWINGLY_SEARCH_KEY'))
