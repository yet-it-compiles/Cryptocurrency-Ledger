""" This module configures each page of the Cryptocurrency ledger """

import tkinter as tk
from tkinter import *
import database
from database import *
import password_encryption
from password_encryption import *
from mpl_charts import MplCharts
import responsive_calculator
import manual_transaction


def logout_button_display(self, controller):
    pop = Toplevel(self)
    pop.geometry('537x273')
    pop.config(height=273, width=537)

    logout_canvas = Canvas(pop, bg="#ffffff", height=273, width=537, bd=0, highlightthickness=0, relief="ridge")
    logout_canvas.place(x=0, y=0)

    self.logout_background_img = PhotoImage(file="Collection of all UI Graphics\logout_background.png")
    logout_canvas.create_image(0, 0, anchor='nw', image=self.logout_background_img)

    def destroy_logout():
        pop.destroy()

    # creates and adds functionality for the Yes button in the log out pop up
    self.logout_yes_img = PhotoImage(file="Collection of all UI Graphics\logout_yes.png")
    logout_yes_img_obj = logout_canvas.create_image(112, 135, anchor='nw', image=self.logout_yes_img)
    logout_canvas.tag_bind(logout_yes_img_obj, "<ButtonRelease-1>",
                           lambda event: [destroy_logout(), (controller.show_canvas(LoginPage))])

    # creates and adds functionality for the No button in the log-out pop up
    self.logout_no_img = PhotoImage(file="Collection of all UI Graphics\logout_no.png")
    logout_no_img_obj = logout_canvas.create_image(297, 135, anchor='nw', image=self.logout_no_img)
    logout_canvas.tag_bind(logout_no_img_obj, "<ButtonRelease-1>", lambda event: destroy_logout())


