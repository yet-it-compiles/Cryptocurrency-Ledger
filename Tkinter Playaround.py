""" This module will display the main dashboard """

from tkinter import *
from tkinter.ttk import *


class Dashboard:
    """ Creates a dashboard with usable buttons, and text """
    dashboard_display = Tk()  # Initializes the dashboard window

    def __init__(self):
        """ Default constructor to initialize window """
        self.dashboard_display.title("Cryptocurrency Ledger")
        Label(self.dashboard_display, text="Testing #1").pack()
        self.create_frame()
        self.create_button()
        self.create_label()

        self.dashboard_display.mainloop()  # executes the Dashboard

    def create_frame(self):
        """ Creates the dashboards frame """
        frame = Frame(self.dashboard_display)  # creates a frame inside the window
        frame.pack()  # geometry method
        button = Button(frame, text='Geek')
        button.pack()

    def create_button(self):
        """ TODO """
        self.dashboard_display.geometry('1900x700')  # window dimension (length by width)
        button = Button(self.dashboard_display, text="Click Me!", command=self.dashboard_display.destroy)

        button.pack(side='bottom')  # sets the button to the bottom

    def create_label(self):
        """ TODO """
        self.dashboard_display.geometry('405x300')

        user_name = Label(self.dashboard_display, text="UserName").place(x=40, y=60)
        user_password = Label(self.dashboard_display, text="Password").place(x=40, y=100)
        submit_button = Button(self.dashboard_display, text="Submit").place(x=40, y=130)
        Entry(self.dashboard_display, width=30).place(x=110, y=60)


if __name__ == "__main__":
    CryptoLedger = Dashboard()
