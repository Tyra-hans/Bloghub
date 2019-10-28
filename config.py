import os

class Config:
    SECRET_KEY = '1371ce8114eac4891b9b92bcea6ecd46'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tyra:password@localhost/bloghub'
    API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}