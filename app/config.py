import datetime
import os
import secrets
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """ Project environment configurations """
    DEBUG = False
    TESTING = False
    SECRET_KEY = '2573472ee1d9542f8bcfead459b237746e6ff5c890afa7f566d744c4570ed959cbc3'
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'


class DevelopmentConfig(BaseConfig):
    """ enables development environment """
    DEBUG = True


class TestingConfig(BaseConfig):
    """ enables testing environment """
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    pass


env_config = dict(
    development = DevelopmentConfig,
    testing = TestingConfig,
    production = ProductionConfig
)
