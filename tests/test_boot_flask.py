import os.path
import pytest
from boot_flask import BootFlask
from boot_flask.boot_flask_base import BootFlaskException


def test_assertion_error():
    with pytest.raises(AssertionError) as e:
        BootFlask()
    assert str(e.value) == "The name project it's necessary to create app."


def test_create_project():
    hello = BootFlask("helloworld")
    hello.start(False)
    assert os.path.isdir("helloworld")
    assert os.path.isfile('helloworld/Procfile')
    assert os.path.isfile('helloworld/app.py')
    assert os.path.isfile('helloworld/main.py')
    assert os.path.isfile('helloworld/settings.py')
    assert os.path.isfile('helloworld/templates/index.html')
    assert os.path.isfile('helloworld/.env')
    hello.project.destroy()


def test_exist_project():
    principal = BootFlask("helloworld")
    principal.start(False)
    with pytest.raises(BootFlaskException) as e:
        hello = BootFlask("helloworld")
        hello.start(False)
    assert str(e.value) == "Exist one folder with name 'helloworld'."
    principal.project.destroy()


def test_match_content():
    def read(file_name):
        return open(file_name, "r").read()
    app = BootFlask("my_blog")
    app.start(False)
    assert read("my_blog/templates/index.html") == "<h1>Hello World</h1>"
    app.project.destroy()
