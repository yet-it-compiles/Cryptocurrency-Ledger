import tkinter as tk
from tkinter import *


class Error:
    @staticmethod
    def open_popup(message):
        win = Tk()
        win("750x250")
        win.title("Error")
        Label(win, text="ERROR", font='Mistral 18 bold').place(x=150, y=80)
        Label(win, text=message, font='Mistral 18 bold').place(x=150, y=210)
        tk.Button(win, text="Close", command=win.destory).pack()