def Error(self, message):
    pop = Toplevel(self)
    pop.geometry('537x250')
    pop.config(height=273, width=537)

    error_canvas = Canvas(pop, bg="#ffffff", height=273, width=537, bd=0, highlightthickness=0, relief="ridge")
    error_canvas.place(x=0, y=0)

    self.error_background_img = PhotoImage(file="Collection of all UI Graphics\error_background.png")
    error_canvas.create_image(0, 0, anchor='nw', image=self.error_background_img)

    def destroy_error():
        pop.destroy()

    error_canvas.create_text(200, 125, text=message, fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
    self.error_button_img = PhotoImage(file="Collection of all UI Graphics/error_button_img.png")
    error_button_obj = error_canvas.create_image(280, 200, image=self.error_button_img)
    error_canvas.tag_bind(error_button_obj, "<ButtonRelease-1>", lambda event: destroy_error())


# general method for the notifications button
def notifications_clicker(self):
    """
    Configures, and displays the alert popup
    """
    pop = Toplevel(self)
    pop.geometry('684x426')
    pop.config(width=684, height=426)

    def destroy_alerts():
        pop.destroy()

    notifications_canvas = Canvas(pop, bg="#ffffff", height=426, width=684, bd=0, highlightthickness=0, relief="ridge")
    notifications_canvas.place(x=0, y=0)

    # alerts background initialization
    self.alert_background_img = PhotoImage(file="Collection of all UI Graphics/alert_popup_background.png")
    notifications_canvas.create_image(342.0, 213.0, image=self.alert_background_img)

    # alert name entry
    self.coin_name_img = PhotoImage(file="Collection of all UI Graphics/alert_popup_textBox2.png")
    notifications_canvas.create_image(341.5, 278.5, image=self.coin_name_img)
    alert_name_entry = Entry(pop, bd=0, bg="#dcdcdc", highlightthickness=0)
    alert_name_entry.place(x=260.5, y=267, width=163.0, height=20)

    # price entry
    self.price_entry_img = PhotoImage(file="Collection of all UI Graphics/alert_popup_textBox1.png")
    notifications_canvas.create_image(391.5, 167.5, image=self.price_entry_img)
    price_entry = Entry(pop, bd=0, bg="#dcdcdc", highlightthickness=0)
    price_entry.place(x=358.5, y=156, width=66.0, height=21)

    # frequency options menu
    frequencies = ["One Time", "Persistent"]
    click_frequency = StringVar()
    click_frequency.set(frequencies[0])

    self.frequency_img = PhotoImage(file="Collection of all UI Graphics/alert_popup_img0.png")
    frequency_button = OptionMenu(notifications_canvas, click_frequency, *frequencies)
    frequency_button.place(x=289, y=209, width=98, height=22)

    # conditions options menu
    conditions = [">", "<", "="]
    clicked_counter = StringVar(pop)
    clicked_counter.set("")

    self.condition_img = PhotoImage(file="Collection of all UI Graphics/alert_popup_img1.png")
    b1 = OptionMenu(notifications_canvas, clicked_counter, *conditions)
    b1.place(x=249, y=156, width=85, height=22)

    # autofill search function for coins
    coin_listbox = Listbox(notifications_canvas)
    coin_list = manual_transaction.get_list_of_coins()

    # updates the listbox
    def update(data):
        """
        TODO - DOCUMENT
        """
        # changes the size of the listbox to number of items in list
        listbox_height = len(data)

        if len(data) > 5:
            listbox_height = 5
        coin_listbox.place(height=(16.5 * listbox_height))

        # clears the listbox
        coin_listbox.delete(0, END)
        for item in data:
            coin_listbox.insert(END, item)

    # allows users to choose items from list
    def fill_out(event):
        coin_name_entry.delete(0, END)
        coin_name_entry.insert(0, coin_listbox.get(ACTIVE))
        price_entry.place(x=358.5, y=156, width=66.0, height=21)
        coin_listbox.place_forget()

    # displays in list appropriate items comparatively to entry
    def check():

        # Retrieves user input
        typed = coin_name_entry.get()
        if typed == "":
            data = coin_list
        else:
            data = []
            for each_item in coin_list:  # TODO - Explain what this does
                if typed.lower() in each_item.lower():
                    data.append(each_item)
        update(data)

    def show_list():
        coin_listbox.place(x=260, y=120, width=140.0, height=82.5)
        price_entry.place_forget()
        check()

        coin_listbox.bind("<<ListboxSelect>>", fill_out)

    # coin name entry and autofill
    self.entry2_img = PhotoImage(file=f"Collection of all UI Graphics/alert_popup_textBox0.png")
    notifications_canvas.create_image(341.5, 108.0, image=self.entry2_img)
    coin_name_entry = Entry(pop, bd=0, bg="#dcdcdc", highlightthickness=0)
    coin_name_entry.place(x=260.0, y=97, width=162.0, height=21)
    # once a key is pressed in the entry the dropdown will show with options
    coin_name_entry.bind("<KeyRelease>", lambda event: show_list())

    # cancel button
    self.cancel_img = PhotoImage(file=f"Collection of all UI Graphics/alert_popup_img0.png")
    cancel_button = notifications_canvas.create_image(324, 341, anchor='nw', image=self.cancel_img)
    notifications_canvas.tag_bind(cancel_button, "<ButtonRelease-1>", lambda event: destroy_alerts())

    # add alert button
    self.add_alerts_img = PhotoImage(file=f"Collection of all UI Graphics/alert_popup_img1.png")
    add_alert_button = notifications_canvas.create_image(293, 307, anchor='nw', image=self.add_alerts_img)
    notifications_canvas.tag_bind(add_alert_button, "<ButtonRelease-1>", lambda event: destroy_alerts())


Collection_of_canvases = {}


class CryptocurrencyLedger(tk.Tk):
    """
    Configures the initial conditions for the UI, and contains the logic to switch between different canvases
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Declares the size of the canvas, and positions it on the screen
        tk.Tk.geometry(self, "")
        tk.Tk.configure(self, bg="#343333")

        canvas_setup = Canvas(self, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0,
                              relief="ridge")
        canvas_setup.place(x=0, y=0)

        # Captures the background image for the canvas
        self.login_background = PhotoImage(file=f"Collection of all UI Graphics/login_background.png")
        canvas_setup.create_image(395.0, 300.0, image=self.login_background)

        # Declaration of logic to iterate through each page layout
        for each_layout in (LoginPage, Enrollment, Dashboard, Charts, ComingSoon, Settings
                            , NotesTab, Portfolio):
            each_canvas = each_layout(canvas_setup, self)

            Collection_of_canvases[each_layout] = each_canvas

            each_canvas.grid(row=5, column=0, sticky="nsew")

        self.show_canvas(LoginPage)  # First frame to show

    def show_canvas(self, container):
        """
        Displays the current from that is passed as a parameter, and raises it to the current stack
        :param container: The passed in window to display next
        :return: the new canvas
        """
        for each_canvas in Collection_of_canvases.values():
            each_canvas.grid_remove()

        each_canvas = Collection_of_canvases[container]
        each_canvas.grid()

        self.geometry(f'{each_canvas.winfo_reqwidth()}x{each_canvas.winfo_reqheight()}')  # resizes the canvases


class LoginPage(tk.Frame):
    """
    Configures, and displays the login page
    """

    def sign_in(self, controller,  usernameEntry, passwordEntry):
        username = usernameEntry.get()
        password = passwordEntry.get()
        if username == "" or password == "":
            Error(self, "Please fill out both fields")
            usernameEntry.set("")
            passwordEntry.set("")
            return

        if Database.checkUsername(username):
            if PasswordEncryption.password_comparison(username, password):
                # reset username and password for when they return to the login screen
                usernameEntry.set("")
                passwordEntry.set("")

                # Set up Dashboard UI to have all customer information
                Dashboard.create_user(Collection_of_canvases[Dashboard], username)
                Dashboard.update(Collection_of_canvases[Dashboard])
                controller.show_canvas(Dashboard)
            else:
                error = "Incorrect Password"
                Error(self, error)
                passwordEntry.set("")
        else:
            error = "No Username"
            Error(self, error)
            usernameEntry.set("")
            passwordEntry.set("")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1000, height=600)
        self.controller = controller
        username = tk.StringVar()
        password = tk.StringVar()

        login_canvas = Canvas(self, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0,
                              relief="ridge")
        login_canvas.place(x=0, y=0)

        # Grabs the background image, and applies it
        self.login_background = PhotoImage(file=f"Collection of all UI Graphics/login_background.png")
        login_canvas.create_image(395.0, 300.0, image=self.login_background)

        # Logic to populate the window
        self.sign_in_button = PhotoImage(file=f"Collection of all UI Graphics/sign_in_button.png")
        sign_in_button_location = Button(self, image=self.sign_in_button, borderwidth=0, highlightthickness=0,
                                         command=lambda: self.sign_in(self.controller,username, password),
                                         relief="flat",
                                         activebackground="#343333")
        sign_in_button_location.place(x=659, y=417, width=159, height=53)

        # Creates, and displays the forgot password button
        self.forgot_password_button = PhotoImage(file=f"Collection of all UI Graphics/forgot_password_button.png")
        forgot_password_location = Button(self, image=self.forgot_password_button, borderwidth=0, highlightthickness=0,
                                          command=lambda: controller.show_canvas(Dashboard),
                                          relief="flat", activebackground="#343333")
        forgot_password_location.place(x=444, y=537, width=142, height=50)

        # Creates, and displays the sign-up button
        self.sign_up_button = PhotoImage(file=f"Collection of all UI Graphics/sign_up_button.png")
        sign_up_button_location = Button(self, image=self.sign_up_button, borderwidth=0, highlightthickness=0,
                                         relief="flat", activebackground="#343333",
                                         command=lambda: controller.show_canvas(Enrollment))

        sign_up_button_location.place(x=864, y=537, width=136, height=46)

        # Creates, and initializes the text boxes
        self.login_textbox_one = PhotoImage(file=f"Collection of all UI Graphics/login_textbox.png")
        login_canvas.create_image(738.5, 263.0, image=self.login_textbox_one)
        textbox_one_location = Entry(self, textvariable=username, bd=0, bg="#696969", highlightthickness=0)
        textbox_one_location.place(x=602.0, y=240, width=273.0, height=44)

        self.login_textbox_two = PhotoImage(file=f"Collection of all UI Graphics/login_textbox.png")
        login_canvas.create_image(738.5, 368.0, image=self.login_textbox_two)
        textbox_two_location = Entry(self, textvariable=password, bd=0, bg="#696969", highlightthickness=0, show='*')
        textbox_two_location.place(x=602.0, y=345, width=273.0, height=44)


class Enrollment(tk.Frame):
    """
    Configures, and displays the login page
    """

    def add_user(self, controller, username, password, email):
        get_username = username.get()
        get_password = password.get()
        get_email = email.get()

        if (get_username == "" or get_password == "" or get_email == ""):
            error = "Please fill out every field"
            Error(self, error)
            return

        if Database.checkUsername(get_username):
            error = "Username is taken. Please choose a different username"
            Error(self, error)
            return

        # possible check for password constraints
        Database.adduser(get_username, get_email, get_password)
        controller.show_canvas(LoginPage)
        username.set("")
        password.set("")
        email.set("")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1000, height=600)
        self.controller = controller
        user_email = tk.StringVar()
        user_username = tk.StringVar()
        user_password = tk.StringVar()

        # Initializes the enrollment page, and configures the position of the canvas
        enrollment_canvas = Canvas(self, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0,
                                   relief="ridge")
        enrollment_canvas.place(x=0, y=0)

        # Captures the background image for the canvas
        self.enrollment_background = PhotoImage(file=f"Collection of all UI Graphics/enrollment_background.png")
        enrollment_canvas.create_image(348.0, 300.0, image=self.enrollment_background)

        # Declaration of string variable which captures user entries
        self.enrollment_text_box = PhotoImage(file=f"Collection of all UI Graphics/enrollment_textBox.png")
        enrollment_canvas.create_image(722.5, 176.0, image=self.enrollment_text_box)
        email_text_box = Entry(self, textvariable=user_email, bd=0, bg="#696969", highlightthickness=0)
        email_text_box.place(x=586.0, y=153, width=273.0, height=44)

        self.enrollment_text_box_2 = PhotoImage(file=f"Collection of all UI Graphics/enrollment_textBox.png")
        enrollment_canvas.create_image(722.5, 293.0, image=self.enrollment_text_box_2)
        enrollment_text_box = Entry(self, textvariable=user_password, bd=0, bg="#696969", highlightthickness=0)
        enrollment_text_box.place(x=586.0, y=270, width=273.0, height=44)

        self.enrollment_text_box_3 = PhotoImage(file=f"Collection of all UI Graphics/enrollment_textBox.png")
        enrollment_canvas.create_image(722.5, 410.0, image=self.enrollment_text_box_3)
        user_name_text_box = Entry(self, textvariable=user_username, bd=0, bg="#696969", highlightthickness=0)
        user_name_text_box.place(x=586.0, y=387, width=273.0, height=44)

        self.get_started_button = PhotoImage(file=f"Collection of all UI Graphics/enrollment_get_started.png")
        get_started_background = Button(self, image=self.get_started_button, borderwidth=0, highlightthickness=0,
                                        command=lambda: self.add_user(controller, user_username, user_password,
                                                                      user_email),
                                        relief="flat",
                                        activebackground="#343333")
        get_started_background.place(x=636, y=481, width=161, height=53)

        enrollment_canvas.create_text(727.5, 71.5, text="Create Account", fill="#ffffff",
                                      font=("Rosarivo-Regular", int(36.0)))

        self.existing_account = PhotoImage(file=f"Collection of all UI Graphics/enrollment_existing_account.png")
        existing_account_background = Button(self, image=self.existing_account, borderwidth=0, highlightthickness=0,
                                             command=lambda: self.controller.show_canvas(LoginPage), relief="flat",
                                             activebackground="#343333")

        existing_account_background.place(x=618, y=530, width=212, height=51)


class Dashboard(tk.Frame):
    """
    Configures, and displays the Dashboard
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1440, height=1024)
        flash_delay = 100  # Milliseconds.
        self.controller = controller

        self.canvas = tk.Canvas(self, bg="#343333", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Creates a blank Database object that will be filled in after sign in
        self.user_data = Database("")

        # Captures the background image for the canvas
        image_path = "Collection of all UI Graphics/dashboard_background.png"
        self.background_img = tk.PhotoImage(file=image_path)
        self.canvas.create_image(0, 0, anchor='nw', image=self.background_img)

        # creates and opens up a log-out pop up
        logout_image_path = "Collection of all UI Graphics/dashboard_logout.png"
        self.logout_image = tk.PhotoImage(file=logout_image_path)
        logout_button = self.canvas.create_image(45, 950, anchor='nw', image=self.logout_image)
        self.canvas.tag_bind(logout_button, "<ButtonRelease-1>",
                             lambda event: logout_button_display(self, self.controller))

        # Creates text-fields for searchbar, and username
        # canvas.create_text(588.0, 40.5, text="Search Bar\n", fill="#abb0c8", font=("Rosarivo-Regular", int(12.0)))
        self.canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        # Investing Portfolio
        self.total_portfolio = self.canvas.create_text(430.0, 198.0, text="$", fill="#ffffff",
                                                       font=("Rosarivo-Regular", int(10.0)))
        self.buy_power = self.canvas.create_text(430.0, 248.0, text="$", fill="#ffffff",
                                                 font=("Rosarivo-Regular", int(10.0)))
        self.total_change = self.canvas.create_text(430.0, 298.5, text="%", fill="#ffffff",
                                                    font=("Rosarivo-Regular", int(10.0)))

        # Top Earner #1
        self.top_earner_1_1 = self.canvas.create_text(640.0, 147.0, text="$", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))
        self.top_earner_1_2 = self.canvas.create_text(640.0, 190.0, text="$", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))
        self.top_earner_1_3 = self.canvas.create_text(690.0, 214.0, text="%", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))

        # Top Earner #2
        self.top_earner_2_1 = self.canvas.create_text(865.0, 147.0, text="$", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))
        self.top_earner_2_2 = self.canvas.create_text(865.0, 190.0, text="$", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))
        self.top_earner_2_3 = self.canvas.create_text(920.0, 214.0, text="%", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))

        # Top Earner #3
        self.top_earner_3_1 = self.canvas.create_text(1096.0, 149.0, text="$", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))
        self.top_earner_3_2 = self.canvas.create_text(1096.0, 192.0, text="$", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))
        self.top_earner_3_3 = self.canvas.create_text(1149.0, 214.0, text="%", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))

        # Top Earner #4
        self.top_earner_4_1 = self.canvas.create_text(1322.0, 149.0, text="$", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))
        self.top_earner_4_2 = self.canvas.create_text(1322.0, 192.0, text="$", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))
        self.top_earner_4_3 = self.canvas.create_text(1373.0, 214.0, text="%", fill="#e5e5e5",
                                                      font=("SourceCodePro-Regular", int(10.0)))

        # Closest to profit #1
        self.closest_1_1 = self.canvas.create_text(640.0, 295.0, text="$", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))
        self.closest_1_2 = self.canvas.create_text(640.0, 338.0, text="$", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))
        self.closest_1_3 = self.canvas.create_text(690.0, 356.0, text="%", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))

        # Closest to profit #2
        self.closest_2_1 = self.canvas.create_text(865.0, 295.0, text="$", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))
        self.closest_2_1 = self.canvas.create_text(865.0, 338.0, text="$", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))
        self.closest_2_3 = self.canvas.create_text(920.0, 356.0, text="%", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))

        # Closest to profit #3
        self.closest_3_1 = self.canvas.create_text(1096.0, 295.0, text="$", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))
        self.closest_3_2 = self.canvas.create_text(1096.0, 338.0, text="$", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))
        self.closest_3_3 = self.canvas.create_text(1149.0, 356.0, text="%", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))

        # Closest to profit #4
        self.closest_4_1 = self.canvas.create_text(1322.0, 295.0, text="$", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))
        self.closest_4_2 = self.canvas.create_text(1322.0, 338.0, text="$", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))
        self.closest_4_3 = self.canvas.create_text(1373.0, 356.0, text="%", fill="#ffffff",
                                                   font=("SourceCodePro-Regular", int(10.0)))

        # Percent Increase Calculator
        calc = responsive_calculator.ResponsiveCalculator()
        initial_price, final_price, percent_difference, raw_difference = calc.return_labels()

        initial_entry = tk.Entry(self, textvariable=initial_price,  font=("Rosarivo-Regular", int(10)), width = 15, bd = 0, bg = '#d3d3d3')
        final_entry = tk.Entry(self,textvariable=final_price, font=("Rosarivo-Regular", int(10)), width = 15, bd = 0, bg = '#d3d3d3')
        percent_entry = tk.Entry(self, textvariable=percent_difference, font=("Rosarivo-Regular", int(10)), width = 15, bd = 0, bg = '#d3d3d3')
        raw_entry = tk.Entry(self, textvariable=raw_difference, font=("Rosarivo-Regular", int(10)), width = 15, bd = 0, bg = '#d3d3d3')

        clear_button = Button(self, text= "clear", borderwidth=0, highlightthickness=0, command=lambda:
        [initial_entry.delete(0, END), final_entry.delete(0, END), percent_entry.delete(0, END), raw_entry.delete(0, END)])
        clear_button.place(x=1075, y= 600, height=20, width=55)

        calculate_button = Button(self, text="Calculate", borderwidth=0, highlightthickness=0, command= lambda:
        [initial_price.set(calc.initial_price_answer.get()), final_price.set(calc.final_price_answer.get()),
         percent_difference.set(calc.percent_difference_answer.get()), raw_difference.set(calc.raw_difference_answer.get())])
        calculate_button.place(x=1075, y=575, height=20, width=55)

        self.canvas.create_window(985, 460, window = initial_entry)
        self.canvas.create_window(985, 502, window = final_entry)
        self.canvas.create_window(985, 547, window = percent_entry)
        self.canvas.create_window(985, 595, window = raw_entry)

        initial_price.trace('w', calc.calculate_initial_price)
        final_price.trace('w', calc.calculate_final_price)
        percent_difference.trace('w', calc.calculate_percent_difference)
        raw_difference.trace('w', calc.calculate_raw_difference)

        # Retrieves the images, and configures the dashboard button
        dashboard_image_path = "Collection of all UI Graphics/dashboard_dashboard.png"
        self.dashboard_image = tk.PhotoImage(file=dashboard_image_path)
        dashboard_image_obj = self.canvas.create_image(0, 120, anchor='nw', image=self.dashboard_image)
        self.canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                             lambda event: (flash_hidden(dashboard_image_obj), controller.show_canvas(Dashboard)))

        # Retrieves the images, and configures the simulated trading button
        simulated_trading_image_path = "Collection of all UI Graphics/dashboard_simulated_trading.png"
        self.simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
        simulated_trading_image_obj = self.canvas.create_image(0, 230, anchor='nw', image=self.simulated_trading_image)
        self.canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                             lambda event: (
                                 flash_hidden(simulated_trading_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the charts button
        charts_image_path = "Collection of all UI Graphics/dashboard_charts.png"
        self.charts_image = tk.PhotoImage(file=charts_image_path)
        charts_image_obj = self.canvas.create_image(0, 340, anchor='nw', image=self.charts_image)
        self.canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                             lambda event: (flash_hidden(charts_image_obj), controller.show_canvas(Charts)))

        # Retrieves the images, and configures the portfolio button
        portfolio_image_path = "Collection of all UI Graphics/dashboard_portfolio.png"
        self.portfolio_image = tk.PhotoImage(file=portfolio_image_path)
        portfolio_image_obj = self.canvas.create_image(0, 450, anchor='nw', image=self.portfolio_image)
        self.canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                             lambda event: (flash_hidden(portfolio_image_obj), controller.show_canvas(Portfolio)))

        alarm_image_path = "Collection of all UI Graphics/dashboard_alarms.png"
        self.alarm_image = tk.PhotoImage(file=alarm_image_path)
        alarm_image_obj = self.canvas.create_image(0, 560, anchor='nw', image=self.alarm_image)
        self.canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                             lambda event: (flash_hidden(alarm_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the news button
        news_image_path = "Collection of all UI Graphics/dashboard_news.png"
        self.news_image = tk.PhotoImage(file=news_image_path)
        news_image_obj = self.canvas.create_image(0, 670, anchor='nw', image=self.news_image)
        self.canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                             lambda event: (flash_hidden(news_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the settings button
        settings_image_path = "Collection of all UI Graphics/dashboard_settings.png"
        self.settings_image = tk.PhotoImage(file=settings_image_path)
        settings_image_obj = self.canvas.create_image(0, 780, anchor='nw', image=self.settings_image)
        self.canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                             lambda event: (flash_hidden(settings_image_obj), controller.show_canvas(Settings)))

        # Retrieves the images, and opens the notifications image
        notifications_image_path = "Collection of all UI Graphics/dashboard_notifications.png"
        self.notifications_image = tk.PhotoImage(file=notifications_image_path)
        notifications_button = self.canvas.create_image(1027, 19, anchor='nw', image=self.notifications_image)
        self.canvas.tag_bind(notifications_button, "<ButtonRelease-1>", lambda event: notifications_clicker(self))

        # Retrieves the images, and configures the support image
        support_image_path = "Collection of all UI Graphics/dashboard_support.png"
        self.support_image = tk.PhotoImage(file=support_image_path)
        support_image_obj = self.canvas.create_image(1155, 16, anchor='nw', image=self.support_image)
        self.canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                             lambda event: (flash_hidden(support_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        notes_image_path = "Collection of all UI Graphics/dashboard_notes.png"
        self.notes_image = tk.PhotoImage(file=notes_image_path)
        notes_image_obj = self.canvas.create_image(1268, 19, anchor='nw', image=self.notes_image)
        self.canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                             lambda event: (flash_hidden(notes_image_obj), controller.show_canvas(NotesTab)))

        # Retrieves the images, and configures the profile image
        profile_image_path = "Collection of all UI Graphics/dashboard_profile_img.png"
        self.profile_image = tk.PhotoImage(file=profile_image_path)
        profile_image_obj = self.canvas.create_image(1360, 4, anchor='nw', image=self.profile_image)
        self.canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                             lambda event: (flash_hidden(profile_image_obj), controller.show_canvas(Settings)))

        self.canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        # Search bar
        self.search_bar_image = PhotoImage(file=f"Collection of all UI Graphics/search_bar.png")
        self.canvas.create_image(657.0, 34.5, image=self.search_bar_image)
        search_bar_textbox = Entry(self, bd=0, bg="#3a495f", highlightthickness=0)
        search_bar_textbox.place(x=536.0, y=19, width=242.0, height=29)

        def flash_hidden(image_obj):
            """
            Method sets the state of the object, and hides the buttons when they are interacted with
            :param image_obj: is the image object to hide
            :type : int
            :return: a hidden button when pressed
            """
            set_state(tk.HIDDEN, image_obj)
            self.canvas.after(flash_delay, set_state, tk.NORMAL, image_obj)

        def set_state(state, image_obj):
            """
            Sets the state of the image object
            :param state: the state to apply to the buttons
            :param image_obj: is the image object to apply a state on
            :return: an image object with a state applied
            """
            self.canvas.itemconfigure(image_obj, state=state)

        self.background_img.width(), self.background_img.height()

    def create_user(self, username):
        self.user_data = Database(username)
        print("successfully created")

    def update(self):
        # Total Value Updater
        self.canvas.itemconfig(self.total_portfolio, text=('$', self.user_data.get_total_portfolio()))

        # Top Earners Updater

        counter = 1
        dict_of_top_earners = {}
        dict_of_top_earners = self.user_data.get_top_earners()
        if len(dict_of_top_earners) == 0:
            return

        for counter in range(len(dict_of_top_earners)):
            print("made it", counter)
            if counter == 0:
                print("counter = 1")
                self.canvas.itemconfig(self.top_earner_1_1, text=('$', dict_of_top_earners[0][1][0]))
                self.canvas.itemconfig(self.top_earner_1_2, text=("$", dict_of_top_earners[0][1][1]))
                self.canvas.itemconfig(self.top_earner_1_3, text=( dict_of_top_earners[0][1][2], '%'))
            elif counter == 1:
                self.canvas.itemconfig(self.top_earner_2_1, text=('$', dict_of_top_earners[1][1][0]))
                self.canvas.itemconfig(self.top_earner_2_2, text=('$', dict_of_top_earners[1][1][1]))
                self.canvas.itemconfig(self.top_earner_2_3, text=( dict_of_top_earners[1][1][2], '%'))
            elif counter == 2:
                self.canvas.itemconfig(self.top_earner_3_1, text=('$', dict_of_top_earners[2][1][0]))
                self.canvas.itemconfig(self.top_earner_3_2, text=('$', dict_of_top_earners[2][1][1]))
                self.canvas.itemconfig(self.top_earner_3_3, text=( dict_of_top_earners[2][1][2], '%'))
            elif counter == 3:
                self.canvas.itemconfig(self.top_earner_4_1, text=('$', dict_of_top_earners[3][1][0]))
                self.canvas.itemconfig(self.top_earner_4_2, text=('$', dict_of_top_earners[3][1][1]))
                self.canvas.itemconfig(self.top_earner_4_3, text=( dict_of_top_earners[3][1][2], '%'))
            else:
                break

        # Closest to Profit Goals


class Charts(tk.Frame):
    """ Configures, and displays the Charts Tab """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.coin = None
        self.data = None
        self.current_price = None

        self.config(width=1440, height=1024)
        self.controller = controller

        flash_delay = 100  # in milliseconds.
        self.canvas = Canvas(self, bg="#1b3152", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        self.charts = MplCharts(self.canvas)

        self.background_img = PhotoImage(file=f"Collection of all UI Graphics/charts_background.png")
        self.canvas.create_image(720.0, 512.0, image=self.background_img)

        # creates and opens up a log-out pop up
        logout_image_path = "Collection of all UI Graphics/dashboard_logout.png"
        self.logout_image = tk.PhotoImage(file=logout_image_path)
        logout_button = self.canvas.create_image(45, 950, anchor='nw', image=self.logout_image)
        self.canvas.tag_bind(logout_button, "<ButtonRelease-1>",
                             lambda event: logout_button_display(self, self.controller))

        # start date label
        self.entry1_img = PhotoImage(file=f"Collection of all UI Graphics/charts_textBox1.png")
        self.canvas.create_image(1085.0, 377.0, image=self.entry1_img)
        entry1 = Entry(self, bd=0, bg="#2a2b31", highlightthickness=0)
        entry1.place(x=996.0, y=357, width=178.0, height=38)

        # end date label
        self.entry0_img = PhotoImage(file=f"Collection of all UI Graphics/charts_textBox0.png")
        self.canvas.create_image(1337.0, 377.0, image=self.entry0_img)
        entry0 = Entry(self, bd=0, bg="#2a2b31", highlightthickness=0)
        entry0.place(x=1248.0, y=357, width=178.0, height=38)

        # text fields for data
        self.mc = self.canvas.create_text(483.0, 167.0, text="0.00", fill="#ffffff",
                                          font=("SourceCodePro-Regular", int(15.0)))
        self.cs = self.canvas.create_text(483.0, 265.0, text="0.00", fill="#ffffff",
                                          font=("SourceCodePro-Regular", int(15.0)))
        self.h24 = self.canvas.create_text(854.0, 167.0, text="0.00", fill="#ffffff",
                                           font=("SourceCodePro-Regular", int(15.0)))
        self.l24 = self.canvas.create_text(854.0, 265.0, text="0.00", fill="#ffffff",
                                           font=("SourceCodePro-Regular", int(15.0)))
        self.vol = self.canvas.create_text(1333.0, 167.0, text="0.00", fill="#ffffff",
                                           font=("SourceCodePro-Regular", int(15.0)))
        self.fdv = self.canvas.create_text(1333.0, 265.0, text="0.00", fill="#ffffff",
                                           font=("SourceCodePro-Regular", int(15.0)))

        # Retrieves the images, and configures the dashboard button
        dashboard_image_path = "Collection of all UI Graphics/dashboard_dashboard.png"
        self.dashboard_image = tk.PhotoImage(file=dashboard_image_path)
        dashboard_image_obj = self.canvas.create_image(0, 120, anchor='nw', image=self.dashboard_image)
        self.canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                             lambda event: (
                                 flash_hidden(dashboard_image_obj), self.close_charts(),
                                 controller.show_canvas(Dashboard)))

        # Retrieves the images, and configures the simulated trading button
        simulated_trading_image_path = "Collection of all UI Graphics/dashboard_simulated_trading.png"
        self.simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
        simulated_trading_image_obj = self.canvas.create_image(0, 230, anchor='nw', image=self.simulated_trading_image)
        self.canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                             lambda event: (flash_hidden(simulated_trading_image_obj), self.close_charts(),
                                            controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the charts button
        charts_image_path = "Collection of all UI Graphics/dashboard_charts.png"
        self.charts_image = tk.PhotoImage(file=charts_image_path)
        charts_image_obj = self.canvas.create_image(0, 340, anchor='nw', image=self.charts_image)
        self.canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                             lambda event: (
                                 flash_hidden(charts_image_obj), self.close_charts(), controller.show_canvas(Charts)))

        # Retrieves the images, and configures the portfolio button
        portfolio_image_path = "Collection of all UI Graphics/dashboard_portfolio.png"
        self.portfolio_image = tk.PhotoImage(file=portfolio_image_path)
        portfolio_image_obj = self.canvas.create_image(0, 450, anchor='nw', image=self.portfolio_image)
        self.canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                             lambda event: (
                                 flash_hidden(portfolio_image_obj), self.close_charts(),
                                 controller.show_canvas(Portfolio)))

        alarm_image_path = "Collection of all UI Graphics/dashboard_alarms.png"
        self.alarm_image = tk.PhotoImage(file=alarm_image_path)
        alarm_image_obj = self.canvas.create_image(0, 560, anchor='nw', image=self.alarm_image)
        self.canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                             lambda event: (
                                 flash_hidden(alarm_image_obj), self.close_charts(),
                                 controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the news button
        news_image_path = "Collection of all UI Graphics/dashboard_news.png"
        self.news_image = tk.PhotoImage(file=news_image_path)
        news_image_obj = self.canvas.create_image(0, 670, anchor='nw', image=self.news_image)
        self.canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                             lambda event: (
                                 flash_hidden(news_image_obj), self.close_charts(), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the settings button
        settings_image_path = "Collection of all UI Graphics/dashboard_settings.png"
        self.settings_image = tk.PhotoImage(file=settings_image_path)
        settings_image_obj = self.canvas.create_image(0, 780, anchor='nw', image=self.settings_image)
        self.canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                             lambda event: (
                                 flash_hidden(settings_image_obj), self.close_charts(),
                                 controller.show_canvas(Settings)))

        # Retrieves the images, and opens the notifications image
        notifications_image_path = "Collection of all UI Graphics/dashboard_notifications.png"
        self.notifications_image = tk.PhotoImage(file=notifications_image_path)
        notifications_button = self.canvas.create_image(1027, 19, anchor='nw', image=self.notifications_image)
        self.canvas.tag_bind(notifications_button, "<ButtonRelease-1>", lambda event: notifications_clicker())

        # Retrieves the images, and configures the support image
        support_image_path = "Collection of all UI Graphics/dashboard_support.png"
        self.support_image = tk.PhotoImage(file=support_image_path)
        support_image_obj = self.canvas.create_image(1155, 16, anchor='nw', image=self.support_image)
        self.canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                             lambda event: (
                                 flash_hidden(support_image_obj), self.close_charts(),
                                 controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        notes_image_path = "Collection of all UI Graphics/dashboard_notes.png"
        self.notes_image = tk.PhotoImage(file=notes_image_path)
        notes_image_obj = self.canvas.create_image(1268, 19, anchor='nw', image=self.notes_image)
        self.canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                             lambda event: (
                                 flash_hidden(notes_image_obj), self.close_charts(), controller.show_canvas(NotesTab)))

        # Retrieves the images, and configures the profile image
        profile_image_path = "Collection of all UI Graphics/dashboard_profile_img.png"
        self.profile_image = tk.PhotoImage(file=profile_image_path)
        profile_image_obj = self.canvas.create_image(1360, 4, anchor='nw', image=self.profile_image)
        self.canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                             lambda event: (
                                 flash_hidden(profile_image_obj), self.close_charts(),
                                 controller.show_canvas(Settings)))

        self.canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        self.img0 = PhotoImage(file=f"Collection of all UI Graphics/charts_img0.png")
        b0 = Button(self, image=self.img0, borderwidth=0, highlightthickness=0, relief="flat")
        b0.place(x=855, y=370, width=26, height=16)

        self.img1 = PhotoImage(file=f"Collection of all UI Graphics/charts_img1.png")
        b1 = Button(self, image=self.img1, borderwidth=0, highlightthickness=0, relief="flat")
        b1.place(x=799, y=370, width=25, height=16)

        self.img2 = PhotoImage(file=f"Collection of all UI Graphics/charts_img2.png")
        b2 = Button(self, image=self.img2, borderwidth=0, highlightthickness=0, relief="flat")
        b2.place(x=743, y=371, width=26, height=16)

        self.img3 = PhotoImage(file=f"Collection of all UI Graphics/charts_img3.png")
        b3 = Button(self, image=self.img3, borderwidth=0, highlightthickness=0, relief="flat")
        b3.place(x=677, y=370, width=28, height=17)

        self.img4 = PhotoImage(file=f"Collection of all UI Graphics/charts_img4.png")
        b4 = Button(self, image=self.img4, borderwidth=0, highlightthickness=0, relief="flat")
        b4.place(x=618, y=369, width=26, height=16)

        # Search bar
        self.search_bar_image = PhotoImage(file=f"Collection of all UI Graphics/search_bar.png")
        self.canvas.create_image(657.0, 34.5, image=self.search_bar_image)
        search_bar_textbox = Entry(self, bd=0, bg="#3a495f", highlightthickness=0)
        search_bar_textbox.place(x=536.0, y=19, width=242.0, height=29)

        def flash_hidden(image_obj):
            """
            Method sets the state of the object, and hides the buttons when they are interacted with
            :param image_obj: is the image object to hide
            :type : int
            :return: a hidden button when pressed
            """
            set_state(tk.HIDDEN, image_obj)
            self.canvas.after(flash_delay, set_state, tk.NORMAL, image_obj)

        def set_state(state, image_obj):
            """
            Sets the state of the image object
            :param state: the state to apply to the buttons
            :param image_obj: is the image object to apply a state on
            :return: an image object with a state applied
            """
            self.canvas.itemconfigure(image_obj, state=state)

    def search(self):
        self.coin = self.coin_name.get()
        self.generate_data()
        self.generate_chart(365)
        self.search_entry.delete(0, tk.END)

    def format_currency(self, num):
        if num != "N/A":
            if num > 1:
                return "${:,.2f}".format(num)
            else:
                return "${:.3g}".format(num)
        else:
            return num

    def update_coin(self, coin):
        self.coin = coin

    def generate_data(self):
        self.data = self.charts.charts_data(self.coin)
        for key, value in self.data.items():
            if value is None:
                self.data[key] = "N/A"

        self.current_price = self.data["current_price"]

        self.canvas.itemconfig(self.mc, text=self.format_currency(self.data["market_cap"]))
        self.canvas.itemconfig(self.fdv, text=self.format_currency(self.data["fully_diluted_valuation"]))
        self.canvas.itemconfig(self.h24, text=self.format_currency(self.data["high_24h"]))
        self.canvas.itemconfig(self.l24, text=self.format_currency(self.data["low_24h"]))
        self.canvas.itemconfig(self.vol, text=self.format_currency(self.data["total_volume"]))
        self.canvas.itemconfig(self.cs, text=self.data["circulating_supply"])

    def generate_chart(self, days_previous):
        ohlc = self.charts.candlestick(self.coin, days_previous)
        # # there is no field for price/percent change
        # start_price = ohlc["open"][0]
        # perc_change = 100 * (self.current_price - start_price) / start_price
        # color = "green" if perc_change > 0 else "red"
        # perc_text = "(" + "{:.2f}".format(perc_change) + "%)"
        # self.canvas.itemconfig(self.percent, text=perc_text, fill=color)

    def close_charts(self):
        self.charts.close()
        self.canvas.itemconfig(self.mc, text="")
        self.canvas.itemconfig(self.fdv, text="")
        self.canvas.itemconfig(self.h24, text="")
        self.canvas.itemconfig(self.l24, text="")
        self.canvas.itemconfig(self.vol, text="")
        self.canvas.itemconfig(self.cs, text="")


class ComingSoon(tk.Frame):
    """
    Configures, and displays the Dashboard
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1440, height=1024)
        flash_delay = 100  # Milliseconds.
        self.controller = controller

        canvas = tk.Canvas(self, bg="#343333", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"Collection of all UI Graphics/coming_soon.png")
        canvas.create_image(718.0, 512.0, image=self.background_img)

        # creates and opens up a log-out pop up
        logout_image_path = "Collection of all UI Graphics/dashboard_logout.png"
        self.logout_image = tk.PhotoImage(file=logout_image_path)
        logout_button = canvas.create_image(45, 950, anchor='nw', image=self.logout_image)
        canvas.tag_bind(logout_button, "<ButtonRelease-1>", lambda event: logout_button_display(self, self.controller))

        # Retrieves the images, and configures the dashboard button
        dashboard_image_path = "Collection of all UI Graphics/dashboard_dashboard.png"
        self.dashboard_image = tk.PhotoImage(file=dashboard_image_path)
        dashboard_image_obj = canvas.create_image(0, 120, anchor='nw', image=self.dashboard_image)
        canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(dashboard_image_obj), controller.show_canvas(Dashboard)))

        # Retrieves the images, and configures the simulated trading button
        simulated_trading_image_path = "Collection of all UI Graphics/dashboard_simulated_trading.png"
        self.simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
        simulated_trading_image_obj = canvas.create_image(0, 230, anchor='nw', image=self.simulated_trading_image)
        canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(simulated_trading_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the charts button
        charts_image_path = "Collection of all UI Graphics/dashboard_charts.png"
        self.charts_image = tk.PhotoImage(file=charts_image_path)
        charts_image_obj = canvas.create_image(0, 340, anchor='nw', image=self.charts_image)
        canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(charts_image_obj), controller.show_canvas(Charts)))

        # Retrieves the images, and configures the portfolio button
        portfolio_image_path = "Collection of all UI Graphics/dashboard_portfolio.png"
        self.portfolio_image = tk.PhotoImage(file=portfolio_image_path)
        portfolio_image_obj = canvas.create_image(0, 450, anchor='nw', image=self.portfolio_image)
        canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(portfolio_image_obj), controller.show_canvas(Portfolio)))

        alarm_image_path = "Collection of all UI Graphics/dashboard_alarms.png"
        self.alarm_image = tk.PhotoImage(file=alarm_image_path)
        alarm_image_obj = canvas.create_image(0, 560, anchor='nw', image=self.alarm_image)
        canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(alarm_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the news button
        news_image_path = "Collection of all UI Graphics/dashboard_news.png"
        self.news_image = tk.PhotoImage(file=news_image_path)
        news_image_obj = canvas.create_image(0, 670, anchor='nw', image=self.news_image)
        canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(news_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the settings button
        settings_image_path = "Collection of all UI Graphics/dashboard_settings.png"
        self.settings_image = tk.PhotoImage(file=settings_image_path)
        settings_image_obj = canvas.create_image(0, 780, anchor='nw', image=self.settings_image)
        canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(settings_image_obj), controller.show_canvas(Settings)))

        # Retrieves the images, and opens the notifications image
        notifications_image_path = "Collection of all UI Graphics/dashboard_notifications.png"
        self.notifications_image = tk.PhotoImage(file=notifications_image_path)
        notifications_button = canvas.create_image(1027, 19, anchor='nw', image=self.notifications_image)
        canvas.tag_bind(notifications_button, "<ButtonRelease-1>", lambda event: notifications_clicker(self))

        # Retrieves the images, and configures the support image
        support_image_path = "Collection of all UI Graphics/dashboard_support.png"
        self.support_image = tk.PhotoImage(file=support_image_path)
        support_image_obj = canvas.create_image(1155, 16, anchor='nw', image=self.support_image)
        canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(support_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        notes_image_path = "Collection of all UI Graphics/dashboard_notes.png"
        self.notes_image = tk.PhotoImage(file=notes_image_path)
        notes_image_obj = canvas.create_image(1268, 19, anchor='nw', image=self.notes_image)
        canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notes_image_obj), controller.show_canvas(NotesTab)))

        # Retrieves the images, and configures the profile image
        profile_image_path = "Collection of all UI Graphics/dashboard_profile_img.png"
        self.profile_image = tk.PhotoImage(file=profile_image_path)
        profile_image_obj = canvas.create_image(1360, 4, anchor='nw', image=self.profile_image)
        canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(profile_image_obj), controller.show_canvas(Settings)))

        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        # search button command
        def search(coin_name=None, search_entry=None):
            controller.show_canvas(Charts)
            Charts.update_coin(Collection_of_canvases[Charts], coin_name.get())
            Charts.generate_data(Collection_of_canvases[Charts])
            Charts.generate_chart(Collection_of_canvases[Charts], 365)
            search_entry.delete(0, tk.END)
            

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
    """
    Configures, and displays the Settings page
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1440, height=1024)
        self.controller = controller

        flash_delay = 100  # in milliseconds.

        canvas = tk.Canvas(self, bg="#343333", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # Retrieves the images, and configures the dashboard button
        self.background_img = tk.PhotoImage(file=f"Collection of all UI Graphics/settings_background.png")
        canvas.create_image(722.0, 512.0, image=self.background_img)

        # creates and opens up a log-out pop up
        logout_image_path = "Collection of all UI Graphics/dashboard_logout.png"
        self.logout_image = tk.PhotoImage(file=logout_image_path)
        logoutButton = canvas.create_image(45, 950, anchor='nw', image=self.logout_image)
        canvas.tag_bind(logoutButton, "<ButtonRelease-1>", lambda event: logout_button_display(self, self.controller))

        # Retrieves the images, and configures the dashboard button
        dashboard_image_path = "Collection of all UI Graphics/dashboard_dashboard.png"
        self.dashboard_image = tk.PhotoImage(file=dashboard_image_path)
        dashboard_image_obj = canvas.create_image(0, 120, anchor='nw', image=self.dashboard_image)
        canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(dashboard_image_obj), controller.show_canvas(Dashboard)))

        # Retrieves the images, and configures the simulated trading button
        simulated_trading_image_path = "Collection of all UI Graphics/dashboard_simulated_trading.png"
        self.simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
        simulated_trading_image_obj = canvas.create_image(0, 230, anchor='nw', image=self.simulated_trading_image)
        canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(simulated_trading_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the charts button
        charts_image_path = "Collection of all UI Graphics/dashboard_charts.png"
        self.charts_image = tk.PhotoImage(file=charts_image_path)
        charts_image_obj = canvas.create_image(0, 340, anchor='nw', image=self.charts_image)
        canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(charts_image_obj), controller.show_canvas(Charts)))

        # Retrieves the images, and configures the portfolio button
        portfolio_image_path = "Collection of all UI Graphics/dashboard_portfolio.png"
        self.portfolio_image = tk.PhotoImage(file=portfolio_image_path)
        portfolio_image_obj = canvas.create_image(0, 450, anchor='nw', image=self.portfolio_image)
        canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(portfolio_image_obj), controller.show_canvas(Portfolio)))

        alarm_image_path = "Collection of all UI Graphics/dashboard_alarms.png"
        self.alarm_image = tk.PhotoImage(file=alarm_image_path)
        alarm_image_obj = canvas.create_image(0, 560, anchor='nw', image=self.alarm_image)
        canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(alarm_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the news button
        news_image_path = "Collection of all UI Graphics/dashboard_news.png"
        self.news_image = tk.PhotoImage(file=news_image_path)
        news_image_obj = canvas.create_image(0, 670, anchor='nw', image=self.news_image)
        canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(news_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the settings button
        settings_image_path = "Collection of all UI Graphics/dashboard_settings.png"
        self.settings_image = tk.PhotoImage(file=settings_image_path)
        settings_image_obj = canvas.create_image(0, 780, anchor='nw', image=self.settings_image)
        canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(settings_image_obj), controller.show_canvas(Settings)))

        # Retrieves the images, and opens the notifications image
        notifications_image_path = "Collection of all UI Graphics/dashboard_notifications.png"
        self.notifications_image = tk.PhotoImage(file=notifications_image_path)
        notifications_button = canvas.create_image(1027, 19, anchor='nw', image=self.notifications_image)
        canvas.tag_bind(notifications_button, "<ButtonRelease-1>", lambda event: notifications_clicker(self))

        # Retrieves the images, and configures the support image
        support_image_path = "Collection of all UI Graphics/dashboard_support.png"
        self.support_image = tk.PhotoImage(file=support_image_path)
        support_image_obj = canvas.create_image(1155, 16, anchor='nw', image=self.support_image)
        canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(support_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        notes_image_path = "Collection of all UI Graphics/dashboard_notes.png"
        self.notes_image = tk.PhotoImage(file=notes_image_path)
        notes_image_obj = canvas.create_image(1268, 19, anchor='nw', image=self.notes_image)
        canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notes_image_obj), controller.show_canvas(NotesTab)))

        # Retrieves the images, and configures the profile image
        profile_image_path = "Collection of all UI Graphics/dashboard_profile_img.png"
        self.profile_image = tk.PhotoImage(file=profile_image_path)
        profile_image_obj = canvas.create_image(1360, 4, anchor='nw', image=self.profile_image)
        canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(profile_image_obj), controller.show_canvas(Settings)))

        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        def search(coin_name=None, search_entry=None):
            controller.show_canvas(Charts)
            Charts.update_coin(Collection_of_canvases[Charts], coin_name.get())
            Charts.generate_data(Collection_of_canvases[Charts])
            Charts.generate_chart(Collection_of_canvases[Charts], 365)
            search_entry.delete(0, tk.END)

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

        self.entry0_img = PhotoImage(file=f"Collection of all UI Graphics/settings_entry.png")
        canvas.create_image(731.5, 766.5, image=self.entry0_img)
        settings_email = Entry(self, bd=0, bg="#696969", highlightthickness=0)
        settings_email.place(x=597.5, y=741, width=268.0, height=49)

        self.entry1_img = PhotoImage(file=f"Collection of all UI Graphics/settings_entry.png")
        canvas.create_image(731.5, 647.5, image=self.entry1_img)

        entry1 = Entry(self, bd=0, bg="#696969", highlightthickness=0)

        entry1.place(x=597.5, y=622, width=268.0, height=49)

        self.entry2_img = PhotoImage(file=f"Collection of all UI Graphics/settings_entry.png")
        canvas.create_image(731.5, 528.5, image=self.entry2_img)

        entry2 = Entry(self, bd=0, bg="#696969", highlightthickness=0)

        entry2.place(x=597.5, y=503, width=268.0, height=49)

        canvas.create_text(731.5, 422.0, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(26.0)))


