from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/crypto', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    public_key = Column(String)
    private_key = Column(String)

    def __init__(self, login, public_key, private_key):
        self.login = login
        self.public_key = public_key
        self.private_key = private_key


Base.metadata.create_all(engine)
