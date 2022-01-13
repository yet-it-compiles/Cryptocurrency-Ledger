""" Simple UI module which contains the logic to display an enrollment screen for a new user to register """
import tkinter
from tkinter import *

"""
TODO 
- Capture the input information entered by the user - Completed
- Record this information -Design Decision- [Dictionary would make sense, else send to a .txt file]
- Send an email to the user saying that have successfully registered their account
- 
"""


def return_enrollment_info():
    """ Prints the email, name, and password to the console """
    user_email_entry = user_email.get()
    user_password_entry = user_password.get()
    user_phone_number_entry = user_phone_number.get()

    print("Should be the name ", user_email_entry)
    print("Should be the name ", user_password_entry)
    print("Should be the name ", user_phone_number_entry)

    # Clears the entry when the user clicks "Get Started
    user_email.set("")
    user_password.set("")
    user_phone_number.set("")


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

user_email = tkinter.StringVar()
user_password = tkinter.StringVar()
user_phone_number = tkinter.StringVar()

# Initializes user entry box objects 1-2
email_entry_img = PhotoImage(file=f"img_textBox0.png")
email_background = sign_in_canvas.create_image(722.5, 179.5, image=email_entry_img)
email_entry = Entry(textvariable=user_email, bd=0, bg="#e9e9e9", highlightthickness=0)
email_entry.place(x=588.5, y=154, width=268.0, height=49)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = sign_in_canvas.create_image(722.5, 298.5, image=entry1_img)
entry1 = Entry(textvariable=user_password, bd=0, bg="#e9e9e9", highlightthickness=0)
entry1.place(x=588.5, y=273, width=268.0, height=49)

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = sign_in_canvas.create_image(722.5, 417.5, image=entry2_img)
entry2 = Entry(textvariable=user_phone_number, bd=0, bg="#e9e9e9", highlightthickness=0)
entry2.place(x=588.5, y=392, width=268.0, height=49)

splash_image = PhotoImage(file=f"img0.png")  # Crypto picture that shows on the enrollment screen

# Initializes user entry box objects 1-2
b0 = Button(image=splash_image, borderwidth=0, highlightthickness=0, relief="flat", command=return_enrollment_info)
b0.place(x=636, y=481, height=53)

enrollment_screen.resizable(False, False)
enrollment_screen.mainloop()
name = entry1.get()
print("Name")

if __name__ == '__main__':
    pass
