""" Simple UI module which contains the logic to display an enrollment screen for a new user to register """
import tkinter
from tkinter import *

'''
def store_enrollment_info():
    """ Prints the email, name, and password to the console """
    global user_email_entry
    global user_password_entry
    global user_name_entry

    # Logic to captures the user input
    user_email_entry = user_email_str.get()
    user_password_entry = user_password_str.get()
    user_name_entry = user_name_str.get()

    # Clears the entry when the user clicks "Get Started"
    user_email_str.set("")
    user_password_str.set("")
    user_name_str.set("")
    #return_user_information()
'''
'''
def return_user_information():
    """
    Stores the user information into a dictionary where it's values is set to password, and user name
    """
    global dict_of_enrolled
    dict_of_enrolled = {}
    if user_email_entry not in dict_of_enrolled:
        dict_of_enrolled[user_email_entry] = {user_password_entry, user_name_entry}
    return dict_of_enrolled
'''

enrollment_window = Tk()

enrollment_window.geometry("1000x600")
enrollment_window.configure(bg="#343333")

enrollment_canvas = Canvas(enrollment_window, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0,
                           relief="ridge")
enrollment_canvas.place(x=0, y=0)

enrollment_background = PhotoImage(file=f"enrollment_background.png")
background = enrollment_canvas.create_image(348.0, 300.0, image=enrollment_background)

# Declaration of string variable which captures user entries
user_email_str = tkinter.StringVar()
user_password_str = tkinter.StringVar()
user_name_str = tkinter.StringVar()

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

enrollment_canvas.create_text(727.5, 71.5, text="Create Account", fill="#ffffff", font=("Rosarivo-Regular", int(36.0)))

if __name__ == '__main__':
    enrollment_window.resizable(False, False)
    enrollment_window.mainloop()
 #   store_enrollment_info()
