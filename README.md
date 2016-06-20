# Twingly Search API Python

[![Build Status](https://travis-ci.org/twingly/twingly-search-api-python.png?branch=master)](https://travis-ci.org/twingly/twingly-search-api-python)

A Python library for Twingly's Search API (previously known as Analytics API). Twingly is a blog search service that provides a searchable API known as [Twingly Search API](https://developer.twingly.com/resources/search/).

## Installation

Install via PyPI

```shell
pip install twingly-search
```

Or add `twingly-search` to your application's [requirements file](https://pip.pypa.io/en/stable/user_guide/#requirements-files) and then run

```shell
pip install -r requirements.txt
```

Or from source code

```shell
git clone https://github.com/twingly/twingly-search-api-python.git
cd twingly-search-api-python
python setup.py install
```

## Usage

```python
from twingly_search import Client

client = Client()

query = client.query()
query.pattern = 'github page-size:10'
query.language = 'sv'

# Assumes UTC if no timezone is specified
query.start_time = datetime.datetime(2015, 2, 23, 15, 18, 13)

result = query.execute()

for post in result.posts:
    print post.url
```

Example code can be found in [examples/](examples/).

The `twingly_search` library talks to a commercial blog search API and requires an API key. Best practice is to set the `TWINGLY_SEARCH_KEY` environment variable to the obtained key. `twingly_search.Client` can be passed a key at initialization if your setup does not allow environment variables.

To learn more about the capabilities of the API, please read the [Twingly Search API documentation](https://developer.twingly.com/resources/search/).

### Documentation

`twingly_search` is documented with [pydoc](https://docs.python.org/2/library/pydoc.html). To read the documentation directly in your console you can run

```shell
pydoc twingly_search
```

or you can start a local pydoc web server with

```shell
pydoc -p 1234 twingly_search
```

In this case documentation will be available at [http://localhost:1234/twingly_search.html](http://localhost:1234/twingly_search.html)

## Requirements

* API key, [sign up](https://www.twingly.com/try-for-free) via [twingly.com](https://www.twingly.com/) to get one
* Python 2.7+, 3.0+ with [SNI] support, see [Requests FAQ] for more information

[SNI]: https://en.wikipedia.org/wiki/Server_Name_Indication
[Requests FAQ]: http://docs.python-requests.org/en/master/community/faq/#what-are-hostname-doesn-t-match-errors

## Development

### Tests

Install the tests dependencies

    make deps

Run the tests

    make test

### Release

To be able to publish the package, create a [.pypirc file] containing your pypi username an password.

You will need pandoc to convert README.md to reStructuredText:

    brew install pandoc
    pip install pypandoc

Bump the version in [setup.py](./setup.py) and [\__init\__.py](./twingly-search/__init__.py).

Publish to [PyPi]:

    ./publish-to-pypi.sh

[PyPi]: https://pypi.python.org/pypi/twingly-search
[.pypirc file]: https://docs.python.org/2/distutils/packageindex.html#pypirc

## License

The MIT License (MIT)

Copyright (c) 2016 Twingly AB

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
