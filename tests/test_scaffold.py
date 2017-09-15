import os.path
from boot_flask.boot_directories import BootFlaskProject
from boot_flask.boot_web import BootFlaskHtmlIndex, BootFlaskStatic, BootFlaskTemplates


def test_scaffold():
    project = BootFlaskProject("blog")
    project.add(
        BootFlaskStatic, BootFlaskTemplates.add(BootFlaskHtmlIndex)
    )
    project.go()
    assert os.path.isdir("blog")
    assert os.path.isdir("blog/static")
    assert os.path.isfile("blog/templates/index.html")
    project.destroy()