class NotesTab(tk.Frame):
    """
    Configures, and displays the Notes tab
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1440, height=1024)
        self.controller = controller

        flash_delay = 100  # in milliseconds.
        canvas = Canvas(self, bg="#ffffff", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_background.png")
        canvas.create_image(720.0, 512.0, image=self.background_img)

        # creates and opens up a log-out pop up
        logout_image_path = "Collection of all UI Graphics/dashboard_logout.png"
        self.logout_image = tk.PhotoImage(file=logout_image_path)
        log_out_button = canvas.create_image(45, 950, anchor='nw', image=self.logout_image)
        canvas.tag_bind(log_out_button, "<ButtonRelease-1>", lambda event: logout_button_display(self, self.controller))

        # Retrieves the images, and configures the dashboard button
        dashboard_image_path = "Collection of all UI Graphics/dashboard_dashboard.png"
        self.dashboard_image = tk.PhotoImage(file=dashboard_image_path)
        dashboard_image_obj = canvas.create_image(0, 120, anchor='nw', image=self.dashboard_image)
        canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(dashboard_image_obj), controller.show_canvas(Dashboard)))

        # Retrieves the images, and configures the simulated trading button
        simulated_trading_image_path = "Collection of all UI Graphics/dashboard_simulated_trading.png"
        self.simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
        simulated_trading_image_obj = canvas.create_image(0, 230, anchor='nw', image=self.simulated_trading_image)
        canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(simulated_trading_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the charts button
        charts_image_path = "Collection of all UI Graphics/dashboard_charts.png"
        self.charts_image = tk.PhotoImage(file=charts_image_path)
        charts_image_obj = canvas.create_image(0, 340, anchor='nw', image=self.charts_image)
        canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(charts_image_obj), controller.show_canvas(Charts)))

        # Retrieves the images, and configures the portfolio button
        portfolio_image_path = "Collection of all UI Graphics/dashboard_portfolio.png"
        self.portfolio_image = tk.PhotoImage(file=portfolio_image_path)
        portfolio_image_obj = canvas.create_image(0, 450, anchor='nw', image=self.portfolio_image)
        canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(portfolio_image_obj), controller.show_canvas(Portfolio)))

        alarm_image_path = "Collection of all UI Graphics/dashboard_alarms.png"
        self.alarm_image = tk.PhotoImage(file=alarm_image_path)
        alarm_image_obj = canvas.create_image(0, 560, anchor='nw', image=self.alarm_image)
        canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(alarm_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the news button
        news_image_path = "Collection of all UI Graphics/dashboard_news.png"
        self.news_image = tk.PhotoImage(file=news_image_path)
        news_image_obj = canvas.create_image(0, 670, anchor='nw', image=self.news_image)
        canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(news_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the settings button
        settings_image_path = "Collection of all UI Graphics/dashboard_settings.png"
        self.settings_image = tk.PhotoImage(file=settings_image_path)
        settings_image_obj = canvas.create_image(0, 780, anchor='nw', image=self.settings_image)
        canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(settings_image_obj), controller.show_canvas(Settings)))

        # Retrieves the images, and opens the notifications image
        notifications_image_path = "Collection of all UI Graphics/dashboard_notifications.png"
        self.notifications_image = tk.PhotoImage(file=notifications_image_path)
        notifications_button = canvas.create_image(1027, 19, anchor='nw', image=self.notifications_image)
        canvas.tag_bind(notifications_button, "<ButtonRelease-1>", lambda event: notifications_clicker(self))

        # Retrieves the images, and configures the support image
        support_image_path = "Collection of all UI Graphics/dashboard_support.png"
        self.support_image = tk.PhotoImage(file=support_image_path)
        support_image_obj = canvas.create_image(1155, 16, anchor='nw', image=self.support_image)
        canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(support_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        notes_image_path = "Collection of all UI Graphics/dashboard_notes.png"
        self.notes_image = tk.PhotoImage(file=notes_image_path)
        notes_image_obj = canvas.create_image(1268, 19, anchor='nw', image=self.notes_image)
        canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notes_image_obj), controller.show_canvas(NotesTab)))

        # Retrieves the images, and configures the profile image
        profile_image_path = "Collection of all UI Graphics/dashboard_profile_img.png"
        self.profile_image = tk.PhotoImage(file=profile_image_path)
        profile_image_obj = canvas.create_image(1360, 4, anchor='nw', image=self.profile_image)
        canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(profile_image_obj), controller.show_canvas(Settings)))

        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        # search button command
        def search():
            controller.show_canvas(Charts)
            Charts.update_coin(Collection_of_canvases[Charts], coin_name.get())
            Charts.generate_data(Collection_of_canvases[Charts])
            Charts.generate_chart(Collection_of_canvases[Charts], 365)
            search_entry.delete(0, tk.END)

        # search bar
        coin_name = tk.StringVar(canvas)
        search_img = PhotoImage(file=f"Collection of all UI Graphics/charts_textBox2.png")
        canvas.create_image(713.0, 26.0, image=search_img)
        search_entry = tk.Entry(canvas, textvariable=coin_name, bd=0, bg="#41597c", highlightthickness=0)
        search_entry.place(x=592.0, y=10, width=242.0, height=30)

        # search bar go button
        self.search_btn_img = PhotoImage(file=f"Collection of all UI Graphics/charts_img17.png")
        search_btn = tk.Button(self, image=self.search_btn_img, borderwidth=0, highlightthickness=0, relief="flat",
                               command=search)
        search_btn.place(x=812, y=17, width=20, height=21)

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

        self.entry0_img = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_textBox0.png")
        canvas.create_image(1132.5, 720.5, image=self.entry0_img)
        entry0 = Entry(self, bd=0, bg="#306380", highlightthickness=0)
        entry0.place(x=975, y=611, width=315, height=217)

        self.entry1_img = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_textBox1.png")
        canvas.create_image(754.5, 720.5, image=self.entry1_img)
        entry1 = Entry(self, bd=0, bg="#2da596", highlightthickness=0)
        entry1.place(x=597, y=611, width=315, height=217)

        self.entry2_img = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_textBox2.png")
        canvas.create_image(376.5, 720.5, image=self.entry2_img)
        entry2 = Entry(self, bd=0, bg="#9d5a89", highlightthickness=0)
        entry2.place(x=219, y=611, width=315, height=217)

        self.entry3_img = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_textBox3.png")
        canvas.create_image(1132.5, 352.5, image=self.entry3_img)
        entry3 = Entry(self, bd=0, bg="#646da7", highlightthickness=0)
        entry3.place(x=975, y=243, width=315, height=217)

        self.entry4_img = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_textBox4.png")
        canvas.create_image(754.5, 352.5, image=self.entry4_img)
        entry4 = Entry(self, bd=0, bg="#417e9a", highlightthickness=0)
        entry4.place(x=597, y=243, width=315, height=217)

        self.entry5_img = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_textBox5.png")
        canvas.create_image(376.5, 352.5, image=self.entry5_img)
        entry5 = Entry(self, bd=0, bg="#826fa8", highlightthickness=0)
        entry5.place(x=219, y=243, width=315, height=217)

        self.img0 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b0 = Button(self, image=self.img0, borderwidth=0, highlightthickness=0, relief="flat")
        b0.place(x=1260, y=835, width=20, height=12)

        self.img1 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b1 = Button(self, image=self.img1, borderwidth=0, highlightthickness=0, relief="flat")
        b1.place(x=1232, y=835, width=19, height=12)

        self.img2 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b2 = Button(self, image=self.img2, borderwidth=0, highlightthickness=0, relief="flat")
        b2.place(x=1203, y=835, width=20, height=12)

        self.img3 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b3 = Button(self, image=self.img3, borderwidth=0, highlightthickness=0, relief="flat")
        b3.place(x=880, y=835, width=20, height=12)

        self.img4 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b4 = Button(self, image=self.img4, borderwidth=0, highlightthickness=0, relief="flat")
        b4.place(x=852, y=835, width=19, height=12)

        self.img5 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b5 = Button(self, image=self.img5, borderwidth=0, highlightthickness=0, relief="flat")
        b5.place(x=823, y=835, width=20, height=12)

        self.img6 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b6 = Button(self, image=self.img6, borderwidth=0, highlightthickness=0, relief="flat")
        b6.place(x=500, y=836, width=20, height=12)

        self.img7 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b7 = Button(self, image=self.img7, borderwidth=0, highlightthickness=0, relief="flat")
        b7.place(x=473, y=836, width=19, height=12)

        self.img8 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b8 = Button(self, image=self.img8, borderwidth=0, highlightthickness=0, relief="flat")
        b8.place(x=445, y=836, width=20, height=12)

        self.img9 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b9 = Button(self, image=self.img9, borderwidth=0, highlightthickness=0, relief="flat")
        b9.place(x=1260, y=466, width=20, height=12)

        self.img10 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b10 = Button(self, image=self.img10, borderwidth=0, highlightthickness=0, relief="flat")
        b10.place(x=1232, y=466, width=19, height=12)

        self.img11 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b11 = Button(self, image=self.img11, borderwidth=0, highlightthickness=0, relief="flat")
        b11.place(x=1203, y=466, width=20, height=12)

        self.img12 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b12 = Button(self, image=self.img12, borderwidth=0, highlightthickness=0, relief="flat")
        b12.place(x=880, y=466, width=20, height=12)

        self.img13 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b13 = Button(self, image=self.img13, borderwidth=0, highlightthickness=0, relief="flat")
        b13.place(x=852, y=466, width=19, height=12)

        self.img14 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b14 = Button(self, image=self.img14, borderwidth=0, highlightthickness=0, relief="flat")
        b14.place(x=823, y=466, width=20, height=12)

        self.img15 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b15 = Button(self, image=self.img15, borderwidth=0, highlightthickness=0, relief="flat")
        b15.place(x=500, y=466, width=20, height=12)

        self.img16 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b16 = Button(self, image=self.img16, borderwidth=0, highlightthickness=0, relief="flat")
        b16.place(x=473, y=466, width=19, height=12)

        self.img17 = PhotoImage(file=f"Collection of all UI Graphics/sticky_notes_color_changer.png")
        b17 = Button(self, image=self.img17, borderwidth=0, highlightthickness=0, relief="flat")
        b17.place(x=445, y=466, width=20, height=12)


class Portfolio(tk.Frame):
    """
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1440, height=1024)
        self.controller = controller

        flash_delay = 100  # in milliseconds.

        canvas = Canvas(self, bg="#ffffff", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"Collection of all UI Graphics/portfolio_background.png")
        canvas.create_image(720.0, 512.0, image=self.background_img)

        def AddTransactionClicker():
            """
            TODO
            """
            pop = Toplevel(self)
            pop.geometry('485x704')
            pop.config(height=704, width=485)

            add_transactions_canvas = Canvas(pop, bg="#ffffff", height=704, width=485, bd=0, highlightthickness=0,
                                             relief="ridge")
            add_transactions_canvas.place(x=0, y=0)

            self.add_transactions_background_img = PhotoImage(file=f"Collection of all UI "
                                                                   f"Graphics/add_transaction_background.png")
            add_transactions_canvas.create_image(242.5, 350.0, image=self.add_transactions_background_img)

            # variables to send to manual transaction module
            self.is_Buy = True  # default option is buy
            coin_name_var = tk.StringVar()
            date_purchased_var = tk.StringVar()
            time_purchased_var = tk.StringVar()
            amount_purchased_var = tk.StringVar()
            price_purchased_var = tk.StringVar()
            purchase_fee_var = tk.StringVar()
            currency_selection_var = tk.StringVar()

            """ Entry boxes """
            # currency selection
            self.entry0_img = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_textBox0.png")
            add_transactions_canvas.create_image(336.5, 538.0, image=self.entry0_img)
            entry0 = Entry(pop, textvariable=currency_selection_var, bd=0, bg="#696969", highlightthickness=0)
            entry0.place(x=275.0, y=515, width=123.0, height=44)

            # purchase fee
            self.entry1_img = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_textBox1.png")
            add_transactions_canvas.create_image(147.5, 538.0, image=self.entry1_img)
            entry1 = Entry(pop, textvariable=purchase_fee_var, bd=0, bg="#696969", highlightthickness=0)
            entry1.place(x=86.0, y=515, width=123.0, height=44)

            # price purchased
            self.entry2_img = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_textBox2.png")
            add_transactions_canvas.create_image(336.5, 445.0, image=self.entry2_img)
            entry2 = Entry(pop, textvariable=price_purchased_var, bd=0, bg="#696969", highlightthickness=0)
            entry2.place(x=275.0, y=422, width=123.0, height=44)

            # amount purchased
            self.entry3_img = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_textBox3.png")
            add_transactions_canvas.create_image(147.5, 445.0, image=self.entry3_img)
            entry3 = Entry(pop, textvariable=amount_purchased_var, bd=0, bg="#696969", highlightthickness=0)
            entry3.place(x=86.0, y=422, width=123.0, height=44)

            # time purchased
            self.entry4_img = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_textBox4.png")
            add_transactions_canvas.create_image(336.5, 344.0, image=self.entry4_img)
            entry4 = Entry(pop, textvariable=time_purchased_var, bd=0, bg="#696969", highlightthickness=0)
            entry4.place(x=275.0, y=321, width=123.0, height=44)

            # date purchased
            self.date_purchased_img = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_textBox5.png")
            add_transactions_canvas.create_image(147.5, 344.0, image=self.date_purchased_img)
            date_purchased_entry = Entry(pop, textvariable=date_purchased_var, bd=0, bg="#696969", highlightthickness=0)
            date_purchased_entry.place(x=86.0, y=321, width=123.0, height=44)

            # autofill search function for coins
            coin_listbox = Listbox(add_transactions_canvas)
            coin_list = manual_transaction.get_list_of_coins()

            # updates the listbox
            def update(data):
                # changes the size of the listbox to number of items in list
                listbox_height = len(data)
                if len(data) > 5:
                    listbox_height = 5
                coin_listbox.place(height=(16.5 * listbox_height))

                # clears the listbox
                coin_listbox.delete(0, END)
                for item in data:
                    coin_listbox.insert(END, item)

            # allows users to choose items from list
            def fill_out(event):
                coin_name_entry.delete(0, END)
                coin_name_entry.insert(0, coin_listbox.get(ACTIVE))
                coin_listbox.place_forget()
                date_purchased_entry.place(x=86.0, y=321, width=123.0, height=44)

            # displays in list appropriate items comparatively to entry
            def check():
                # Retrieve user input
                typed = coin_name_entry.get()

                if typed == "":
                    data = coin_list
                else:
                    data = []
                    for each_item in coin_list:
                        if typed.lower() in each_item.lower():
                            data.append(each_item)
                update(data)

            def show_list():
                coin_listbox.place(x=114.0, y=270, width=140.0, height=63)
                date_purchased_entry.place_forget()  # Entry box appears in front of List box
                check()

                coin_listbox.bind("<<ListboxSelect>>", fill_out)

            # coin name
            self.coin_name_img = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_textBox6.png")
            add_transactions_canvas.create_image(242.5, 249.0, image=self.coin_name_img)
            coin_name_entry = Entry(pop, textvariable=coin_name_var, bd=0, bg="#696969", highlightthickness=0)
            coin_name_entry.place(x=106.0, y=226, width=273.0, height=44)
            coin_name_entry.bind("<KeyRelease>", lambda event: show_list())
            """ End of Entry boxes """

            def buy_or_sell(buy_or_sell):
                self.is_Buy = buy_or_sell

            def submit():
                # grabs all entry box entries

                coin_name = coin_name_var.get()
                date_purchased = date_purchased_var.get()
                time_purchased = time_purchased_var.get()
                amount_purchased = amount_purchased_var.get()
                price_purchased = price_purchased_var.get()
                purchase_fee = purchase_fee_var.get()
                currency_selection = currency_selection_var.get()
                # print(str(coin_name)+'\n'+str(date_purchased))
                print(self.is_Buy)

                if currency_selection != "":
                    mt = ManualTransaction(coin_name, self.is_Buy, price_purchased, amount_purchased, "target",
                                           purchase_fee, "time")

                    print("works")

                    pop.destroy()

            # submit button
            self.submit_button_image = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_img0.png")
            submit_button = add_transactions_canvas.create_image(181, 620, anchor='nw', image=self.submit_button_image)
            add_transactions_canvas.tag_bind(submit_button, "<ButtonRelease-1>", lambda event: submit())

            # transfer button
            self.transfer_button_image = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_img1.png")
            transfer_button = add_transactions_canvas.create_image(313, 125, anchor='nw',
                                                                   image=self.transfer_button_image)
            add_transactions_canvas.tag_bind(transfer_button, "<ButtonRelease-1>")

            # sell button
            self.sell_button_image = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_img2.png")
            sell_button = add_transactions_canvas.create_image(200, 125, anchor='nw', image=self.sell_button_image)
            add_transactions_canvas.tag_bind(sell_button, "<ButtonRelease-1>", lambda event: buy_or_sell(False))

            # buy button
            self.buy_button_image = PhotoImage(file=f"Collection of all UI Graphics/add_transaction_img3.png")
            buy_button = add_transactions_canvas.create_image(83, 125, anchor='nw', image=self.buy_button_image)
            add_transactions_canvas.tag_bind(buy_button, "<ButtonRelease-1>", lambda event: buy_or_sell(True))

        # creates and opens up a log out pop up
        logout_image_path = "Collection of all UI Graphics/dashboard_logout.png"
        self.logout_image = tk.PhotoImage(file=logout_image_path)
        log_out_button = canvas.create_image(45, 950, anchor='nw', image=self.logout_image)
        canvas.tag_bind(log_out_button, "<ButtonRelease-1>", lambda event: logout_button_display(self, self.controller))

        ycoor = 0
        portfolio = {}
        for coin in portfolio:
            avg_buy = portfolio[coin]["avg_price"]
            amount = portfolio[coin]["amount"]

            target = portfolio[coin]["target"]
            current_price = 0
            profit_and_loss = current_price - avg_buy * amount
            percent_profit = current_price / avg_buy * amount * 100
            net_balance = current_price * amount

            canvas.create_text(601.0, 904.0, text=f"${current_price}", fill="#ffffff",
                               font=("SourceCodePro-Regular", int(13.0)))
            canvas.create_text(763.0, 886.0, text=f"${net_balance}", fill="#ffffff",
                               font=("SourceCodePro-Regular", int(13.0)))
            canvas.create_text(1270.0, 895.0, text=f"${profit_and_loss}", fill="#ffffff",
                               font=("SourceCodePro-Regular", int(13.0)))
            canvas.create_text(1270.0, 917.0, text=f"{percent_profit}%", fill="#ffffff",
                               font=("RopaSans-Regular", int(13.0)))
            canvas.create_text(763.0, 912.0, text="0", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
            canvas.create_text(376.0, 905.0, text="-", fill="#ffffff", font=("Rosarivo-Regular", int(13.0)))

        """
        canvas.create_text(601.0, 904.0, text="First", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(763.0, 886.0, text="Second", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 895.0, text="Third", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 917.0, text="0.00%", fill="#ffffff", font=("RopaSans-Regular", int(13.0)))
        canvas.create_text(763.0, 912.0, text="0", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(376.0, 905.0, text="-", fill="#ffffff", font=("Rosarivo-Regular", int(13.0)))
        canvas.create_text(978.5, 191.5, text="0.00%", fill="#ffffff", font=("SourceCodePro-Regular", int(15.0)))
        canvas.create_text(717.5, 191.5, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(15.0)))
        canvas.create_text(1196.5, 191.5, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(15.0)))
        canvas.create_text(374.5, 197.5, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(25.0)))
        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))
        canvas.create_text(601.0, 387.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(759.0, 387.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 378.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(938.0, 387.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(938.0, 463.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(938.0, 549.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(938.0, 640.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(938.0, 724.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(938.0, 818.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(938.0, 904.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1131.0, 387.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1131.0, 460.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1131.0, 546.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1131.0, 637.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1131.0, 721.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1131.0, 815.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1131.0, 901.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 399.0, text="0.00%", fill="#ffffff", font=("RopaSans-Regular", int(13.0)))
        canvas.create_text(759.0, 409.0, text="0 ", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(376.0, 384.0, text="-", fill="#ffffff", font=("Rosarivo-Regular", int(13.0)))
        canvas.create_text(601.0, 466.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(763.0, 451.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 460.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 482.0, text="0.00%", fill="#ffffff", font=("RopaSans-Regular", int(13.0)))
        canvas.create_text(763.0, 477.0, text="0", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(376.0, 470.0, text="-", fill="#ffffff", font=("Rosarivo-Regular", int(13.0)))
        canvas.create_text(601.0, 562.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(763.0, 538.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 547.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 569.0, text="0.00%", fill="#ffffff", font=("RopaSans-Regular", int(13.0)))
        canvas.create_text(763.0, 564.0, text="0", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(376.0, 557.0, text="-", fill="#ffffff", font=("Rosarivo-Regular", int(13.0)))
        canvas.create_text(601.0, 644.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(763.0, 625.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 634.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 656.0, text="0.00%", fill="#ffffff", font=("RopaSans-Regular", int(13.0)))
        canvas.create_text(763.0, 651.0, text="0", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(376.0, 644.0, text="-", fill="#ffffff", font=("Rosarivo-Regular", int(13.0)))
        canvas.create_text(601.0, 727.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(763.0, 710.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 719.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 741.0, text="0.00%", fill="#ffffff", font=("RopaSans-Regular", int(13.0)))
        canvas.create_text(763.0, 736.0, text="0", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(376.0, 729.0, text="-", fill="#ffffff", font=("Rosarivo-Regular", int(13.0)))
        canvas.create_text(601.0, 822.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(763.0, 803.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 812.0, text="$", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(1270.0, 834.0, text="0.00%", fill="#ffffff", font=("RopaSans-Regular", int(13.0)))
        canvas.create_text(763.0, 829.0, text="0", fill="#ffffff", font=("SourceCodePro-Regular", int(13.0)))
        canvas.create_text(376.0, 822.0, text="-", fill="#ffffff", font=("Rosarivo-Regular", int(13.0)))
        canvas.create_text(378.5, 237.0, text="0.00%", fill="#ffffff", font=("SourceCodePro-Regular", int(15.0)))
        """
        # Retrieves the images, and configures the dashboard button
        dashboard_image_path = "Collection of all UI Graphics/dashboard_dashboard.png"
        self.dashboard_image = tk.PhotoImage(file=dashboard_image_path)
        dashboard_image_obj = canvas.create_image(0, 120, anchor='nw', image=self.dashboard_image)
        canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(dashboard_image_obj), controller.show_canvas(Dashboard)))

        # Retrieves the images, and configures the simulated trading button
        simulated_trading_image_path = "Collection of all UI Graphics/dashboard_simulated_trading.png"
        self.simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
        simulated_trading_image_obj = canvas.create_image(0, 230, anchor='nw', image=self.simulated_trading_image)
        canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(simulated_trading_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the charts button
        charts_image_path = "Collection of all UI Graphics/dashboard_charts.png"
        self.charts_image = tk.PhotoImage(file=charts_image_path)
        charts_image_obj = canvas.create_image(0, 340, anchor='nw', image=self.charts_image)
        canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(charts_image_obj), controller.show_canvas(Charts)))

        # Retrieves the images, and configures the portfolio button
        portfolio_image_path = "Collection of all UI Graphics/dashboard_portfolio.png"
        self.portfolio_image = tk.PhotoImage(file=portfolio_image_path)
        portfolio_image_obj = canvas.create_image(0, 450, anchor='nw', image=self.portfolio_image)
        canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(portfolio_image_obj), controller.show_canvas(Portfolio)))

        alarm_image_path = "Collection of all UI Graphics/dashboard_alarms.png"
        self.alarm_image = tk.PhotoImage(file=alarm_image_path)
        alarm_image_obj = canvas.create_image(0, 560, anchor='nw', image=self.alarm_image)
        canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(alarm_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the news button
        news_image_path = "Collection of all UI Graphics/dashboard_news.png"
        self.news_image = tk.PhotoImage(file=news_image_path)
        news_image_obj = canvas.create_image(0, 670, anchor='nw', image=self.news_image)
        canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(news_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the settings button
        settings_image_path = "Collection of all UI Graphics/dashboard_settings.png"
        self.settings_image = tk.PhotoImage(file=settings_image_path)
        settings_image_obj = canvas.create_image(0, 780, anchor='nw', image=self.settings_image)
        canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(settings_image_obj), controller.show_canvas(Settings)))

        # Retrieves the images, and opens the notifications image
        notifications_image_path = "Collection of all UI Graphics/dashboard_notifications.png"
        self.notifications_image = tk.PhotoImage(file=notifications_image_path)
        notifications_button = canvas.create_image(1027, 19, anchor='nw', image=self.notifications_image)
        canvas.tag_bind(notifications_button, "<ButtonRelease-1>", lambda event: notifications_clicker(self))

        # Retrieves the images, and configures the support image
        support_image_path = "Collection of all UI Graphics/dashboard_support.png"
        self.support_image = tk.PhotoImage(file=support_image_path)
        support_image_obj = canvas.create_image(1155, 16, anchor='nw', image=self.support_image)
        canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(support_image_obj), controller.show_canvas(ComingSoon)))

        # Retrieves the images, and configures the profile image
        notes_image_path = "Collection of all UI Graphics/dashboard_notes.png"
        self.notes_image = tk.PhotoImage(file=notes_image_path)
        notes_image_obj = canvas.create_image(1268, 19, anchor='nw', image=self.notes_image)
        canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notes_image_obj), controller.show_canvas(NotesTab)))

        # Retrieves the images, and configures the profile image
        profile_image_path = "Collection of all UI Graphics/dashboard_profile_img.png"
        self.profile_image = tk.PhotoImage(file=profile_image_path)
        profile_image_obj = canvas.create_image(1360, 4, anchor='nw', image=self.profile_image)
        canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(profile_image_obj), controller.show_canvas(Settings)))

        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        # search button command
        def search(coin_name=None, search_entry=None):
            controller.show_canvas(Charts)
            Charts.update_coin(Collection_of_canvases[Charts], coin_name.get())
            Charts.generate_data(Collection_of_canvases[Charts])
            Charts.generate_chart(Collection_of_canvases[Charts], 365)
            search_entry.delete(0, tk.END)

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

        self.entry0_img = PhotoImage(file=f"Collection of all UI Graphics/portfolio_textBox0.png")
        canvas.create_image(977.0, 251.0, image=self.entry0_img)

        entry0 = Entry(self, bd=0, bg="#053f53", highlightthickness=0)
        entry0.place(x=856.0, y=235, width=242.0, height=30)

        # add transactions button
        self.add_transactions_img = PhotoImage(file=f"Collection of all UI Graphics/portfolio_img12.png")
        notifications_button = canvas.create_image(1140, 226, anchor='nw', image=self.add_transactions_img)
        canvas.tag_bind(notifications_button, "<ButtonRelease-1>", lambda event: AddTransactionClicker())

        self.all_option_img = PhotoImage(file=f"Collection of all UI Graphics/portfolio_img13.png")
        all_option_button = Button(self, image=self.all_option_img, borderwidth=0, highlightthickness=0, relief="flat")
        all_option_button.place(x=883, y=97, width=43, height=25)

        self.six_month_option_img = PhotoImage(file=f"Collection of all UI Graphics/portfolio_img14.png")
        six_month_option_button = Button(self, image=self.six_month_option_img, borderwidth=0, highlightthickness=0,
                                         relief="flat")
        six_month_option_button.place(x=829, y=97, width=32, height=23)

        self.three_month_option_img = PhotoImage(file=f"Collection of all UI Graphics/portfolio_img15.png")
        three_month_option_button = Button(self, image=self.three_month_option_img, borderwidth=0, highlightthickness=0,
                                           relief="flat")
        three_month_option_button.place(x=772, y=96, width=30, height=30)

        self.one_month_option_img = PhotoImage(file=f"Collection of all UI Graphics/portfolio_img16.png")
        one_month_option_button = Button(self, image=self.one_month_option_img, borderwidth=0, highlightthickness=0,
                                         relief="flat")
        one_month_option_button.place(x=722, y=97, width=29, height=25)

        self.one_week_option_img = PhotoImage(file=f"Collection of all UI Graphics/portfolio_img17.png")
        one_week_option_button = Button(self, image=self.one_week_option_img, borderwidth=0, highlightthickness=0,
                                        relief="flat")
        one_week_option_button.place(x=670, y=98, width=30, height=28)

        self.oneday_option_img = PhotoImage(file=f"Collection of all UI Graphics/portfolio_img18.png")
        oneday_option_button = Button(self, image=self.oneday_option_img, borderwidth=0, highlightthickness=0,
                                      relief="flat")
        oneday_option_button.place(x=614, y=96, width=32, height=26)

        self.search_icon = PhotoImage(file=f"Collection of all UI Graphics/portfolio_img19.png")
        search_button = Button(self, image=self.search_icon, borderwidth=0, highlightthickness=0, relief="flat")
        search_button.place(x=1074, y=238, width=30, height=27)


def main():
    """
    Launchpad method to compile, and run this module
    :return: runs the program
    """
    app = CryptocurrencyLedger()
    app.mainloop()


if __name__ == '__main__':
    main()