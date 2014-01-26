#coding: utf-8
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
		for directory in self._directories:
			if not os.path.isdir(directory.get('name')):
				os.makedirs(directory.get('name'))
	
	def start(self):
		self._create_directories()
		self._create_files()
		command = """
		Para iniciar o processo basta executar o comando:
		>>> foreman start
		"""
		print command
		
if __name__ == '__main__':
	f = FlaskBootStrap()
	f.start()