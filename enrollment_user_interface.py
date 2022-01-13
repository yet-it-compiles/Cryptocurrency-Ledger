""" Simple UI module which contains the logic to display an enrollment screen for a new user to register """
from tkinter import *


class EnrollmentScreen:
    enrollment_screen = Tk()

    def __init__(self):
        """ Initializes the enrollment screen objects """
        sign_in_canvas = Canvas(self.enrollment_screen, bg="#ffffff", height=600, width=1000, bd=0, highlightthickness=0
                                , relief="ridge")
        sign_in_canvas.place(x=0, y=0)

        # Initializes the main screen size and sets the color to white
        self.enrollment_screen.geometry("1000x600")
        self.enrollment_screen.configure(bg="#ffffff")

        # Initializes background objects
        background_img = PhotoImage(file=f"background.png")
        background = sign_in_canvas.create_image(500.5, 300.0, image=background_img)

        # Initializes user entry box objects 1-2
        entry0_img = PhotoImage(file=f"img_textBox0.png")
        entry0_bg = sign_in_canvas.create_image(722.5, 179.5, image=entry0_img)
        entry0 = Entry(bd=0, bg="#e9e9e9", highlightthickness=0)
        entry0.place(x=588.5, y=154, width=268.0, height=49)

        entry1_img = PhotoImage(file=f"img_textBox1.png")
        entry1_bg = sign_in_canvas.create_image(722.5, 298.5, image=entry1_img)
        entry1 = Entry(bd=0, bg="#e9e9e9", highlightthickness=0)
        entry1.place(x=588.5, y=273, width=268.0, height=49)

        entry2_img = PhotoImage(file=f"img_textBox2.png")
        entry2_bg = sign_in_canvas.create_image(722.5, 417.5, image=entry2_img)
        entry2 = Entry(bd=0, bg="#e9e9e9", highlightthickness=0)
        entry2.place(x=588.5, y=392, width=268.0, height=49)

        splash_image = PhotoImage(file=f"img0.png")  # Crypto picture that shows on the enrollment screen

        # Initializes user entry box objects 1-2
        b0 = Button(image=splash_image, borderwidth=0, highlightthickness=0, relief="flat")
        b0.place(x=636, y=481, height=53)

        self.enrollment_screen.resizable(False, False)
        self.enrollment_screen.mainloop()


if __name__ == '__main__':
    display_enrollment_screen = EnrollmentScreen()
