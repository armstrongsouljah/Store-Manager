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
    HOST = os.getenv('DB_HOST') #'ec2-184-73-169-151.compute-1.amazonaws.com'
    DATABASE = os.getenv('DB_NAME')  # 'dec9gdnj02hff8'
    USER =  os.getenv('DB_USER')  #'xtyhcyxhshwipn'
    PASSWORD =  os.getenv('DB_PASSWORD') #'40750512ca9a1bb9de7b8793fc4d2494caca32c156efc895cf529aa69111b39e'


env_config = dict(
    development = DevelopmentConfig,
    testing = TestingConfig,
    production = ProductionConfig
)
