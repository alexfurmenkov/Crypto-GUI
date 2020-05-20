from tkinter import Button, messagebox, filedialog

import rsa

from src.db import User, session
from src.crypto import Crypto


class Actions:
    def __init__(self, master, user: User):
        self.master = master
        self.user = user
        self.button_generate = Button(self.master, text='Сгенерировать ключи', command=self.generate_keys)
        self.button_encrypt = Button(self.master, text='Зашифровать файл', command=self.encrypt_file)
        self.button_decrypt = Button(self.master, text='Расшифровать файл', command=self.decrypt_file)

        self.master.geometry('800x600')
        self.button_generate.pack(pady=10)
        self.button_encrypt.pack(pady=10)
        self.button_decrypt.pack(pady=10)

    def generate_keys(self):
        crypto = Crypto()
        crypto.generate_keys()

        messagebox.showinfo(title='Успех', message='Пара ключей была сгенерирована.')

        data = dict(
            public_key='public_key.pem',
            private_key='private_key.pem',
        )
        session.query(User).filter_by(id=self.user.id).update(data)
        session.commit()

    def encrypt_file(self):
        filename = filedialog.askopenfilename()
        if filename is not None:
            with open(filename, 'rb+') as file:
                content = file.read()
                file.seek(0)
                content = rsa.encrypt(content, self.user.get_public_key())
                file.write(content)
                messagebox.showinfo(title='Успех', message='Содержимое файла зашифровано.')

    def decrypt_file(self):
        filename = filedialog.askopenfilename()
        if filename is not None:
            with open(filename, 'rb+') as file:
                content = file.read()
                content = rsa.decrypt(content, self.user.get_private_key())
                file.truncate(0)
                file.seek(0)
                file.write(content)
                messagebox.showinfo(title='Успех', message='Содержимое файла расшифровано.')
