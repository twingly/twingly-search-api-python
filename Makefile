help:
	@echo "  deps        install test dependencies"
	@echo "  test        run tests"

deps:
	pip install --user --requirement test_requirements.txt
	pip install .

test:
	nosetests
