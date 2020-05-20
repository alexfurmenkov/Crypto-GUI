from tkinter import Tk

from src.screens import Login

main_window = Tk()
main_window.geometry('800x600')
main_window.title('Juliya Crypto')

login_block = Login(main_window)
main_window.mainloop()
