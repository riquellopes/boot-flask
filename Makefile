.SILENT:

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

test: clean
	PYTHONPATH=boot_flask  py.test -s -v --cov=boot_flask tests/*
