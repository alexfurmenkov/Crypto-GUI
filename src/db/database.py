from sqlalchemy import create_engine  # Импорт функции, выполняющей TCP/IP соеднение с БД

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/crypto', echo=True)  # Соеднение с БД под названием crypto
