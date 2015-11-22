import os
from boot_flask_base import BootFlaskBase
from boot_file import BootFlaskFile
from . import BootFlaskException


class BootDirectories(BootFlaskBase):
    name = ""

    def __init__(self, project_name):
        self._project_name = project_name

    def create(self):
        name_package = self.path_generation(self.name)
        if not os.path.isdir(name_package):
            os.makedirs(name_package)

    def destroy(self):
        name_package = self.path_generation(self.name)
        if os.path.isdir(name_package):
            os.removedirs(name_package)

    @classmethod
    def add(cls, *args):
        for piece in args:
            if piece is not None:
                if not hasattr(cls, "__pieces__"):
                    setattr(cls, "__pieces__", [])
                getattr(cls, "__pieces__").append(piece)
        return cls

    def go(self):
        for piece in self.__pieces__:
            if issubclass(piece, BootDirectories):
                bran = piece(self._project_name)
                bran.create()
                if hasattr(bran, "__pieces__"):
                    # @TODO Salvar no diretorio correto.
                    bran.go()
            elif issubclass(piece, BootFlaskFile):
                bran = piece(self._project_name)
                bran.write()

    def __str__(self):
        return self.name


class BootFlaskStatic(BootDirectories):
    name = "static"


class BootFlaskTemplates(BootDirectories):
    name = "templates"


class BootFlaskProject(BootDirectories):

    def __init__(self, project_name):
        assert project_name, "The name project it's necessary to create app."
        super(BootFlaskProject, self).__init__(project_name)

    def create(self):
        if os.path.isdir(self.path_generation(self.name)):
            raise BootFlaskException(
                "Exist one folder with name '{0}'.".format(self._project_name))
        super(BootFlaskProject, self).create()

    def __str__(self):
        return self._project_name
