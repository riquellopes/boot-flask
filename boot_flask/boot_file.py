import os
from inspect import getdoc
from boot_flask_base import BootFlaskBase, BootFlaskException


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


class BootFlaskApp(BootFlaskFile):
    __name__ = "app.py"
    __doc__ = """
        from flask import Flask, render_template
        app = Flask(__name__)
        app.config.from_object("settings")


        @app.route("/")
        def home():
            return render_template("index.html")
    """


class BootFlaskEnv(BootFlaskFile):
    __name__ = ".env"
    __doc__ = """"""


class BootFlaskHtmlIndex(BootFlaskFile):
    __name__ = "index.html"
    __doc__ = """
        <h1>Hello World</h1>
    """


class BootFlaskMain(BootFlaskFile):
    __name__ = "main.py"
    __doc__ = """
        import os
        from app import app

        if __name__ == "__main__":
            port = int(os.environ.get("PORT", 5000))
            app.run(host="0.0.0.0", port=port)
    """


class BootFlaskProcfile(BootFlaskFile):
    __name__ = "Procfile"
    __doc__ = """
        web: python main.py
    """


class BootFlaskSettings(BootFlaskFile):
    __name__ = "settings.py"
    __doc__ = """"""


class BootFlaskRequiriments(BootFlaskFile):
    __name__ = "requirements.txt"
    __doc__ = """"""

    def write(self):
        self.__doc__ = os.popen("pip freeze").read()
        super(BootFlaskRequiriments, self).write()
