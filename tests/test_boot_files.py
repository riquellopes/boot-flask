import os.path
from boot_flask.boot_file import BootFlaskApp, BootFlaskRequiriments
from boot_flask.boot_directories import BootFlaskProject


def test_build_boot_flask_app():
    main = BootFlaskProject("hello")
    main.create()
    app = BootFlaskApp("hello", stop=False)
    app.write()
    assert app.__name__ == "app.py"
    assert os.path.isfile('hello/app.py')
    app.remove()
    main.destroy()


def test_requirements():
    main = BootFlaskProject("anything")
    main.create()
    app = BootFlaskRequiriments("anything", stop=False)
    app.write()
    assert app.__name__ == "requirements.txt"
    assert str("Flask") in app.__doc__
    assert os.path.isfile('anything/requirements.txt')
    app.remove()
    main.destroy()
