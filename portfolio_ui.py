from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    720.0, 512.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 1360, y = 4,
    width = 68,
    height = 57)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 1275, y = 24,
    width = 39,
    height = 42)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 1149, y = 16,
    width = 81,
    height = 49)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 1027, y = 19,
    width = 81,
    height = 46)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 44, y = 925,
    width = 30,
    height = 30)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 13, y = 777,
    width = 90,
    height = 90)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 13, y = 668,
    width = 90,
    height = 90)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 13, y = 559,
    width = 90,
    height = 90)

img8 = PhotoImage(file = f"img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 13, y = 450,
    width = 90,
    height = 90)

img9 = PhotoImage(file = f"img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 12, y = 341,
    width = 90,
    height = 90)

img10 = PhotoImage(file = f"img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 14, y = 232,
    width = 90,
    height = 90)

img11 = PhotoImage(file = f"img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b11.place(
    x = 14, y = 123,
    width = 90,
    height = 90)

canvas.create_text(
    1398.5, 68.5,
    text = "John Doe",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(12.0)))

canvas.create_text(
    440.5, 93.5,
    text = "$",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(18.0)))

canvas.create_text(
    314.0, 345.5,
    text = "Assets",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(19.0)))

canvas.create_text(
    479.0, 345.5,
    text = "Balance",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(19.0)))

canvas.create_text(
    676.0, 345.5,
    text = "Current Price",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(19.0)))

canvas.create_text(
    928.5, 345.5,
    text = "Percent Change",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(19.0)))

canvas.create_text(
    1143.0, 345.5,
    text = "Action",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(19.0)))

window.resizable(False, False)
window.mainloop()
