#!/usr/bin/env python
from .boot_directories import (
    BootFlaskStatic, BootFlaskProject, BootFlaskTemplates)
from .boot_file import (
    BootFlaskApp, BootFlaskEnv, BootFlaskHtmlIndex, BootFlaskMain,
    BootFlaskProcfile, BootFlaskSettings)


class BootFlask(object):

    def __init__(self, project_name):
        self.project = BootFlaskProject(project_name)
        self.project.add(
            BootFlaskApp,
            BootFlaskEnv,
            BootFlaskMain,
            BootFlaskProcfile,
            BootFlaskSettings,
            BootFlaskStatic,
            BootFlaskTemplates.add(BootFlaskHtmlIndex)
        )
        self.project.go()

    def start(self, auto_exec=False):
        pass
