from tkinter import (
    Toplevel,
    Label,
    Entry,
    Button,
    CENTER,
    messagebox,
)

from src.db import session, User
from .actions import Actions


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
        user = session.query(User).filter_by(login=user_login).first()
        if user is not None:
            Actions(Toplevel(self.master), user)
        else:
            messagebox.showerror(title='Ошибка', message='Пользователь не существует')
