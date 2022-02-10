import tkinter as tk  # PEP 8 recommends avoiding `import *`.


def btn_clicked(x):
    """ Prints to console a message every time the button is clicked """
    print("Button Clicked - " + x)


dashboard = tk.Tk()
flash_delay = 100  # Milliseconds.

dashboard.geometry("1440x1024")
dashboard.configure(bg="#ffffff")
canvas = tk.Canvas(dashboard, bg="#343333", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

BGR_IMG_PATH = "dashboard_background.png"
background_img = tk.PhotoImage(file=BGR_IMG_PATH)
background = canvas.create_image(0, 0, anchor='nw', image=background_img)

# Retrieves the images, and configures the dashboard button
dashboard_image_path = "dashboard_dashboard.png"
dashboard_image = tk.PhotoImage(file=dashboard_image_path)
dashboard_image_obj = canvas.create_image(0, 120, anchor='nw', image=dashboard_image)
canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(dashboard_image_obj), btn_clicked("1")))

# Retrieves the images, and configures the simulated trading button
simulated_trading_image_path = "dashboard_simulated_trading.png"
simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
simulated_trading_image_obj = canvas.create_image(0, 230, anchor='nw', image=simulated_trading_image)
canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(simulated_trading_image_obj), btn_clicked("2")))

# Retrieves the images, and configures the charts button
charts_image_path = "dashboard_charts.png"
charts_image = tk.PhotoImage(file=charts_image_path)
charts_image_obj = canvas.create_image(0, 340, anchor='nw', image=charts_image)
canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(charts_image_obj), btn_clicked("3")))

# Retrieves the images, and configures the portfolio button
portfolio_image_path = "dashboard_portfolio.png"
portfolio_image = tk.PhotoImage(file=portfolio_image_path)
portfolio_image_obj = canvas.create_image(0, 450, anchor='nw', image=portfolio_image)
canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(portfolio_image_obj), btn_clicked("4")))

alarm_image_path = "dashboard_alarms.png"
alarm_image = tk.PhotoImage(file=alarm_image_path)
alarm_image_obj = canvas.create_image(0, 560, anchor='nw', image=alarm_image)
canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(alarm_image_obj), btn_clicked("5")))

# Retrieves the images, and configures the news button
news_image_path = "dashboard_news.png"
news_image = tk.PhotoImage(file=news_image_path)
news_image_obj = canvas.create_image(0, 670, anchor='nw', image=news_image)
canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(news_image_obj), btn_clicked("6")))

# Retrieves the images, and configures the settings button
settings_image_path = "dashboard_settings.png"
settings_image = tk.PhotoImage(file=settings_image_path)
settings_image_obj = canvas.create_image(0, 780, anchor='nw', image=settings_image)
canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(settings_image_obj), btn_clicked("7")))

# Retrieves the images, and configures the logout button
logout_image_path = "dashboard_logout.png"
logout_image = tk.PhotoImage(file=logout_image_path)
logout_image_obj = canvas.create_image(45, 950, anchor='nw', image=logout_image)
canvas.tag_bind(logout_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(logout_image_obj), btn_clicked("8")))

# Retrieves the images, and configures the notifications image
notifications_image_path = "dashboard_notifications.png"
notifications_image = tk.PhotoImage(file=notifications_image_path)
notifications_image_obj = canvas.create_image(1027, 19, anchor='nw', image=notifications_image)
canvas.tag_bind(notifications_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(notifications_image_obj), btn_clicked("9")))

# Retrieves the images, and configures the support image
support_image_path = "dashboard_support.png"
support_image = tk.PhotoImage(file=support_image_path)
support_image_obj = canvas.create_image(1155, 16, anchor='nw', image=support_image)
canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(support_image_obj), btn_clicked("10")))

# Retrieves the images, and configures the profile image
notes_image_path = "dashboard_notes.png"
notes_image = tk.PhotoImage(file=notes_image_path)
notes_image_obj = canvas.create_image(1268, 19, anchor='nw', image=notes_image)
canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(notes_image_obj), btn_clicked("11")))

# Retrieves the images, and configures the profile image
profile_image_path = "dashboard_profile_img.png"
profile_image = tk.PhotoImage(file=profile_image_path)
profile_image_obj = canvas.create_image(1360, 4, anchor='nw', image=profile_image)
canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                lambda event: (flash_hidden(profile_image_obj), btn_clicked("12")))

canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))


def flash_hidden(image_obj):
    set_state(tk.HIDDEN, image_obj)
    canvas.after(flash_delay, set_state, tk.NORMAL, image_obj)


def set_state(state, image_obj):
    canvas.itemconfigure(image_obj, state=state)





bgr_width, bgr_height = background_img.width(), background_img.height()

dashboard.title("TKinter button over transparent background")

dashboard.resizable(False, False)
dashboard.mainloop()
