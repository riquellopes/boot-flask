from __future__ import unicode_literals
import os
import sys


class BootFlaskBase:
    """
    """

    def __int__(self, project_name):
        self._project_name = project_name

    def write(self):
        try:
            file_name = self.path_generation()
            handle = open(file_name, "w+")
            handle.write()
            handle.close()
        except IOError as e:
            print "Error >>> %s" % str(e.exception)
            sys.exit(1)

    def path_generation(self, file_name):
        return "{0}/{1}/{2}".format(os.getcwd(), self._project_name, file_name)


class BootFlaskApp(BootFlaskBase):
    """
        from flask import Flask, render_template
        app = Flask(__name__)
        app.config.from_object("settings")

        @app.route("/")
        def home():
            return render_template("index.html")
    """


class BootFlaskEnv(BootFlaskBase):
    """
    """


class BootFlaskIndex(BootFlaskBase):
    """
        <h1>Hello World</h1>
    """


class BootFlaskMain(BootFlaskBase):
    """
        import os
        from app import app

        if __name__ == "__main__":
            port = int(os.environ.get("PORT", 5000))
            app.run(host="0.0.0.0", port=port)
    """


class BootFlaskProcfile(BootFlaskBase):
    """
        web: python main.py
    """


class BootFlaskSettings(BootFlaskBase):
    """
    """
