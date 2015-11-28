import os.path
from boot_flask.boot_directories import BootFlaskStatic, BootFlaskProject


def test_build_boot_directories():
    main = BootFlaskProject("helloworld")
    main.create()

    static = BootFlaskStatic("helloworld")
    static.create()
    assert static.name == "static"
    assert os.path.isdir("helloworld/static")
    static.destroy()
    main.destroy()


def test_build_boot_main():
    main = BootFlaskProject("olamundo")
    main.create()
    assert main.name == ""
    assert os.path.isdir("olamundo")
    assert str(main) == "olamundo"
    main.destroy()
