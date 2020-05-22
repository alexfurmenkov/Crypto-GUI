from sqlalchemy import Column, Integer, String  # Импорт необходимых класслв
from src.db.database import engine  # Импорт соединения с БД, которое было установлено в файле src.db.database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker  # Импорт функции, создающуей сесии работы с БД

import rsa  # Импорт библиотеки rsa

Base = declarative_base()


class User(Base):
    """
    Класс User, который являетеся отображением таблицы users в БД
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)  # Создание атрибутов класса User, которые являютеся отображением
    login = Column(String)                  # колонок в таблице users
    public_key = Column(String)
    private_key = Column(String)

    def __init__(self, login, public_key, private_key):
        """
        Метод, вызываемый каждый раз при создании объекта класса User
        :param login: Логин
        :param public_key: Путь к публичному ключу
        :param private_key: Путь к приватному ключу
        """
        self.login = login
        self.public_key = public_key
        self.private_key = private_key

    def get_public_key(self):
        """
        Метод, возвращающий публичный ключ объекта класса User
        :return: объекта класса PublicKey
        """
        with open(self.public_key, 'rb') as file:
            public_key = file.read()
            return rsa.PublicKey.load_pkcs1(keyfile=public_key)

    def get_private_key(self):
        """
        Метод, возвращающий приватный ключ объекта класса User
        :return: объекта класса PrivateKey
        """
        with open(self.private_key, 'rb') as file:
            private_key = file.read()
            return rsa.PrivateKey.load_pkcs1(keyfile=private_key)


Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()  # Открытие сессии подключения к БД
user = User('Juliya', 'public', 'private')  # Создание нового объекта класса User
session.add(user)  # Добавляет нового пользователя
session.commit()  # Сохраняет нового пользователя
