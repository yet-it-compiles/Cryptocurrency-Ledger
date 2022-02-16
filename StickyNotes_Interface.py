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
    x = 45, y = 937,
    width = 30,
    height = 30)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 14, y = 789,
    width = 90,
    height = 90)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 14, y = 680,
    width = 90,
    height = 90)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 14, y = 571,
    width = 90,
    height = 90)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 14, y = 462,
    width = 90,
    height = 90)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 13, y = 353,
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
    x = 15, y = 244,
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
    x = 15, y = 135,
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
    x = 1360, y = 4,
    width = 68,
    height = 57)

img9 = PhotoImage(file = f"img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 1275, y = 24,
    width = 39,
    height = 42)

img10 = PhotoImage(file = f"img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 1149, y = 16,
    width = 81,
    height = 50)

img11 = PhotoImage(file = f"img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b11.place(
    x = 1027, y = 19,
    width = 81,
    height = 47)

img12 = PhotoImage(file = f"img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b12.place(
    x = 870, y = 467,
    width = 20,
    height = 12)

img13 = PhotoImage(file = f"img13.png")
b13 = Button(
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b13.place(
    x = 844, y = 467,
    width = 19,
    height = 12)

img14 = PhotoImage(file = f"img14.png")
b14 = Button(
    image = img14,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b14.place(
    x = 815, y = 467,
    width = 20,
    height = 12)

img15 = PhotoImage(file = f"img15.png")
b15 = Button(
    image = img15,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b15.place(
    x = 510, y = 467,
    width = 20,
    height = 12)

img16 = PhotoImage(file = f"img16.png")
b16 = Button(
    image = img16,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b16.place(
    x = 484, y = 467,
    width = 19,
    height = 12)

img17 = PhotoImage(file = f"img17.png")
b17 = Button(
    image = img17,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b17.place(
    x = 455, y = 467,
    width = 20,
    height = 12)

img18 = PhotoImage(file = f"img18.png")
b18 = Button(
    image = img18,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b18.place(
    x = 510, y = 832,
    width = 20,
    height = 12)

img19 = PhotoImage(file = f"img19.png")
b19 = Button(
    image = img19,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b19.place(
    x = 484, y = 832,
    width = 19,
    height = 12)

img20 = PhotoImage(file = f"img20.png")
b20 = Button(
    image = img20,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b20.place(
    x = 455, y = 832,
    width = 20,
    height = 12)

img21 = PhotoImage(file = f"img21.png")
b21 = Button(
    image = img21,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b21.place(
    x = 1266, y = 467,
    width = 20,
    height = 12)

img22 = PhotoImage(file = f"img22.png")
b22 = Button(
    image = img22,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b22.place(
    x = 1240, y = 467,
    width = 19,
    height = 12)

img23 = PhotoImage(file = f"img23.png")
b23 = Button(
    image = img23,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b23.place(
    x = 1211, y = 467,
    width = 20,
    height = 12)

img24 = PhotoImage(file = f"img24.png")
b24 = Button(
    image = img24,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b24.place(
    x = 888, y = 834,
    width = 20,
    height = 12)

img25 = PhotoImage(file = f"img25.png")
b25 = Button(
    image = img25,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b25.place(
    x = 862, y = 834,
    width = 19,
    height = 12)

img26 = PhotoImage(file = f"img26.png")
b26 = Button(
    image = img26,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b26.place(
    x = 833, y = 834,
    width = 20,
    height = 12)

img27 = PhotoImage(file = f"img27.png")
b27 = Button(
    image = img27,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b27.place(
    x = 1266, y = 833,
    width = 20,
    height = 12)

img28 = PhotoImage(file = f"img28.png")
b28 = Button(
    image = img28,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b28.place(
    x = 1240, y = 833,
    width = 19,
    height = 12)

img29 = PhotoImage(file = f"img29.png")
b29 = Button(
    image = img29,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b29.place(
    x = 1211, y = 833,
    width = 20,
    height = 12)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    1132.5, 709.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#cf7c93",
    highlightthickness = 0)

entry0.place(
    x = 975, y = 596,
    width = 315,
    height = 224)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    754.5, 709.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#2da596",
    highlightthickness = 0)

entry1.place(
    x = 597, y = 596,
    width = 315,
    height = 224)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    376.5, 713.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#a9498d",
    highlightthickness = 0)

entry2.place(
    x = 219, y = 600,
    width = 315,
    height = 224)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    1132.5, 344.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#646da7",
    highlightthickness = 0)

entry3.place(
    x = 975, y = 229,
    width = 315,
    height = 228)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    754.5, 343.0,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#417e9a",
    highlightthickness = 0)

entry4.place(
    x = 597, y = 230,
    width = 315,
    height = 224)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    376.5, 342.0,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#826fa8",
    highlightthickness = 0)

entry5.place(
    x = 219, y = 229,
    width = 315,
    height = 224)

window.resizable(False, False)
window.mainloop()
