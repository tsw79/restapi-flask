from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from api.models.db import init_db
from flask_restful import Api
from api.routes.routes import init_routes
from api.resources.errors import errors

app = Flask(__name__)
app.config.from_object('config.ProductionConf')

api = Api(app)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

init_db(app)
init_routes(api)

app.run()