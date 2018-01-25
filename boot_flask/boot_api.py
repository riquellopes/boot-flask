from boot_flask.boot_file import BootFlaskFile
from boot_flask.boot_directories import BootDirectories
from boot_flask.boot_directories import BootFlaskProject
from boot_flask.boot_web import BootFlaskEnv, BootFlaskSettings, BootFlaskProcfile


class BootFlaskApp(BootDirectories):
    name = "app"


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


class BootFlaskProcfile(BootFlaskProcfile):
    __doc__ = """
        web: python run.py
    """


class BootFlaskRun(BootFlaskFile):
    __name__ = "run.py"
    __doc__ = """
        import os
        from app.api import app


        if __name__ == "__main__":
            port = int(os.environ.get("PORT", 5000))
            app.run(host="0.0.0.0", port=port)
    """


class BootFlaskRequiriments(BootFlaskFile):
    __name__ = "requirements.txt"
    __doc__ = """
    Flask==0.12.2
    Flask-RESTful==0.3.6
    Flask-SQLAlchemy==2.2
    marshmallow==2.13.5
    marshmallow-sqlalchemy==0.13.1
    SQLAlchemy==1.1.13
    webargs==1.8.1
    """


# TEST CONFIGURATIONS
class BootFlaskTests(BootDirectories):
    name = "tests"


class BootFlaskPyTestFile(BootFlaskFile):
    __name__ = "pytest.ini"
    __doc__ = """
        [pytest]
        norecursedirs= .git
    """


class BootFlaskTestInit(BootFlaskFile):
    __name__ = "__init__.py"
    __doc__ = """"""


class BootFlaskTestConf(BootFlaskFile):
    __name__ = "conftest.py"
    __doc__ = """
    import pytest
    from app.api import app as application
    from app.api import db


    @pytest.fixture(scope='session')
    def app(request):
        ctx = application.app_context()
        ctx.app.config['DEBUG'] = True
        ctx.app.config['TESTING'] = True
        ctx.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        ctx.push()

        def teardown():
            ctx.pop()

        request.addfinalizer(teardown)
        return application


    @pytest.fixture(scope='session')
    def test_client(app):
        return app.test_client()


    @pytest.fixture(scope='session', autouse=True)
    def build_db(app):
        db.create_all()


    @pytest.fixture(scope='function', autouse=True)
    def rollback(app, request):
        def fin():
            db.drop_all()
            db.create_all()
        request.addfinalizer(fin)
    """


class BootFlaskTestFactories(BootFlaskFile):
    __name__ = "factories.py"
    __doc__ = """
    from app.db import db
    from factory.alchemy import SQLAlchemyModelFactory as Factory
    from app.models import SampleModel


    class SampleModelFactory(Factory):
        class Meta:
            model = SampleModel
            sqlalchemy_session = db.session
    """


class BootFlaskTestSample(BootFlaskFile):
    __name__ = "test_sample.py"
    __doc__ = """
    import json
    import pytest
    from .factories import SampleModelFactory


    @pytest.fixture
    def sample_model():
        return SampleModelFactory.create_batch(3)


    def test_(test_client, sample_model):
        response = test_client.get("/v1/sample/")

        assert response.status_code == 200
        data = json.loads(response.data.decode('utf-8'))

        assert len(data.get("results")) == 3
    """

class BootFlaskDockerFile(BootFlaskFile):
    __name__ = "Dockerfile"
    __doc__ = """
    FROM python:3.7.0a4-alpine3.7

    WORKDIR /usr/src/app

    COPY . .

    RUN pip install -r requirements.txt
    """

class BootFlaskDockerCompose(BootFlaskFile):
    __name__ = "docker-compose.yml"
    __doc__ = """"
    version: '2'
    services:
        web:
            container_name: flask-api-1
            build: .
            image: flask-api
            working_dir: /usr/src/app
            command: 'python run.py'
            expose:
                - 5000
            ports:
                - 8000:5000
            volumes:
                - ./vendor:/pythonvendor
            - .:/usr/src/app
    """

class BootFlaskRequirimentsDev(BootFlaskFile):
    __name__ = "requirements_dev.txt"
    __doc__ = """
    -r requirements.txt
    ipdb==0.10.3
    ipython==6.1.0
    pytest==3.2.1
    factory-boy==2.9.2
    pytest-cov==2.5.1
    """


class BootFlaskProjectApi(BootFlaskProject):

    @classmethod
    def setup(cls, name):
        project = cls(name)
        project.add(
            BootFlaskEnv,
            BootFlaskSettings,
            BootFlaskProcfile,
            BootFlaskRun,
            BootFlaskRequiriments,
            BootFlaskRequirimentsDev,
            BootFlaskPyTestFile,
            BootFlaskTests.add(
                BootFlaskTestInit,
                BootFlaskTestConf,
                BootFlaskTestFactories,
                BootFlaskTestSample
            ),
            BootFlaskDockerCompose,
            BootFlaskDockerFile,
            BootFlaskApp.add(BootFlaskApiInit,
                             BootFlasApi,
                             BootFlaskSampleResource,
                             BootFlaskModel,
                             BootFlaskSchema,
                             BootFlaskDB)
        )
        return project

    def auto_exec(self, name):
        super(BootFlaskProjectApi, self).auto_exec("run")
