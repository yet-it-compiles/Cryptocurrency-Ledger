""" This module configures each page of the Cryptocurrency ledger """
import tkinter as tk
from tkinter import *


class TkinterApp(tk.Tk):
    """
    Configures the initial conditions for the UI, and contains the logic to switch between different canvases
    """
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

        # Initializing canvases to an empty dictionary
        self.collection_of_canvases = {}

        # Declaration of logic to iterate through each page layout
        for each_layout in (LoginPage, Enrollment, Dashboard, ComingSoon, Settings):
            each_canvas = each_layout(canvas_setup, self)

            self.collection_of_canvases[each_layout] = each_canvas

            each_canvas.grid(row=5, column=0, sticky="nsew")

        self.show_canvas(LoginPage)  # First frame to show

    def show_canvas(self, container):
        """
        Displays the current from that is passed as a parameter, and raises it to the current stack

        :param container: The passed in window to display next
        :return: the new canvas
        """
        for each_canvas in self.collection_of_canvases.values():
            each_canvas.grid_remove()
        each_canvas = self.collection_of_canvases[container]
        each_canvas.grid()


        self.geometry(f'{each_canvas.winfo_reqwidth()}x{each_canvas.winfo_reqheight()}')


class LoginPage(tk.Frame):
    """ Configures, and displays the login page """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1000, height=600)
        self.controller = controller

        login_canvas = Canvas(self, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0,
                              relief="ridge")
        login_canvas.place(x=0, y=0)

        # Grabs the background image, and applies it
        self.login_background = PhotoImage(file=f"login_background.png")
        login_canvas.create_image(395.0, 300.0, image=self.login_background)

        # Logic to populate the window
        self.sign_in_button = PhotoImage(file=f"sign_in_button.png")
        sign_in_button_location = Button(self, image=self.sign_in_button, borderwidth=0, highlightthickness=0,
                                         command=lambda: controller.show_canvas(Dashboard), relief="flat",
                                         activebackground="#343333")
        sign_in_button_location.place(x=659, y=417, width=159, height=53)

        # Creates, and displays the forgot password button
        self.forgot_password_button = PhotoImage(file=f"forgot_password_button.png")
        forgot_password_location = Button(self, image=self.forgot_password_button, borderwidth=0, highlightthickness=0,
                                          command=lambda: controller.show_canvas(ComingSoon),
                                          relief="flat", activebackground="#343333")
        forgot_password_location.place(x=444, y=537, width=142, height=50)

        # Creates, and displays the sign-up button
        self.sign_up_button = PhotoImage(file=f"sign_up_button.png")
        sign_up_button_location = Button(self, image=self.sign_up_button, borderwidth=0, highlightthickness=0,
                                         relief="flat", activebackground="#343333",
                                         command=lambda: controller.show_canvas(Enrollment))

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

        # Initializes the enrollment page, and configures the position of the canvas
        enrollment_canvas = Canvas(self, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0,
                                   relief="ridge")
        enrollment_canvas.place(x=0, y=0)

        # Captures the background image for the canvas
        self.enrollment_background = PhotoImage(file=f"enrollment_background.png")
        enrollment_canvas.create_image(348.0, 300.0, image=self.enrollment_background)

        # Declaration of string variable which captures user entries
        self.enrollment_text_box = PhotoImage(file=f"enrollment_textBox.png")
        enrollment_canvas.create_image(722.5, 176.0, image=self.enrollment_text_box)
        email_text_box = Entry(self, bd=0, bg="#696969", highlightthickness=0)
        email_text_box.place(x=586.0, y=153, width=273.0, height=44)

        self.enrollment_text_box_2 = PhotoImage(file=f"enrollment_textBox.png")
        enrollment_canvas.create_image(722.5, 293.0, image=self.enrollment_text_box_2)
        enrollment_text_box = Entry(self, bd=0, bg="#696969", highlightthickness=0)
        enrollment_text_box.place(x=586.0, y=270, width=273.0, height=44)

        self.enrollment_text_box_3 = PhotoImage(file=f"enrollment_textBox.png")
        enrollment_canvas.create_image(722.5, 410.0, image=self.enrollment_text_box_3)
        user_name_text_box = Entry(self, bd=0, bg="#696969", highlightthickness=0)
        user_name_text_box.place(x=586.0, y=387, width=273.0, height=44)

        self.get_started_button = PhotoImage(file=f"enrollment_get_started.png")
        get_started_background = Button(self, image=self.get_started_button, borderwidth=0, highlightthickness=0,
                                        command=lambda: controller.show_canvas(Dashboard), relief="flat",
                                        activebackground="#343333")
        get_started_background.place(x=636, y=481, width=161, height=53)

        enrollment_canvas.create_text(727.5, 71.5, text="Create Account", fill="#ffffff",
                                      font=("Rosarivo-Regular", int(36.0)))

        self.existing_account = PhotoImage(file=f"enrollment_existing_account.png")
        existing_account_background = Button(self, image=self.existing_account, borderwidth=0, highlightthickness=0,
                                             command=lambda: controller.show_canvas(LoginPage), relief="flat",
                                             activebackground="#343333")

        existing_account_background.place(x=618, y=530, width=212, height=51)


