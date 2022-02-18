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
    x = 1261, y = 17,
    width = 76,
    height = 59)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 1145, y = 6,
    width = 104,
    height = 64)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 1022, y = 12,
    width = 95,
    height = 55)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 38, y = 920,
    width = 46,
    height = 43)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 13, y = 781,
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
    x = 14, y = 670,
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
    x = 16, y = 559,
    width = 91,
    height = 90)

img8 = PhotoImage(file = f"img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 14, y = 447,
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
    x = 14, y = 335,
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
    x = 14, y = 221,
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
    x = 14, y = 105,
    width = 89,
    height = 90)

canvas.create_text(
    1398.5, 68.5,
    text = "John Doe",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(12.0)))

canvas.create_text(
    274.0, 100.5,
    text = "$",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(18.0)))

canvas.create_text(
    303.0, 428.0,
    text = "Assets 1",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    948.0, 425.0,
    text = "Percent Change  1",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    729.0, 425.0,
    text = "Currency Price 1",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    538.0, 428.0,
    text = "Balance 1",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    303.0, 492.0,
    text = "Assets 2",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    948.0, 489.0,
    text = "Percent Change  2",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    729.0, 489.0,
    text = "Currency Price 2",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    538.0, 492.0,
    text = "Balance 2",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    303.0, 555.0,
    text = "Assets 3",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    948.0, 552.0,
    text = "Percent Change  3",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    729.0, 552.0,
    text = "Currency Price 3",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    538.0, 555.0,
    text = "Balance 3",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    303.0, 624.0,
    text = "Assets 4",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    948.0, 621.0,
    text = "Percent Change  14",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    729.0, 621.0,
    text = "Currency Price 4",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    538.0, 625.0,
    text = "Balance 4",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    303.0, 693.0,
    text = "Assets 5",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    948.0, 690.0,
    text = "Percent Change  5",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    729.0, 690.0,
    text = "Currency Price 5",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    538.0, 693.0,
    text = "Balance 5",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    303.0, 762.0,
    text = "Assets 6",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    948.0, 759.0,
    text = "Percent Change  6",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    729.0, 759.0,
    text = "Currency Price 6",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    538.0, 762.0,
    text = "Balance 6",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    303.0, 831.0,
    text = "Assets 7",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    948.0, 828.0,
    text = "Percent Change  7",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    729.0, 828.0,
    text = "Currency Price 7",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    538.0, 831.0,
    text = "Balance 7",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    303.0, 900.0,
    text = "Assets 8",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    948.0, 897.0,
    text = "Percent Change  8",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    729.0, 897.0,
    text = "Currency Price 8",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

canvas.create_text(
    538.0, 900.0,
    text = "Balance 8",
    fill = "#ffffff",
    font = ("Rosarivo-Regular", int(13.0)))

img12 = PhotoImage(file = f"img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b12.place(
    x = 1236, y = 950,
    width = 22,
    height = 26)

img13 = PhotoImage(file = f"img13.png")
b13 = Button(
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b13.place(
    x = 1261, y = 949,
    width = 19,
    height = 23)

window.resizable(False, False)
window.mainloop()
