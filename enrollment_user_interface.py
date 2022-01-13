from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.5, 300.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    722.5, 179.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0)

entry0.place(
    x = 588.5, y = 154,
    width = 268.0,
    height = 49)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    722.5, 298.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0)

entry1.place(
    x = 588.5, y = 273,
    width = 268.0,
    height = 49)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    722.5, 417.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0)

entry2.place(
    x = 588.5, y = 392,
    width = 268.0,
    height = 49)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 636, y = 481,
    width = 161,
    height = 53)

window.resizable(False, False)
window.mainloop()
