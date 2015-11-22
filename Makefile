.SILENT:

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

test: clean
	rm -r helloworld
	py.test -s -v tests/*
