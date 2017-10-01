"""
    BootFlask

    A simple tool to make your Flask aplication quicker and fun.
"""
from setuptools import setup

setup_params = {
    "entry_points": {
        "console_scripts": [
            "bootflask=boot_flask:main"
        ]
    }
}

setup(
    author="Henrique Lopes",
    author_email="contato@henriquelopes.com.br",
    version='0.1',
    name="BootFlask",
    url="https://github.com/riquellopes/boot-flask",
    packages=["boot_flask"],
    platforms=['python >= 2.7'],
    description=__doc__,
    long_description=__doc__,
    install_requires=["Flask"],
    py_modules=["boot_flask"],
    **setup_params
)
