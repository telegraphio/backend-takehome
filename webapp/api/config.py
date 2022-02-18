import os


class Config:
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class DevelopmentConfig(Config):
    # for example, 'postgresql://candidate:password123@localhost:5432/takehome'
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']


config_dict = {"DEVELOPMENT": DevelopmentConfig, "default": DevelopmentConfig}
