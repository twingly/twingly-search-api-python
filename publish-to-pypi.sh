#!/bin/sh

GENERATE_RST=true python3 setup.py sdist bdist_wheel
twine upload dist/*
