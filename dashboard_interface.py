from tkinter import *


class Dashboard:
    def __init__(self):
        window = Tk()

        # Configures dashboard window
        window.geometry("1440x1024")
        window.configure(bg="#ffffff")
        canvas = Canvas(window, bg="#ffffff", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # Sets background image
        background_img = PhotoImage(file=f"dashboard_background.png")
        background = canvas.create_image(718.0, 512.0, image=background_img)

        # Search Bar and Username Entries
        canvas.create_text(588.0, 40.5, text="Search Bar\n", fill="#abb0c8", font=("Rosarivo-Regular", int(12.0)))
        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        # Investing Portfolio
        canvas.create_text(430.0, 198.0, text="$34", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(430.0, 248.0, text="$33", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(411.0, 298.5, text="%32", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))

        #Top Earner #1
        canvas.create_text(640.0, 147.0, text = "$", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(640.0, 190.0, text = "$", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(690.0, 214.0, text = "%", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))

        # Top Earner #2
        canvas.create_text(865.0, 147.0, text = "$", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(865.0, 190.0, text = "$", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(920.0, 214.0, text = "%", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))

        # Top Earner #3
        canvas.create_text(1096.0, 149.0, text = "$", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0))) 
        canvas.create_text(1096.0, 192.0, text = "$", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1149.0, 214.0, text = "%", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))

        # Top Earner #4
        canvas.create_text(1322.0, 149.0, text = "$", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1322.0, 192.0, text = "$", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1373.0, 214.0, text = "%", fill = "#e5e5e5", font = ("Rosarivo-Regular", int(10.0)))

        # Closest to profit #1
        canvas.create_text(640.0, 295.0, text = "$", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(640.0, 338.0, text = "$", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(690.0, 356.0, text = "%", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))

        # Closest to profit #2
        canvas.create_text(865.0, 295.0, text = "$", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(865.0, 338.0, text = "$", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(920.0, 356.0, text = "%", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))

        # Closest to profit #3
        canvas.create_text(1096.0, 295.0, text = "$", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1096.0, 338.0, text = "$", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1149.0, 356.0, text = "%", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))

        # Closest to profit #4
        canvas.create_text(1322.0, 295.0, text = "$", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1322.0, 338.0, text = "$", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))
        canvas.create_text(1373.0, 356.0, text = "%", fill = "#ffffff", font = ("Rosarivo-Regular", int(10.0)))

        # Percent Increase Calculator
        canvas.create_text(968.0, 469.0, text="$7", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(968.0, 504.0, text="$6", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(968.0, 553.0, text="%5", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(972.0, 604.0, text="$4", fill="#ffffff", font=("Rosarivo-Regular", int(10.0)))
        canvas.create_text(975.0, 620.0, text="$0.00 is a 0% increase from $0.00", fill="#ffffff",
                           font=("Rosarivo-Regular", int(10.0)))

        # Retrieves the images, and configures the profile image
        dash_profile_img = PhotoImage(file=f"dashboard_profile_img.png")
        profile_button = Button(image=dash_profile_img, borderwidth=0, highlightthickness=0, relief="flat")
        profile_button.place(x=1360, y=4, width=68, height=57)

        # Retrieves the images, and configures the notes image
        dash_notes_img = PhotoImage(file=f"dashboard_notes.png")
        notes_button = Button(image=dash_notes_img, borderwidth=0, highlightthickness=0, relief="flat")
        notes_button.place(x=1275, y=24, width=39, height=42)

        # Retrieves the images, and configures the support image
        dash_support_img = PhotoImage(file=f"dashboard_support.png")
        support_button = Button(image=dash_support_img, borderwidth=0, highlightthickness=0, relief="flat")
        support_button.place(x=1149, y=16, width=81, height=50)

        # Retrieves the images, and configures the notifications image
        dash_notifications_img = PhotoImage(file=f"dashboard_notifications.png")
        notifications_button = Button(image=dash_notifications_img, borderwidth=0, highlightthickness=0, relief="flat")
        notifications_button.place(x=1027, y=19, width=81, height=47)

        # Retrieves the images, and configures the logout image
        dash_logout_img = PhotoImage(file=f"dashboard_logout.png")
        logout_button = Button(image=dash_logout_img, borderwidth=0, highlightthickness=0, relief="flat")
        logout_button.place(x=45, y=937, width=30, height=30)

        # Retrieves the images, and dash the logout image
        dash_settings_img = PhotoImage(file=f"dashboard_settings.png")
        settings_button = Button(image=dash_settings_img, borderwidth=0, highlightthickness=0, relief="flat")
        settings_button.place(x=14, y=789, width=90, height=90)

        # Retrieves the images, and configures the news image
        dash_news_img = PhotoImage(file=f"dashboard_news.png")
        news_button = Button(image=dash_news_img, borderwidth=0, highlightthickness=0, relief="flat")
        news_button.place(x=14, y=680, width=90, height=90)

        # Retrieves the images, and configures the alarms image
        dash_alarms_img = PhotoImage(file=f"dashboard_alarms.png")
        alarms_button = Button(image=dash_alarms_img, borderwidth=0, highlightthickness=0, relief="flat")
        alarms_button.place(x=14, y=571, width=90, height=90)

        # Retrieves the images, and configures the portfolio image
        dash_portfolio_img = PhotoImage(file=f"dashboard_portfolio.png")
        portfolio_button = Button(image=dash_portfolio_img, borderwidth=0, highlightthickness=0, relief="flat")
        portfolio_button.place(x=14, y=462, width=90, height=90)

        # Retrieves the images, and configures the charts image
        dash_charts_img = PhotoImage(file=f"dashboard_charts.png")
        charts_button = Button(image=dash_charts_img, borderwidth=0, highlightthickness=0, relief="flat")
        charts_button.place(x=13, y=353, width=90, height=90)

        # Retrieves the images, and configures the simulated trading image
        dash_simulated_img = PhotoImage(file=f"dashboard_simulated_trading.png")
        simulated_button = Button(image=dash_simulated_img, borderwidth=0, highlightthickness=0, relief="flat")
        simulated_button.place(x=15, y=244, width=90, height=90)

        # Retrieves the images, and configures the dashboard image
        dash_image = PhotoImage(file=f"dashboard_dashboard.png")
        dash_button = Button(image=dash_image, borderwidth=0, highlightthickness=0, relief="flat")
        dash_button.place(x=15, y=135, width=90, height=90)

        window.resizable(False, False)
        window.mainloop()


def main():
    Dashboard_Root = Dashboard()


if __name__ == '__main__':
    main()
