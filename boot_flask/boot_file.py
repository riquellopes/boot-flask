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


# API
class BootFlasApi(BootFlaskFile):
    __name__ = 'api.py'
    __doc__ = """
        from flask_restful import Api
        from app import app as application
        from app.db import db
        from app.resources import SampleResource

        def setup_app():
            db.init_app(application)

            api = Api(application, prefix="/v1")
            api.add_resource(SampleResource, "/sample/", methods=['GET'])

            return application


        app = setup_app()
    """


class BootFlaskSampleResource(BootFlaskFile):
    __name__ = "resources.py"
    __doc__ = """
        import http
        from flask import jsonify, make_response
        from flask_restful import Resource
        from webargs.flaskparser import use_args
        from app.models import SampleModel
        from app.schemas import SampleSchema
        from app.db import db


        class SampleResource(Resource):

            def get(self):
                schema = SampleSchema(many=True)
                data = schema.dump(SampleModel.query.all())
                return make_response(jsonify(results=data.data))

            @use_args(SampleSchema(strict=True, only=("name")), locations=("json", ))
            def post(self, sample_model):
                db.session.add(sample_model)
                db.session.commit()

                return make_response(
                    jsonify(mensagem="sample model saved successfully"), http.HTTPStatus.CREATED)
    """


class BootFlaskModel(BootFlaskFile):
    pass


class BootFlaskSchema(BootFlaskFile):
    pass


class BootFlaskDB(BootFlaskFile):
    pass


class BootFlaskApiInit(BootFlaskFile):
    pass
