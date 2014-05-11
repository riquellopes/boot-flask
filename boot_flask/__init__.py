#!/usr/bin/env python
#coding: utf-8
"""
	>>> import os.path
	>>> h = BootFlask()
	Traceback (most recent call last):
	...
	...
	AssertionError: The name of project it's necessary for create app.
	>>> f = BootFlask('helloword')
	>>> def assert_project(dirName):
	...    if os.path.isdir(dirName):
	...       print 'ok'
	...    else:
	...       print 'not ok'
	>>> f.start(False)
	>>> assert_project('helloword')
	ok
	>>> assert_project('helloword/helloword')
	not ok
	>>> g = BootFlask('helloword')
	>>> g.start(False)
	Traceback (most recent call last):
	...
	...
	BootFlaskException: Exist one folder with name 'helloword'.
	>>> def assert_file(fileName):
	... 	if os.path.isfile(fileName):
	... 		print 'ok'
	... 	else:
	... 		print 'not ok'
	>>> assert_file('helloword/Procfile')
	ok
	>>> assert_file('helloword/app.py')
	ok
	>>> assert_file('helloword/hifive.py')
	not ok
	>>> assert_file('helloword/main.py')
	ok
	>>> assert_file('helloword/settings.py')
	ok
	>>> assert_file('helloword/templates/index.html')
	ok
	>>> assert_file('helloword/.env')
	ok
	>>> def assert_dir(dirName):
	... 	if os.path.isdir(dirName):
	... 		print 'ok'
	... 	else:
	... 		print 'not ok'
	>>> assert_dir('helloword/static')
	ok
	>>> assert_dir('helloword/static/static')
	not ok
	>>> assert_dir('helloword/templates')
	ok
	>>> assert_dir('helloword/hifive')
	not ok
	>>> def assert_content(file_name, value):
	... 	content = open(file_name, 'r').read()
	... 	if value in content:
	... 		print 'ok'
	... 	else:
	... 		print 'not ok'
	>>> BootFlask._files[0].get('name')
	'Procfile'
	>>> content=''.join(BootFlask._files[0].get('content'))
	>>> assert_content("helloword/"+BootFlask._files[0].get('name'), content)
	ok
	>>> assert_content('helloword/templates/index.html', '<h1>Hello World</h1>')
	ok
	>>> import os
	>>> os.system('rm *.pyc; rm -r helloword')
	0
"""
import os
import sys
class BootFlaskException(Exception):
	pass
	
class BootFlask:
	_directories = ({'name':'static'}, {'name':'templates'})
	_files = (	{'name':'Procfile', 'content':['web: python main.py']}, 
				{'name':'app.py', 
					'content':['#coding: utf-8', 
								'from flask import Flask, render_template', 
								'app = Flask(__name__)', 
								'app.config.from_object("settings")', 
								'', 
								'@app.route("/")', 
								'def home():', 
								'\treturn render_template("index.html")']}, 
				{'name':'settings.py', 'content':['#coding: utf-8']},
				{'name':'main.py', 'content':['#coding: utf-8', 
											'import os', 
											'from app import app', 
											'', 
											'if __name__ == "__main__":', 
											'\tport = int(os.environ.get("PORT", 5000))', 
											'\tapp.run(host="0.0.0.0", port=port)']},
				{'name':'templates/index.html', 'content':['<h1>Hello World</h1>']},
				{'name':'.env', 'content':''}
	)
	
	def __init__(self, name_project=None):
		self.name_project = name_project
		assert self.name_project, "The name of project it's necessary for create app."
	
	def _create_main_package(self):
		try:
			name_package = self._generate_path()
			os.makedirs(name_package)
		except OSError as e:
			raise BootFlaskException("Exist one folder with name '{0}'.".format(self.name_project))	
			
	def _create_files(self):
		for _file in self._files:
			try:
				file_name = self._generate_path(_file.get('name'))
				handle = open(file_name, 'w+')
				handle.write( "\n".join(_file.get('content')) )
				handle.close()
			except IOError as e:
				print "Error >>>", _file.get('name')
				sys.exit(1)
				
	def _create_directories(self):
		for directory in self._directories:
			name_package = self._generate_path(directory.get('name'))
			if not os.path.isdir(name_package):
				os.makedirs(name_package)
	
	def _generate_path(self, name=""):
		import os
		return "{0}/{1}/{2}".format(os.getcwd(), self.name_project, name)
		
	def start(self, auto_exec=True):
		self._create_main_package()
		self._create_directories()
		self._create_files()
		if auto_exec:
			from subprocess import call
			call(['foreman', 'start'])
		else:
			pass
def main():
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option('-a', '--auto-exec', action="store_true", default=False)
	parser.add_option('-p', '--project-name', default='')
	(options, args) = parser.parse_args()
	
	f = BootFlask(options.project_name)
	f.start(auto_exec=options.auto_exec)
	
if __name__ == '__main__':
	main()