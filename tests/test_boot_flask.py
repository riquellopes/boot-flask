import os.path
import pytest
from boot_flask import BootFlask, BootFlaskException


def test_assertion_error():
    with pytest.raises(AssertionError) as e:
        BootFlask()
    assert str(e.value) == "The name of project it's necessary for create app."


def test_create_project():
    hello = BootFlask("helloworld")
    hello.start(False)
    assert os.path.isdir("helloworld")


def test_projet_does_not_exist():
    assert not os.path.isdir("helloworld/helloworld")


def test_exist_project():
    with pytest.raises(BootFlaskException) as e:
        hello = BootFlask("helloworld")
        hello.start(False)
    assert str(e.value) == "Exist one folder with name 'helloworld'."


def test_match_files():
    assert os.path.isfile('helloworld/Procfile')
    assert os.path.isfile('helloworld/app.py')
    assert os.path.isfile('helloworld/main.py')
    assert os.path.isfile('helloworld/settings.py')
    assert os.path.isfile('helloworld/templates/index.html')
    assert os.path.isfile('helloworld/.env')


def test_match_content():
    def read(file_name):
        return open(file_name, "r").read()
    assert read("helloworld/templates/index.html") == "<h1>Hello World</h1>"
