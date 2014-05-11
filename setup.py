#coding: utf-8
"""
	BootFlask::
	
	A simple tool for turn your flask project more quick and fun.
"""
import sys
from setuptools import setup

#PATH="{0}/python{1}/site-packages/".format(sys.prefix, sys.version[:3])
#print PATH
#sys.exit(1)
if sys.version_info[0] == 2 and sys.version_info[1] < 7:
	print "Sorry, BootFlask doesn't suporte python version minor that 2.7."
	sys.exit(1)

setup_params = {
	'entry_points':{
		'console_scripts':[
			'bootflask=boot_flask:main'
		]
	}
}

setup(
	author="Henrique Lopes",
	author_email="contato@henriquelopes.com.br",
	version='0.1',
	name="BootFlask",
	url="https://github.com/riquellopes/flask-hello",
	packages=['boot_flask'],
	platforms=['python >= 2.7'],
	description="A simple tool for turn your flask projects more quick and fun.",
	long_description=__doc__,
	install_requires=['Flask'],
	py_modules=['boot_flask'],
	**setup_params
)