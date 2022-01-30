from tkinter import *

login_window = Tk()

login_window.geometry("1000x600")
login_window.configure(bg="#343333")

login_canvas = Canvas(login_window, bg="#343333", height=600, width=1000, bd=0, highlightthickness=0, relief="ridge")
login_canvas.place(x=0, y=0)

login_background = PhotoImage(file=f"login_background.png")
background = login_canvas.create_image(395.0, 300.0, image=login_background)

sign_in_button = PhotoImage(file=f"sign_in_button.png")
sing_in_button_location = Button(image=sign_in_button, borderwidth=0, highlightthickness=0, relief="flat")
sing_in_button_location.place(x=659, y=417, width=159, height=53)

forgot_password_button = PhotoImage(file=f"forgot_password_button.png")
forgot_password_location = Button(image=forgot_password_button, borderwidth=0, highlightthickness=0, relief="flat")
forgot_password_location.place(x=444, y=537, width=142, height=50)

sign_up_button = PhotoImage(file=f"sign_up_button.png")
sign_up_button_location = Button(image=sign_up_button, borderwidth=0, highlightthickness=0, relief="flat")
sign_up_button_location.place(x=864, y=537, width=136, height=46)

login_textbox_one = PhotoImage(file=f"login_textbox.png")
textbox_one = login_canvas.create_image(738.5, 263.0, image=login_textbox_one)
textbox_one_location = Entry(bd=0, bg="#696969", highlightthickness=0)
textbox_one_location.place(x=602.0, y=240, width=273.0, height=44)

login_textbox_two = PhotoImage(file=f"login_textbox.png")
textbox_two = login_canvas.create_image(738.5, 368.0, image=login_textbox_two)
textbox_two_location = Entry(bd=0, bg="#696969", highlightthickness=0)
textbox_two_location.place(x=602.0, y=345, width=273.0, height=44)

login_window.resizable(False, False)
login_window.mainloop()
