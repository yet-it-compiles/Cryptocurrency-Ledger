from tkinter import *

canvas = Canvas(self, bg="#ffffff", height=704, width=485, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(242.5, 350.0, image=background_img)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(336.5, 538.0, image=entry0_img)

entry0 = Entry(bd=0, bg="#696969", highlightthickness=0)

entry0.place(x=275.0, y=515, width=123.0, height=44)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(147.5, 538.0, image=entry1_img)

entry1 = Entry(bd=0, bg="#696969", highlightthickness=0)

entry1.place(x=86.0, y=515, width=123.0, height=44)

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = canvas.create_image(336.5, 445.0, image=entry2_img)

entry2 = Entry(bd=0, bg="#696969", highlightthickness=0)

entry2.place(x=275.0, y=422, width=123.0, height=44)

entry3_img = PhotoImage(file=f"img_textBox3.png")
entry3_bg = canvas.create_image(147.5, 445.0, image=entry3_img)

entry3 = Entry(bd=0, bg="#696969", highlightthickness=0)

entry3.place(x=86.0, y=422, width=123.0, height=44)

entry4_img = PhotoImage(file=f"img_textBox4.png")
entry4_bg = canvas.create_image(336.5, 344.0, image=entry4_img)

entry4 = Entry(bd=0, bg="#696969", highlightthickness=0)

entry4.place(x=275.0, y=321, width=123.0, height=44)

entry5_img = PhotoImage(file=f"img_textBox5.png")
entry5_bg = canvas.create_image(147.5, 344.0, image=entry5_img)

entry5 = Entry(bd=0, bg="#696969", highlightthickness=0)

entry5.place(x=86.0, y=321, width=123.0, height=44)

entry6_img = PhotoImage(file=f"img_textBox6.png")
entry6_bg = canvas.create_image(242.5, 249.0, image=entry6_img)

entry6 = Entry(bd=0, bg="#696969", highlightthickness=0)

entry6.place(x=106.0, y=226, width=273.0, height=44)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, relief="flat")

b0.place(x=181, y=620, width=123, height=49)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(image=img1, borderwidth=0, highlightthickness=0, relief="flat")

b1.place(x=313, y=125, width=89, height=42)

img2 = PhotoImage(file=f"img2.png")
b2 = Button(image=img2, borderwidth=0, highlightthickness=0, relief="flat")

b2.place(x=200, y=125, width=84, height=42)

img3 = PhotoImage(file=f"img3.png")
b3 = Button(image=img3, borderwidth=0, highlightthickness=0, relief="flat")

b3.place(x=83, y=125, width=84, height=42)

