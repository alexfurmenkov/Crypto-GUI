from tkinter import (
    Tk,
    Toplevel,
    Label,
    Entry,
    Button,
    Text,
    CENTER,
    DISABLED,
    messagebox
)

from sqlalchemy.orm import sessionmaker

from src.db import User, engine
from src.crypto import Crypto

main_window = Tk()
main_window.geometry('800x600')
main_window.title('Juliya Crypto')


class Actions:
    def __init__(self, master, user: User):
        self.master = master
        self.user = user
        self.button_generate = Button(self.master, text='Сгенерировать ключи', command=self.generate_keys)
        self.button_encrypt = Button(self.master, text='Зашифровать файл')
        self.button_decrypt = Button(self.master, text='Расшифровать файл')

        self.master.geometry('800x600')
        self.button_generate.pack(pady=10)
        self.button_encrypt.pack(pady=10)
        self.button_decrypt.pack(pady=10)

    def generate_keys(self):
        crypto = Crypto()
        crypto.generate_keys()

        public_text = Text(self.master, height=1, relief='flat')
        private_text = Text(self.master, height=1, relief='flat')

        public_text.insert(1.0, crypto.public_key)
        private_text.insert(1.0, crypto.private_key)
        public_text.config(state=DISABLED)
        private_text.config(state=DISABLED)
        public_text.place(relx=0.5, rely=0.48, anchor=CENTER)
        private_text.place(relx=0.5, rely=0.58, anchor=CENTER)

        #  добавить сюда присваивание этих ключей объекту класса User


class Login:
    def __init__(self, master):
        self.master = master
        self.login_label = Label(master, text='Логин')
        self.login_input = Entry(master)
        self.button = Button(text='Войти', command=self.login_user)

        self.login_label.place(relx=0.3, rely=0.3, anchor=CENTER)
        self.login_input.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.38, anchor=CENTER)

    def login_user(self):
        user_login = self.login_input.get()
        session = sessionmaker(bind=engine)()
        user = session.query(User).filter_by(login=user_login).first()
        if user is not None:
            Actions(Toplevel(self.master), user)
        else:
            messagebox.showerror(title='Ошибка', message='Пользователь не существует')


login_block = Login(main_window)
main_window.mainloop()
