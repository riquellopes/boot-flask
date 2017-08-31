import os.path
from boot_flask.boot_web import BootFlaskApp, BootFlaskRequiriments, BootFlaskProjectWeb
# from boot_flask.boot_directories import BootFlaskProject


def test_build_boot_flask_app():
    main = BootFlaskProjectWeb("hello")
    main.create()
    app = BootFlaskApp("hello", stop=False)
    app.write()
    assert app.__name__ == "app.py"
    assert os.path.isfile('hello/app.py')
    app.remove()
    main.destroy()


def test_requirements():
    main = BootFlaskProjectWeb("anything")
    main.create()
    app = BootFlaskRequiriments("anything", stop=False)
    app.write()
    assert app.__name__ == "requirements.txt"
    assert str("Flask") in app.__doc__
    assert os.path.isfile('anything/requirements.txt')
    app.remove()
    main.destroy()
