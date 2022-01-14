""" Simple UI module which contains the logic to display an enrollment screen for a new user to register """
import tkinter
from tkinter import *

"""
TODO 
- Capture the input information entered by the user - Completed
- Record this information -Design Decision- [Dictionary would make sense, else send to a .txt file] - Completed
- Send an email to the user saying that have successfully registered their account - Completed
"""


def store_enrollment_info():
    """ Prints the email, name, and password to the console """
    global user_email_entry
    global user_password_entry
    global user_phone_number_entry

    # Logic to captures the user input
    user_email_entry = user_email_str.get()
    user_password_entry = user_password_str.get()
    user_phone_number_entry = user_phone_number_str.get()

    # Clears the entry when the user clicks "Get Started"
    user_email_str.set("")
    user_password_str.set("")
    user_phone_number_str.set("")
    return_user_information()


def return_user_information():
    """ Stores the user information into a dictionary where it's values is set to password, and phone number """
    dict_of_enrolled = {}
    if user_email_entry not in dict_of_enrolled:
        dict_of_enrolled[user_email_entry] = {user_password_entry, user_phone_number_entry}

    return dict_of_enrolled


enrollment_screen = Tk()

sign_in_canvas = Canvas(enrollment_screen, bg="#ffffff", height=600, width=1000, bd=0, highlightthickness=0
                        , relief="ridge")
sign_in_canvas.place(x=0, y=0)

# Initializes the main screen size and sets the color to white
enrollment_screen.geometry("1000x600")
enrollment_screen.configure(bg="#ffffff")

# Initializes background objects
background_img = PhotoImage(file=f"background.png")
background = sign_in_canvas.create_image(500.5, 300.0, image=background_img)

# Declaration of string variable which captures user entries
user_email_str = tkinter.StringVar()
user_password_str = tkinter.StringVar()
user_phone_number_str = tkinter.StringVar()

# Initializes the email entry boxes
email_entry_img = PhotoImage(file=f"img_textBox0.png")
email_background = sign_in_canvas.create_image(722.5, 179.5, image=email_entry_img)
email_entry = Entry(textvariable=user_email_str, bd=0, bg="#e9e9e9", highlightthickness=0)
email_entry.place(x=588.5, y=154, width=268.0, height=49)

# Initializes user entry box objects 1-2
password_img = PhotoImage(file=f"img_textBox1.png")
password_background = sign_in_canvas.create_image(722.5, 298.5, image=password_img)
user_password_entry = Entry(textvariable=user_password_str, bd=0, bg="#e9e9e9", highlightthickness=0)
user_password_entry.place(x=588.5, y=273, width=268.0, height=49)

# Initializes the phone number entry boxes
phone_number_img = PhotoImage(file=f"img_textBox2.png")
phone_number_background = sign_in_canvas.create_image(722.5, 417.5, image=phone_number_img)
phone_number_entry = Entry(textvariable=user_phone_number_str, bd=0, bg="#e9e9e9", highlightthickness=0)
phone_number_entry.place(x=588.5, y=392, width=268.0, height=49)

splash_image = PhotoImage(file=f"img0.png")  # Crypto picture that shows on the enrollment screen

# Initializes the "Get Started" button
get_started_button = Button(image=splash_image, borderwidth=0, highlightthickness=0, relief="flat"
                            , command=store_enrollment_info)
get_started_button.place(x=636, y=481, height=53)

enrollment_screen.resizable(False, False)
enrollment_screen.mainloop()

if __name__ == '__main__':
    pass
