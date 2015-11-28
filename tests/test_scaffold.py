import os.path
from boot_flask.boot_directories import (
    BootFlaskStatic, BootFlaskProject, BootFlaskTemplates)
from boot_flask.boot_file import BootFlaskHtmlIndex


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
