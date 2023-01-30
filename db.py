import toml

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def get_db():
    config = toml.load('config.toml')
    db_host = config['database']['DB_HOST']
    db_port = config['database']['DB_PORT']
    db_name = config['database']['DB_SCHEMA_NAME']
    db_user_name = config['database']['DB_USER_NAME']
    db_pwd = config['database']['DB_PWD']
    db_args = config['database']['DB_ARGS']
    DATABASE_URL = f"mysql+pymysql://{db_user_name}:{db_pwd}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(DATABASE_URL)
    session = sessionmaker(engine)
    return session()