import os


class BootFlaskBase(object):

    def path_generation(self, file_name):
        return "{0}/{1}/{2}".format(os.getcwd(), self._project_name, file_name)
