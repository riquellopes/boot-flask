import os
from boot_flask.boot_file import BootFlaskFile
from boot_flask.boot_directories import BootFlaskProject, BootFlaskStatic, BootFlaskTemplates


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


class BootFlaskProjectWeb(BootFlaskProject):

    @classmethod
    def setup(cls, name):
        project = cls(name)
        project.add(
            BootFlaskApp,
            BootFlaskEnv,
            BootFlaskMain,
            BootFlaskProcfile,
            BootFlaskRequiriments,
            BootFlaskSettings,
            BootFlaskStatic,
            BootFlaskTemplates.add(BootFlaskHtmlIndex)
        )
        return project
