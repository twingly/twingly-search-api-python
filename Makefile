help:
	@echo "  deps        install test dependencies"
	@echo "  test        run tests"

testdeps:
	pip install --user --requirement test_requirements.txt

deps: testdeps
	pip install --user --requirement requirements.txt

test:
	nosetests
