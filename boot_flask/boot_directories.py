from __future__ import absolute_import
import os
from .boot_flask_base import BootFlaskBase, BootFlaskException
from .boot_file import BootFlaskFile


class BootDirectories(BootFlaskBase):
    name = ""

    def __init__(self, project_name):
        self._project_name = project_name

    def create(self):
        name_package = self.path_generation(self.name)
        if not os.path.isdir(name_package):
            os.mkdir(name_package)

    def destroy(self):
        name_package = self.path_generation(self.name)
        if os.path.isdir(name_package):
            os.system("rm -rf %s" % name_package)

    @classmethod
    def add(cls, *args):
        for piece in args:
            if piece is not None:
                if not hasattr(cls, "__pieces__"):
                    setattr(cls, "__pieces__", [])
                getattr(cls, "__pieces__").append(piece)
        return cls

    def go(self, path=None):
        for piece in self.__pieces__:
            if issubclass(piece, BootDirectories):
                bran = piece(self._project_name)
                bran.create()
                if hasattr(bran, "__pieces__"):
                    bran.go("{0}/{1}".format(self._project_name, bran.name))
            elif issubclass(piece, BootFlaskFile):
                bran = piece(path if path else self._project_name)
                bran.write()

    def __str__(self):
        return self.name


class BootFlaskProject(BootDirectories):

    def __init__(self, project_name):
        assert project_name, "The name project it's necessary to create app."
        super(BootFlaskProject, self).__init__(project_name)

    def create(self):
        if os.path.isdir(self.path_generation(self.name)):
            raise BootFlaskException(
                "Exist one folder with name '{0}'.".format(self._project_name))
        super(BootFlaskProject, self).create()

    def go(self, path=None):
        if isinstance(self, BootFlaskProject):
            self.create()
        super(BootFlaskProject, self).go(path)

    @classmethod
    def setup(cls, name):
        return cls(name)

    def __str__(self):
        return self._project_name
