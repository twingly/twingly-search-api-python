#!/bin/sh

GENERATE_RST=true python setup.py sdist bdist_wheel
twine upload dist/*
