.SILENT:

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

test: clean
	py.test -s -v tests/test_boot_flask.py
	rm -r helloworld
