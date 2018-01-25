import os.path
import pytest
from boot_flask import BootFlask
from boot_flask.boot_flask_base import BootFlaskException


def test_assertion_error():
    with pytest.raises(AssertionError) as e:
        BootFlask()
    assert str(e.value) == "The name project it's necessary to create app."


def test_create_project():
    backend = BootFlask("backend", type="api")
    backend.start(False)
    assert os.path.isdir("backend")
    assert os.path.isfile('backend/app/__init__.py')
    assert os.path.isfile('backend/app/api.py')
    assert os.path.isfile('backend/app/db.py')
    assert os.path.isfile('backend/app/models.py')
    assert os.path.isfile('backend/app/resources.py')
    assert os.path.isfile('backend/app/schemas.py')
    assert os.path.isfile('backend/.env')
    assert os.path.isfile('backend/Procfile')
    assert os.path.isfile('backend/Dockerfile')
    assert os.path.isfile('backend/docker-compose.yml')
    backend.project.destroy()


def _test_exist_project():
    principal = BootFlask("backend")
    principal.start(False)
    with pytest.raises(BootFlaskException) as e:
        hello = BootFlask("backend")
        hello.start(False)
    assert str(e.value) == "Exist one folder with name 'backend'."
    principal.project.destroy()
