from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class BaseConfig:
  JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
  SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')

class DevelopmentConf(BaseConfig):
  FLASK_ENV = 'development'
  DEBUG = True
  TESTING = True
  DATABASE_URI = environ.get('DEV_DATABASE_URI')

class ProductionConf(BaseConfig):
  FLASK_ENV = 'production'
  DEBUG = False
  TESTING = False
  DATABASE_URI = environ.get('PROD_DATABASE_URI')
