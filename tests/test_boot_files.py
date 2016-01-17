import os.path
from boot_flask.boot_file import BootFlaskApp
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
