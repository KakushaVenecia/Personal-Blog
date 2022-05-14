import os

class Config:
  
    SECRET_KEY = os.environ.get('SECRET_KEY')
    


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'

class ProdConfig(Config):
     # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'
    pass


class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
