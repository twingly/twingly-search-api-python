help:
	@echo "  deps        install test dependencies"
	@echo "  test        run tests"

cideps:
	pip install --requirement test_requirements.txt

localdeps:
	pip install --user --requirement test_requirements.txt
	pip install --user --requirement requirements.txt

test:
	pytest --disable-warnings
