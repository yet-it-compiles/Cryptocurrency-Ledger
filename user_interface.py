""" This module configures each page of the Cryptocurrency ledger """
import tkinter as tk
from tkinter import *


class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Declares the size of the canvas, and positions it on the screen
        tk.Tk.geometry(self, '1000x600')
        tk.Tk.configure(self, bg="#343333")

        canvas_setup = Canvas(self, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0,
                              relief="ridge")
        canvas_setup.place(x=0, y=0)

        # Captures the background image for the canvas
        self.login_background = PhotoImage(file=f"login_background.png")
        canvas_setup.create_image(395.0, 300.0, image=self.login_background)

        # Initializing frames to an empty dictionary
        self.collection_of_canvases = {}

        # Declaration of logic to iterate through each page layout
        for each_layout in (LoginPage, Enrollment):
            each_canvas = each_layout(canvas_setup, self)

            self.collection_of_canvases[each_layout] = each_canvas

            each_canvas.grid(row=5, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, container):
        """
        Displays the current from that is passed as a parameter, and raises it to the current stack

        :param container: The passed in window to display next
        :return: the new canvas
        """
        new_frame = self.collection_of_canvases[container]
        new_frame.tkraise()


class LoginPage(tk.Frame):
    """ Configures, and displays the login page """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1000, height=600)

        login_canvas = Canvas(self, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0,
                              relief="ridge")
        login_canvas.place(x=0, y=0)
        self.controller = controller

        # Grabs the background image, and applies it
        self.login_background = PhotoImage(file=f"login_background.png")
        login_canvas.create_image(395.0, 300.0, image=self.login_background)

        # Logic to populate the window
        self.sign_in_button = PhotoImage(file=f"sign_in_button.png")
        sign_in_button_location = Button(self, image=self.sign_in_button, borderwidth=0, highlightthickness=0,
                                         relief="flat", activebackground="#343333")
        sign_in_button_location.place(x=659, y=417, width=159, height=53)

        # Creates, and displays the forgot password button
        self.forgot_password_button = PhotoImage(file=f"forgot_password_button.png")
        forgot_password_location = Button(self, image=self.forgot_password_button, borderwidth=0, highlightthickness=0,
                                          relief="flat", activebackground="#343333")
        forgot_password_location.place(x=444, y=537, width=142, height=50)

        # Creates, and displays the sign-up button
        self.sign_up_button = PhotoImage(file=f"sign_up_button.png")
        sign_up_button_location = Button(self, image=self.sign_up_button, borderwidth=0, highlightthickness=0,
                                         relief="flat", activebackground="#343333"
                                         , command=lambda: controller.show_frame(Enrollment))

        sign_up_button_location.place(x=864, y=537, width=136, height=46)

        # Creates, and initializes the text boxes
        self.login_textbox_one = PhotoImage(file=f"login_textbox.png")
        login_canvas.create_image(738.5, 263.0, image=self.login_textbox_one)
        textbox_one_location = Entry(self, bd=0, bg="#696969", highlightthickness=0)
        textbox_one_location.place(x=602.0, y=240, width=273.0, height=44)

        self.login_textbox_two = PhotoImage(file=f"login_textbox.png")
        login_canvas.create_image(738.5, 368.0, image=self.login_textbox_two)
        textbox_two_location = Entry(self, bd=0, bg="#696969", highlightthickness=0)
        textbox_two_location.place(x=602.0, y=345, width=273.0, height=44)


class Enrollment(tk.Frame):
    """ Configures, and displays the login page """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1000, height=600)
        self.controller = controller

        enrollment_canvas = Canvas(self, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0,
                                   relief="ridge")
        enrollment_canvas.place(x=0, y=0)

        self.enrollment_background = PhotoImage(file=f"enrollment_background.png")
        background = enrollment_canvas.create_image(348.0, 300.0, image=self.enrollment_background)

        # Declaration of string variable which captures user entries

        self.enrollment_text_box = PhotoImage(file=f"enrollment_textBox.png")
        enrollment_canvas.create_image(722.5, 176.0, image=self.enrollment_text_box)
        enrollment_text_box_location = Entry(self, bd=0, bg="#696969", highlightthickness=0)
        enrollment_text_box_location.place(x=586.0, y=153, width=273.0, height=44)

        self.enrollment_text_box_2 = PhotoImage(file=f"enrollment_textBox.png")
        enrollment_canvas.create_image(722.5, 293.0, image=self.enrollment_text_box_2)
        enrollment_text_box_location_2 = Entry(self, bd=0, bg="#696969", highlightthickness=0)
        enrollment_text_box_location_2.place(x=586.0, y=270, width=273.0, height=44)

        self.enrollment_text_box_3 = PhotoImage(file=f"enrollment_textBox.png")
        enrollment_canvas.create_image(722.5, 410.0, image=self.enrollment_text_box_3)
        enrollment_text_box_location_3 = Entry(self, bd=0, bg="#696969", highlightthickness=0)
        enrollment_text_box_location_3.place(x=586.0, y=387, width=273.0, height=44)

        self.get_started_button = PhotoImage(file=f"enrollment_get_started.png")
        get_started_background = Button(self, image=self.get_started_button, borderwidth=0, highlightthickness=0
                                        , relief="flat", activebackground="#343333")
        get_started_background.place(x=636, y=481, width=161, height=53)

        enrollment_canvas.create_text(727.5, 71.5, text="Create Account", fill="#ffffff",
                                      font=("Rosarivo-Regular", int(36.0)))

        self.existing_account = PhotoImage(file=f"enrollment_existing_account.png")
        existing_account_background = Button(self, image=self.existing_account, borderwidth=0, highlightthickness=0
                                             , command=lambda: controller.show_frame(LoginPage), relief="flat",
                                             activebackground="#343333")

        existing_account_background.place(x=618, y=530, width=212, height=51)


class Dashboard(tk.Frame):
    """ """
    pass


# Driver Code
app = TkinterApp()
app.mainloop()
