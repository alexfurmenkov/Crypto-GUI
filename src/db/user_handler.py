from src.db.database import engine, User

from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()
user = User('Juliya', 'public', 'private')
session.add(user)
session.commit()
