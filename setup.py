#!/usr/bin/env python

'''The setup and build script for the twingly-search library.'''

import os

from setuptools import setup, find_packages

if 'GENERATE_RST' in os.environ:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
else:
    readme_file = open('README.md', 'r')
    long_description = readme_file.read()
    readme_file.close()

with open('requirements.txt') as fp:
    install_requires = fp.readlines()

setup(
    name='twingly-search',
    version='2.1.4',
    author='Twingly AB',
    author_email='support@twingly.com',
    license='MIT',
    url='https://github.com/twingly/twingly-search-api-python',
    keywords='twingly',
    description='Python library for Twingly Search API',
    long_description=long_description,
    packages=find_packages(exclude=['tests*']),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
