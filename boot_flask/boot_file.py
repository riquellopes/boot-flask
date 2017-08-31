import os
from inspect import getdoc
from boot_flask_base import BootFlaskBase, BootFlaskException


# WEB
class BootFlaskFile(BootFlaskBase):
    __name__ = ""
    __doc__ = """"""

    def __init__(self, project_name, stop=True):
        self._project_name = project_name
        self._stop = stop
        self._content = getdoc(self)

    def write(self):
        try:
            file_name = self.path_generation(self.__name__)
            handle = open(file_name, "w+")
            handle.write(str(self._content))
            handle.close()
        except IOError as e:
            raise BootFlaskException(e.message)

    def remove(self):
        file_name = self.path_generation(self.__name__)
        if os.path.isfile(file_name):
            os.remove(file_name)
