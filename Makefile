help:
	@echo "  deps        install test dependencies"
	@echo "  test        run tests"

deps:
	pip install -r test_requirements.txt

test:
	nosetests
