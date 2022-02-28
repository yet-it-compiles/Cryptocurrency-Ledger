from tkinter import *
from tkinter import ttk


class Error:
    @staticmethod
    def open_popup(message):
        win = Tk()
        win.geometry("250x300")
        win.title("Error")
        Label(win, text="ERROR", font="Times 12 bold").place(x=12, y=80)
        Label(win, text=message, font='Times 12 bold').place(x=12, y=100)
        exit_button = ttk.Button(
            win,
            text='Exit',
            command=lambda: win.quit()
        )

        exit_button.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
        win.mainloop()
