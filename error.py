from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("558x260")
window.configure(bg = "#343333")
canvas = Canvas(
    window,
    bg = "#343333",
    height = 260,
    width = 558,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 245, y = 185,
    width = 67,
    height = 11)

canvas.create_text(
    274.5, 124.5,
    text = "You have entered the wrong username or password",
    fill = "#f55959",
    font = ("None", int(16.0)))

window.resizable(False, False)
window.mainloop()
