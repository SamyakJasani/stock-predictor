from tkinter import *
import pandas as pd
import tkinter.messagebox
from .main import launch_main_app
import os

def check_credentials(username, password):
    filepath = os.path.join(os.path.dirname(__file__), '../data/users.csv')
    df = pd.read_csv(filepath)
    for i in range(len(df)):
        if username == df['LoginID'][i] and password == str(df['Password'][i]):
            return True
    return False

def start_login():
    def on_login():
        user = username.get()
        passwd = password.get()
        if check_credentials(user, passwd):
            tkWindow.destroy()
            launch_main_app()
        else:
            response = tkinter.messagebox.askretrycancel(title='Error', message='Invalid Login or Password')
            if not response:
                tkWindow.destroy()

    tkWindow = Tk()
    tkWindow.geometry('400x150')
    tkWindow.title('Login Page')

    Label(tkWindow, text="Username").grid(row=0, column=0)
    username = StringVar()
    Entry(tkWindow, textvariable=username).grid(row=0, column=1)

    Label(tkWindow, text="Password").grid(row=1, column=0)
    password = StringVar()
    Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

    Button(tkWindow, text="Login", command=on_login).grid(row=2, column=0, columnspan=2)

    tkWindow.mainloop()