class Dashboard(tk.Frame):
    """ Configures, and displays the Dashboard """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1440, height=1024)
        flash_delay = 100  # Milliseconds.
        self.controller = controller

        canvas = tk.Canvas(self, bg="#343333", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # Captures the background image for the canvas
        image_path = "dashboard_background.png"
        self.background_img = tk.PhotoImage(file=image_path)
        canvas.create_image(0, 0, anchor='nw', image=self.background_img)

        # Creates text-fields for Searchbar, and Username
        canvas.create_text(588.0, 40.5, text="Search Bar\n", fill="#abb0c8", font=("Rosarivo-Regular", int(12.0)))
        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        # Investing PortFolio
        canvas.create_text(430.0, 198.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(430.0, 248.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(411.0, 298.5, text="%", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))

        # Investing Portfolio
        canvas.create_text(430.0, 198.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(430.0, 248.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(411.0, 298.5, text="%", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))

        # Top Earner #1
        canvas.create_text(640.0, 147.0, text="$", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(640.0, 190.0, text="$", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(690.0, 214.0, text="%", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))

        # Top Earner #2
        canvas.create_text(865.0, 147.0, text="$", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(865.0, 190.0, text="$", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(920.0, 214.0, text="%", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))

        # Top Earner #3
        canvas.create_text(1096.0, 149.0, text="$", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1096.0, 192.0, text="$", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1149.0, 214.0, text="%", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))

        # Top Earner #4
        canvas.create_text(1322.0, 149.0, text="$", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1322.0, 192.0, text="$", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1373.0, 214.0, text="%", fill="#e5e5e5", font=("Rosarivo-Regular", int(10.0)))

        # Closest to profit #1
        canvas.create_text(640.0, 295.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(640.0, 338.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(690.0, 356.0, text="%", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))

        # Closest to profit #2
        canvas.create_text(865.0, 295.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(865.0, 338.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(920.0, 356.0, text="%", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))

        # Closest to profit #3
        canvas.create_text(1096.0, 295.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1096.0, 338.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1149.0, 356.0, text="%", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))

        # Closest to profit #4
        canvas.create_text(1322.0, 295.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1322.0, 338.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1373.0, 356.0, text="%", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))

        # Percent Increase Calculator
        canvas.create_text(968.0, 469.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(968.0, 504.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(968.0, 553.0, text="%", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(972.0, 604.0, text="$", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(975.0, 620.0, text="$0.00 is a 0% increase from $0.00", fill="#ffffff",
                           font=("Rosarivo-Regular", int(10.0)))

        # Retrieves the images, and configures the dashboard button
        dashboard_image_path = "dashboard_dashboard.png"
        self.dashboard_image = tk.PhotoImage(file=dashboard_image_path)
        dashboard_image_obj = canvas.create_image(0, 120, anchor='nw', image=self.dashboard_image)
        canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(dashboard_image_obj), controller.show_canvas(Dashboard)))

        # Retrieves the images, and configures the simulated trading button
        simulated_trading_image_path = "dashboard_simulated_trading.png"
        self.simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
        simulated_trading_image_obj = canvas.create_image(0, 230, anchor='nw', image=self.simulated_trading_image)
        canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(simulated_trading_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the charts button
        charts_image_path = "dashboard_charts.png"
        self.charts_image = tk.PhotoImage(file=charts_image_path)
        charts_image_obj = canvas.create_image(0, 340, anchor='nw', image=self.charts_image)
        canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(charts_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the portfolio button
        portfolio_image_path = "dashboard_portfolio.png"
        self.portfolio_image = tk.PhotoImage(file=portfolio_image_path)
        portfolio_image_obj = canvas.create_image(0, 450, anchor='nw', image=self.portfolio_image)
        canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(portfolio_image_obj), controller.show_canvas(ComingSoon)))

        alarm_image_path = "dashboard_alarms.png"
        self.alarm_image = tk.PhotoImage(file=alarm_image_path)
        alarm_image_obj = canvas.create_image(0, 560, anchor='nw', image=self.alarm_image)
        canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(alarm_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the news button
        news_image_path = "dashboard_news.png"
        self.news_image = tk.PhotoImage(file=news_image_path)
        news_image_obj = canvas.create_image(0, 670, anchor='nw', image=self.news_image)
        canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(news_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the settings button
        settings_image_path = "dashboard_settings.png"
        self.settings_image = tk.PhotoImage(file=settings_image_path)
        settings_image_obj = canvas.create_image(0, 780, anchor='nw', image=self.settings_image)
        canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(settings_image_obj), controller.show_canvas(Settings)))

        # Retrieves the images, and configures the logout button
        logout_image_path = "dashboard_logout.png"
        self.logout_image = tk.PhotoImage(file=logout_image_path)
        logout_image_obj = canvas.create_image(45, 950, anchor='nw', image=self.logout_image)
        canvas.tag_bind(logout_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(logout_image_obj), controller.show_canvas(LoginPage)))

        # Retrieves the images, and configures the notifications image
        notifications_image_path = "dashboard_notifications.png"
        self.notifications_image = tk.PhotoImage(file=notifications_image_path)
        notifications_image_obj = canvas.create_image(1027, 19, anchor='nw', image=self.notifications_image)
        canvas.tag_bind(notifications_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notifications_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the support image
        support_image_path = "dashboard_support.png"
        self.support_image = tk.PhotoImage(file=support_image_path)
        support_image_obj = canvas.create_image(1155, 16, anchor='nw', image=self.support_image)
        canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(support_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        notes_image_path = "dashboard_notes.png"
        self.notes_image = tk.PhotoImage(file=notes_image_path)
        notes_image_obj = canvas.create_image(1268, 19, anchor='nw', image=self.notes_image)
        canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notes_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        profile_image_path = "dashboard_profile_img.png"
        self.profile_image = tk.PhotoImage(file=profile_image_path)
        profile_image_obj = canvas.create_image(1360, 4, anchor='nw', image=self.profile_image)
        canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(profile_image_obj), controller.show_canvas(Settings)))

        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        def flash_hidden(image_obj):
            """
            Method sets the state of the object, and hides the buttons when they are interacted with

            :param image_obj: is the image object to hide
            :type : int
            :return: a hidden button when pressed
            """
            set_state(tk.HIDDEN, image_obj)
            canvas.after(flash_delay, set_state, tk.NORMAL, image_obj)

        def set_state(state, image_obj):
            """
            Sets the state of the image object

            :param state: the state to apply to the buttons
            :param image_obj: is the image object to apply a state on
            :return: an image object with a state applied
            """
            canvas.itemconfigure(image_obj, state=state)

        self.background_img.width(), self.background_img.height()


class ComingSoon(tk.Frame):
    """ Configures, and displays the Dashboard """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1440, height=1024)
        flash_delay = 100  # Milliseconds.
        self.controller = controller

        canvas = tk.Canvas(self, bg="#343333", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"coming_soon.png")
        canvas.create_image(718.0, 512.0, image=self.background_img)

        # Retrieves the images, and configures the dashboard button
        dashboard_image_path = "dashboard_dashboard.png"
        self.dashboard_image = tk.PhotoImage(file=dashboard_image_path)
        dashboard_image_obj = canvas.create_image(0, 120, anchor='nw', image=self.dashboard_image)
        canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(dashboard_image_obj), controller.show_canvas(Dashboard)))

        # Retrieves the images, and configures the simulated trading button
        simulated_trading_image_path = "dashboard_simulated_trading.png"
        self.simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
        simulated_trading_image_obj = canvas.create_image(0, 230, anchor='nw', image=self.simulated_trading_image)
        canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(simulated_trading_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the charts button
        charts_image_path = "dashboard_charts.png"
        self.charts_image = tk.PhotoImage(file=charts_image_path)
        charts_image_obj = canvas.create_image(0, 340, anchor='nw', image=self.charts_image)
        canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(charts_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the portfolio button
        portfolio_image_path = "dashboard_portfolio.png"
        self.portfolio_image = tk.PhotoImage(file=portfolio_image_path)
        portfolio_image_obj = canvas.create_image(0, 450, anchor='nw', image=self.portfolio_image)
        canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(portfolio_image_obj), controller.show_canvas(ComingSoon)))

        alarm_image_path = "dashboard_alarms.png"
        self.alarm_image = tk.PhotoImage(file=alarm_image_path)
        alarm_image_obj = canvas.create_image(0, 560, anchor='nw', image=self.alarm_image)
        canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(alarm_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the news button
        news_image_path = "dashboard_news.png"
        self.news_image = tk.PhotoImage(file=news_image_path)
        news_image_obj = canvas.create_image(0, 670, anchor='nw', image=self.news_image)
        canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(news_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the settings button
        settings_image_path = "dashboard_settings.png"
        self.settings_image = tk.PhotoImage(file=settings_image_path)
        settings_image_obj = canvas.create_image(0, 780, anchor='nw', image=self.settings_image)
        canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(settings_image_obj), controller.show_canvas(Settings)))

        # Retrieves the images, and configures the logout button
        logout_image_path = "dashboard_logout.png"
        self.logout_image = tk.PhotoImage(file=logout_image_path)
        logout_image_obj = canvas.create_image(45, 950, anchor='nw', image=self.logout_image)
        canvas.tag_bind(logout_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(logout_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the notifications image
        notifications_image_path = "dashboard_notifications.png"
        self.notifications_image = tk.PhotoImage(file=notifications_image_path)
        notifications_image_obj = canvas.create_image(1027, 19, anchor='nw', image=self.notifications_image)
        canvas.tag_bind(notifications_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notifications_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the support image
        support_image_path = "dashboard_support.png"
        self.support_image = tk.PhotoImage(file=support_image_path)
        support_image_obj = canvas.create_image(1155, 16, anchor='nw', image=self.support_image)
        canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(support_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        notes_image_path = "dashboard_notes.png"
        self.notes_image = tk.PhotoImage(file=notes_image_path)
        notes_image_obj = canvas.create_image(1268, 19, anchor='nw', image=self.notes_image)
        canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notes_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        profile_image_path = "dashboard_profile_img.png"
        self.profile_image = tk.PhotoImage(file=profile_image_path)
        profile_image_obj = canvas.create_image(1360, 4, anchor='nw', image=self.profile_image)
        canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(profile_image_obj), controller.show_canvas(ComingSoon)))

        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        def flash_hidden(image_obj):
            """
            Method sets the state of the object, and hides the buttons when they are interacted with

            :param image_obj: is the image object to hide
            :type : int
            :return: an image object that is hidden
            """
            set_state(tk.HIDDEN, image_obj)
            canvas.after(flash_delay, set_state, tk.NORMAL, image_obj)

        def set_state(state, image_obj):
            """
            Sets the state of the image object

            :param state: the state to apply to the buttons
            :param image_obj: is the image object to apply a state on
            :return: an image object with a state applied
            """
            canvas.itemconfigure(image_obj, state=state)

        self.background_img.width(), self.background_img.height()


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1440, height=1024)
        self.controller = controller

        flash_delay = 100  # in milliseconds.

        canvas = tk.Canvas(self, bg="#343333", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # Retrieves the images, and configures the dashboard button
        self.background_img = tk.PhotoImage(file=f"settings_background.png")
        canvas.create_image(722.0, 512.0, image=self.background_img)

        # Retrieves the images, and configures the dashboard button
        dashboard_image_path = "dashboard_dashboard.png"
        self.dashboard_image = tk.PhotoImage(file=dashboard_image_path)
        dashboard_image_obj = canvas.create_image(0, 120, anchor='nw', image=self.dashboard_image)
        canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(dashboard_image_obj), controller.show_canvas(Dashboard)))

        # Retrieves the images, and configures the simulated trading button
        simulated_trading_image_path = "dashboard_simulated_trading.png"
        self.simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
        simulated_trading_image_obj = canvas.create_image(0, 230, anchor='nw', image=self.simulated_trading_image)
        canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(simulated_trading_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the charts button
        charts_image_path = "dashboard_charts.png"
        self.charts_image = tk.PhotoImage(file=charts_image_path)
        charts_image_obj = canvas.create_image(0, 340, anchor='nw', image=self.charts_image)
        canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(charts_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the portfolio button
        portfolio_image_path = "dashboard_portfolio.png"
        self.portfolio_image = tk.PhotoImage(file=portfolio_image_path)
        portfolio_image_obj = canvas.create_image(0, 450, anchor='nw', image=self.portfolio_image)
        canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(portfolio_image_obj), controller.show_canvas(ComingSoon)))

        alarm_image_path = "dashboard_alarms.png"
        self.alarm_image = tk.PhotoImage(file=alarm_image_path)
        alarm_image_obj = canvas.create_image(0, 560, anchor='nw', image=self.alarm_image)
        canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(alarm_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the news button
        news_image_path = "dashboard_news.png"
        self.news_image = tk.PhotoImage(file=news_image_path)
        news_image_obj = canvas.create_image(0, 670, anchor='nw', image=self.news_image)
        canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(news_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the settings button
        settings_image_path = "dashboard_settings.png"
        self.settings_image = tk.PhotoImage(file=settings_image_path)
        settings_image_obj = canvas.create_image(0, 780, anchor='nw', image=self.settings_image)
        canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(settings_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the notifications image
        notifications_image_path = "dashboard_notifications.png"
        self.notifications_image = tk.PhotoImage(file=notifications_image_path)
        notifications_image_obj = canvas.create_image(1027, 19, anchor='nw', image=self.notifications_image)
        canvas.tag_bind(notifications_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notifications_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the support image
        support_image_path = "dashboard_support.png"
        self.support_image = tk.PhotoImage(file=support_image_path)
        support_image_obj = canvas.create_image(1155, 16, anchor='nw', image=self.support_image)
        canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(support_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        notes_image_path = "dashboard_notes.png"
        self.notes_image = tk.PhotoImage(file=notes_image_path)
        notes_image_obj = canvas.create_image(1268, 19, anchor='nw', image=self.notes_image)
        canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notes_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        profile_image_path = "dashboard_profile_img.png"
        self.profile_image = tk.PhotoImage(file=profile_image_path)
        profile_image_obj = canvas.create_image(1360, 4, anchor='nw', image=self.profile_image)
        canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(profile_image_obj), controller.show_canvas(ComingSoon)))

        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        def flash_hidden(image_obj):
            """
            Method sets the state of the object, and hides the buttons when they are interacted with

            :param image_obj: is the image object to hide
            :type : int
            :return: a hidden button when pressed
            """
            set_state(tk.HIDDEN, image_obj)
            canvas.after(flash_delay, set_state, tk.NORMAL, image_obj)

        def set_state(state, image_obj):
            """
            Sets the state of the image object

            :param state: the state to apply to the buttons
            :param image_obj: is the image object to apply a state on
            :return: an image object with a state applied
            """
            canvas.itemconfigure(image_obj, state=state)

        self.settings_image.width(), self.settings_image.height()

        self.entry0_img = PhotoImage(file=f"settings_entry.png")
        canvas.create_image(731.5, 766.5, image=self.entry0_img)
        settings_email = Entry(self, bd=0, bg="#696969", highlightthickness=0)
        settings_email.place(x=597.5, y=741, width=268.0, height=49)

        self.entry1_img = PhotoImage(file=f"settings_entry.png")
        canvas.create_image(731.5, 647.5, image=self.entry1_img)

        entry1 = Entry(self, bd=0, bg="#696969", highlightthickness=0)

        entry1.place(x=597.5, y=622, width=268.0, height=49)

        self.entry2_img = PhotoImage(file=f"settings_entry.png")
        canvas.create_image(731.5, 528.5, image=self.entry2_img)

        entry2 = Entry(self, bd=0, bg="#696969", highlightthickness=0)

        entry2.place(x=597.5, y=503, width=268.0, height=49)

        canvas.create_text(583, 372.0, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(26.0)))


# class LogoutButtonBottom(tk.Frame):
#     """
#
#     """
#
#     def init(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.config(width=1000, height=600)
#         self.controller = controller
#
#         canvas = Canvas(self, bg="#343333", height=273, width=537, bd=0, highlightthickness=0, relief="ridge")
#         canvas.place(x=0, y=0)
#
#         self.background_img = PhotoImage(file=f"logout_background.png")
#         canvas.create_image(268.5, 136.5, image=self.background_img)
#
#         self.img0 = PhotoImage(file=f"settings_yes.png")
#         b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, relief="flat")
#
#         b0.place(x=112, y=135, width=123, height=49)
#
#         self.img1 = PhotoImage(file=f"settings_no.png")
#         b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, relief="flat")
#
#         b1.place(x=297, y=135, width=123, height=49)


# Driver Code
app = TkinterApp()
app.mainloop()
