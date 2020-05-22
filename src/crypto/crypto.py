import rsa  # Импорт библиотеки rsa, с помощью функций которой будут сгенерированы ключи


class Crypto:
    """
    Класс Crypto, который служит для совершения криптографических операций
    """

    def __init__(self, public_key=None, private_key=None):
        """
        Метод, вызываемый при создании объекта класса Crypto
        Изначально аттрибуты public_key и private_key равны None
        :param public_key: Публичный ключ
        :param private_key: Приватный ключ
        """
        self.public_key = public_key
        self.private_key = private_key

    def generate_keys(self):
        """
        Метод, генерирующий пару ключей и сохраняющий в файл
        :return: Tuple (public_key, private_key)
        """
        (public_key, private_key) = rsa.newkeys(1024)  # Генерация пары ключей длиной в 1024 б
        self.public_key = public_key  # Присваивние значения public_key аттрибуту public_key объекта класса Crypto
        self.private_key = private_key  # Присваивние значения private_key аттрибуту private_key объекта класса Crypto

        with open('public_key.pem', 'wb') as f:
            # Открытие файла public_key.pem в режиме побайтовой записи.
            # Если файл не существует - будет создан новый
            f.write(rsa.PublicKey.save_pkcs1(self.public_key, format='PEM'))
            # Запись значения аттрибута public_key объекта класса Crypto в открытый файл

        with open('private_key.pem', 'wb') as f:  # аналогично для приватного ключа
            f.write(rsa.PrivateKey.save_pkcs1(self.private_key, format='PEM'))

        return public_key, private_key  # Вернуть интерпретатору пару ключей
