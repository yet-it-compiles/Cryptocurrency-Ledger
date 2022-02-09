""" Simple UI module which contains the logic to display an enrollment screen for a new user to register """
import tkinter
from tkinter import *
from password_encryption import PasswordEncryption as encryption 

class EnrollmentInterface:
    enrollment_window = Tk()
    user_email_str = tkinter.StringVar()
    user_password_str = tkinter.StringVar()
    user_name_str = tkinter.StringVar()
    dict_of_enrolled = {}

    def store_enrollment_info(self):
        """ Prints the email, name, and password to the console """
        # Logic to captures the user input
        user_email_entry = self.user_email_str.get()
        user_password_entry = self.user_password_str.get()
        
        # all that is necessary to encrypt password
        encrypted_password_entry = user_password_entry.encrypt()
        
        user_name_entry = self.user_name_str.get()

        # Clears the entry when the user clicks "Get Started"
        self.user_email_str.set("")
        self.user_password_str.set("")
        self.user_name_str.set("")

        if user_email_entry not in self.dict_of_enrolled:
            self.dict_of_enrolled[user_email_entry] = {user_password_entry, user_name_entry}
            # 
            # self.dict_of_enrolled[user_email_entry] = {encrypted_password_entry, user_name_entry}
        return self.dict_of_enrolled

    enrollment_window.geometry("1000x600")
    enrollment_window.configure(bg="#343333")

    enrollment_canvas = Canvas(enrollment_window, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0,
                               relief="ridge")
    enrollment_canvas.place(x=0, y=0)

    enrollment_background = PhotoImage(file=f"enrollment_background.png")
    background = enrollment_canvas.create_image(348.0, 300.0, image=enrollment_background)

    enrollment_text_box = PhotoImage(file=f"enrollment_textBox.png")
    enrollment_text_background = enrollment_canvas.create_image(722.5, 177.0, image=enrollment_text_box)
    enrollment_text_box_location = Entry(textvariable=user_email_str, bd=0, bg="#696969", highlightthickness=0)
    enrollment_text_box_location.place(x=586.0, y=154, width=273.0, height=44)

    enrollment_text_box_2 = PhotoImage(file=f"enrollment_textBox.png")
    enrollment_text_background_2 = enrollment_canvas.create_image(722.5, 293.0, image=enrollment_text_box_2)
    enrollment_text_box_location_2 = Entry(textvariable=user_password_str, bd=0, bg="#696969", highlightthickness=0)
    enrollment_text_box_location_2.place(x=586.0, y=270, width=273.0, height=44)

    enrollment_text_box_3 = PhotoImage(file=f"enrollment_textBox.png")
    enrollment_text_background_3 = enrollment_canvas.create_image(722.5, 408.0, image=enrollment_text_box_3)
    enrollment_text_box_location_3 = Entry(textvariable=user_name_str, bd=0, bg="#696969", highlightthickness=0)
    enrollment_text_box_location_3.place(x=586.0, y=385, width=273.0, height=44)

    get_started_button = PhotoImage(file=f"enrollment_get_started.png")
    get_started_background = Button(image=get_started_button, borderwidth=0, highlightthickness=0, relief="flat")
    get_started_background.place(x=636, y=481, width=161, height=53)

    enrollment_canvas.create_text(727.5, 71.5, text="Create Account", fill="#ffffff",
                                  font=("Rosarivo-Regular", int(36.0)))

    enrollment_window.resizable(False, False)
    enrollment_window.mainloop()
