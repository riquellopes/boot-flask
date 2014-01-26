#coding: utf-8
"""
	>>> import os.path
	>>> f = FlaskBootStrap()
	>>> f.start(False)
	>>> if os.path.isfile('Procfile'):
	... 	print 'ok'
	... else:
	... 	print 'not ok'
	ok
	>>> if os.path.isdir('static'):
	... 	print 'ok'
	... else:
	... 	print 'not ok'
	ok
	>>> content = open('Procfile', 'r').read()
	>>> if 'web: python main.py' in content:
	... 	print 'ok'
	... else:
	... 	print 'not ok'
	ok
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
				{'name':'templates/index.html', 'content':['<h1>Hello World</h1>']}
	)
	
	def _create_files(self):
		"""
			Método cria os arquivos.
		"""
		for _file in self._files:
			try:
				handle = open(_file.get('name'), 'w+')
				handle.write( "\n".join(_file.get('content')) )
				handle.close()
			except IOError:
				print "Erro ao criar arquivo. >>>", _file.get('name')
				sys.exit(1)
				
	def _create_directories(self):
		"""
			Método cria diretórios básicos do projeto.
		"""
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
			#print 'Para iniciar o processo use o comando:\n>>> foreman start'
if __name__ == '__main__':
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option('-a', '--auto-exec', action="store_true", default=False)
	(options, args) = parser.parse_args()
	
	f = FlaskBootStrap()
	f.start(auto_exec=options.auto_exec)