import datetime
import os
import secrets
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """ Project environment configurations """
    DEBUG = False
    TESTING = False
    # SECRET_KEY = '2573472ee1d9542f8bcfead459b237746e6ff5c890afa7f566d744c4570ed959cbc3'
    JWT_SECRET_KEY = '2573472ee1d9542f8bcfead459b237746e6ff5c890afa7f566d744c4570ed959cbc3'
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


class DevelopmentConfig(BaseConfig):
    """ enables development environment """
    ENV = 'development'
    DATABASE = 'storemanager'
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    """ enables testing environment """
    ENV = 'testing'
    DATABASE = 'store_manager_test'
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    HOST = 'ec2-184-73-169-151.compute-1.amazonaws.com'
    DATABASE = 'dec9gdnj02hff8'
    USER = 'xtyhcyxhshwipn'
    PASSWORD = '40750512ca9a1bb9de7b8793fc4d2494caca32c156efc895cf529aa69111b39e'
    # DATABASE_URI = 'postgres://xtyhcyxhshwipn:40750512ca9a1bb9de7b8793fc4d2494caca32c156efc895cf529aa69111b39e@ec2-184-73-169-151.compute-1.amazonaws.com:5432/dec9gdnj02hff8?sslmode=require'


env_config = dict(
    development = DevelopmentConfig,
    testing = TestingConfig,
    production = ProductionConfig
)
