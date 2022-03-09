class Config(object):
    DEBUG = True
    ENV = "development"
    PORT = 8000
    # change hot to your domain if you want to deploying
    HOST = f"http://127.0.0.1:{PORT}/"

    # change SQLALCHEMY_DATABASE_URI to fit your database
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:f%40r1Zi1906@localhost:3306/url"
    SQLALCHEMY_POOL_TIMEOUT = 86400
    SQLALCHEMY_POOL_SIZE = 200
    SQLALCHEMY_POOL_RECYCLE = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ConfigProd(Config):
    DEBUG =  False
    HOST = "http://bitpy.pythonanywhere.com/"
    ENV = "production"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://bitpy:7GqpiaikKpQWg4q@bitpy.mysql.pythonanywhere-services.com/bitpy$default"
    
