#coding: utf-8
"""
	>>> import os.path
	>>> f = FlaskBootStrap()
	>>> f.start(False)
	>>> def assert_file(fileName):
	... 	if os.path.isfile(fileName):
	... 		print 'ok'
	... 	else:
	... 		print 'not ok'
	>>> assert_file('Procfile')
	ok
	>>> assert_file('app.py')
	ok
	>>> assert_file('hifive.py')
	not ok
	>>> assert_file('main.py')
	ok
	>>> assert_file('settings.py')
	ok
	>>> assert_file('templates/index.html')
	ok
	>>> assert_file('.env')
	ok
	>>> def assert_dir(dirName):
	... 	if os.path.isdir(dirName):
	... 		print 'ok'
	... 	else:
	... 		print 'not ok'
	>>> assert_dir('static')
	ok
	>>> assert_dir('templates')
	ok
	>>> assert_dir('hifive')
	not ok
	>>> def assert_content(file_name, value):
	... 	content = open(file_name, 'r').read()
	... 	if value in content:
	... 		print 'ok'
	... 	else:
	... 		print 'not ok'
	>>> FlaskBootStrap._files[0].get('name')
	'Procfile'
	>>> content=''.join(FlaskBootStrap._files[0].get('content'))
	>>> assert_content(FlaskBootStrap._files[0].get('name'), content)
	ok
	>>> assert_content('templates/index.html', '<h1>Hello World</h1>')
	ok
	>>> import os
	>>> os.system('rm *.pyc; rm -r static; rm -r templates; rm settings.py; rm main.py; rm app.py; rm Procfile; rm .env')
	0
"""
import os
import sys
class FlaskBootStrap:
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
	
	def _create_files(self):
		for _file in self._files:
			try:
				handle = open(_file.get('name'), 'w+')
				handle.write( "\n".join(_file.get('content')) )
				handle.close()
			except IOError:
				print "Error >>>", _file.get('name')
				sys.exit(1)
				
	def _create_directories(self):
		for directory in self._directories:
			if not os.path.isdir(directory.get('name')):
				os.makedirs(directory.get('name'))
	
	def start(self, auto_exec=True):
		self._create_directories()
		self._create_files()
		if auto_exec:
			from subprocess import call
			call(['foreman', 'start'])
		else:
			pass
if __name__ == '__main__':
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option('-a', '--auto-exec', action="store_true", default=False)
	(options, args) = parser.parse_args()
	
	f = FlaskBootStrap()
	f.start(auto_exec=options.auto_exec)