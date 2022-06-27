import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:1234@localhost:5432/postgres_db'  
        #  'sqlite:///' + os.path.join(basedir, 'app.db')
        
    # Postgres db connection format: 'postgresql://username:password@hostname:port/dbname'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = os.getenv('REDIS_SERVER', 'localhost')
    CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_DB = 0
    CACHE_REDIS_URL = "redis://"+CACHE_REDIS_HOST+":6379/0"
    CACHE_DEFAULT_TIMEOUT = 3300