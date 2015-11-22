import os.path
from boot_flask.boot_directories import BootFlaskStatic, BootFlaskProject


def test_build_boot_directories():
    static = BootFlaskStatic("helloworld")
    static.create()
    assert static.__name__ == "static"
    assert os.path.isdir("helloworld/static")
    static.destroy()


def test_build_boot_main():
    main = BootFlaskProject("olamundo")
    main.create()
    assert main.__name__ == ""
    assert os.path.isdir("olamundo")
    assert str(main) == "olamundo"
    main.destroy()
