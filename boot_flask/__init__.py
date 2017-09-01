#!/usr/bin/env python
from __future__ import absolute_import
from optparse import OptionParser


from .boot_web import BootFlaskProjectWeb
from .boot_api import BootFlaskProjectApi


class BootFlask:

    def __init__(self, project_name="", type=""):
        project = BootFlaskProjectWeb
        if type == "api":
            project = BootFlaskProjectApi
        self.project = project.setup(project_name)

    def start(self, auto_exec=False):
        self.project.go()
        if auto_exec:
            self.project.auto_exec()


def main():
    parser = OptionParser()
    parser.add_option('-a', '--auto-exec', action="store_true", default=False)
    parser.add_option('-p', '--project-name', default='')
    parser.add_option('-t', '--type-project', default='web')
    (options, args) = parser.parse_args()

    boot = BootFlask(options.project_name, options.type_project)
    boot.start(auto_exec=options.auto_exec)

if __name__ == "__main__":
    main()
