from boot_flask.boot_file import BootFlaskFile


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
    __name__ = "models.py"
    __doc__ = """
        from app.db import db

        class SampleModel(db.Model):
            id = db.Column(db.Integer, primary_key=True, autoincrement=True)
            name = db.Column(db.String(100), nullable=False, unique=True)
    """


class BootFlaskSchema(BootFlaskFile):
    __name__ = "schemas.py"
    __doc__ = """
        from marshmallow import fields
        from marshmallow_sqlalchemy import ModelSchema
        from app.models import SampleModel
        from app.db import db

        class SampleSchema(ModelSchema):
            class Meta:
                model = SampleModel
                sqla_session = db.session
    """


class BootFlaskDB(BootFlaskFile):
    __name__ = "db.py"
    __doc__ = """
        from flask_sqlalchemy import SQLAlchemy

        db = SQLAlchemy()
    """


class BootFlaskApiInit(BootFlaskFile):
    __name__ = "__init__.py"
    __doc__ = """
        from flask import Flask

        app = Flask(__name__)
        app.config.from_object("settings")
    """
