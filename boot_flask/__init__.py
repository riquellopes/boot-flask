#!/usr/bin/env python
from __future__ import absolute_import
from optparse import OptionParser
from subprocess import call
from .boot_directories import (
    BootFlaskStatic, BootFlaskProject, BootFlaskTemplates)
from .boot_file import (
    BootFlaskApp, BootFlaskEnv, BootFlaskHtmlIndex, BootFlaskMain,
    BootFlaskProcfile, BootFlaskSettings, BootFlaskRequiriments)


class BootFlask:

    def __init__(self, project_name=""):
        self.project = BootFlaskProject(project_name)
        self.project.add(
            BootFlaskApp,
            BootFlaskEnv,
            BootFlaskMain,
            BootFlaskProcfile,
            BootFlaskRequiriments,
            BootFlaskSettings,
            BootFlaskStatic,
            BootFlaskTemplates.add(BootFlaskHtmlIndex)
        )

    def start(self, auto_exec=False):
        self.project.go()
        if auto_exec:
            call(["python", "app.py"])


def main():
    parser = OptionParser()
    parser.add_option('-a', '--auto-exec', action="store_true", default=False)
    parser.add_option('-p', '--project-name', default='')
    (options, args) = parser.parse_args()

    boot = BootFlask(options.project_name)
    boot.start(auto_exec=options.auto_exec)

if __name__ == "__main__":
    main()
