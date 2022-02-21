from typing import Any

import tkinter as tk
from tkinter import *

class Portfolio(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width=1440, height=1024)
        self.controller = controller

        flash_delay = 100  # in milliseconds.

        canvas = tk.Canvas(self, bg="#343333", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # Retrieves the images, and configures the dashboard button
        self.background_img = tk.PhotoImage(file=f"portfolio_background.png")
        canvas.create_image(722.0, 512.0, image=self.background_img)

        # Retrieves the images, and configures the dashboard button
        dashboard_image_path = "dashboard_dashboard.png"
        self.dashboard_image = tk.PhotoImage(file=dashboard_image_path)
        dashboard_image_obj = canvas.create_image(0, 120, anchor='nw', image=self.dashboard_image)
        canvas.tag_bind(dashboard_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(dashboard_image_obj), controller.show_canvas(Portfolio)))

        # Retrieves the images, and configures the simulated trading button
        simulated_trading_image_path = "dashboard_simulated_trading.png"
        self.simulated_trading_image = tk.PhotoImage(file=simulated_trading_image_path)
        simulated_trading_image_obj = canvas.create_image(0, 230, anchor='nw', image=self.simulated_trading_image)
        canvas.tag_bind(simulated_trading_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(simulated_trading_image_obj), controller.show_canvas(Portfolio)))

        # Retrieves the images, and configures the charts button
        charts_image_path = "dashboard_charts.png"
        self.charts_image = tk.PhotoImage(file=charts_image_path)
        charts_image_obj = canvas.create_image(0, 340, anchor='nw', image=self.charts_image)
        canvas.tag_bind(charts_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(charts_image_obj), controller.show_canvas(Portfolio)))

        # Retrieves the images, and configures the portfolio button
        portfolio_image_path = "dashboard_portfolio.png"
        self.portfolio_image = tk.PhotoImage(file=portfolio_image_path)
        portfolio_image_obj = canvas.create_image(0, 450, anchor='nw', image=self.portfolio_image)
        canvas.tag_bind(portfolio_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(portfolio_image_obj), controller.show_canvas(Portfolio)))

        alarm_image_path = "dashboard_alarms.png"
        self.alarm_image = tk.PhotoImage(file=alarm_image_path)
        alarm_image_obj = canvas.create_image(0, 560, anchor='nw', image=self.alarm_image)
        canvas.tag_bind(alarm_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(alarm_image_obj), controller.show_canvas(Portfolio)))

        # Retrieves the images, and configures the news button
        news_image_path = "dashboard_news.png"
        self.news_image = tk.PhotoImage(file=news_image_path)
        news_image_obj = canvas.create_image(0, 670, anchor='nw', image=self.news_image)
        canvas.tag_bind(news_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(news_image_obj), controller.show_canvas(Portfolio)))

        # Retrieves the images, and configures the settings button
        settings_image_path = "dashboard_settings.png"
        self.settings_image = tk.PhotoImage(file=settings_image_path)
        settings_image_obj = canvas.create_image(0, 780, anchor='nw', image=self.settings_image)
        canvas.tag_bind(settings_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(settings_image_obj), controller.show_canvas(Portfolio)))

        # Retrieves the images, and configures the notifications image
        notifications_image_path = "dashboard_notifications.png"
        self.notifications_image = tk.PhotoImage(file=notifications_image_path)
        notifications_image_obj = canvas.create_image(1027, 19, anchor='nw', image=self.notifications_image)
        canvas.tag_bind(notifications_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notifications_image_obj), controller.show_canvas(Portfolio)))

        # Retrieves the images, and configures the support image
        support_image_path = "dashboard_support.png"
        self.support_image = tk.PhotoImage(file=support_image_path)
        support_image_obj = canvas.create_image(1155, 16, anchor='nw', image=self.support_image)
        canvas.tag_bind(support_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(support_image_obj), controller.show_canvas(Portfolio)))

        # Retrieves the images, and configures the profile image
        notes_image_path = "dashboard_notes.png"
        self.notes_image = tk.PhotoImage(file=notes_image_path)
        notes_image_obj = canvas.create_image(1268, 19, anchor='nw', image=self.notes_image)
        canvas.tag_bind(notes_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(notes_image_obj), controller.show_canvas(Portfolio)))

        # Retrieves the images, and configures the profile image
        profile_image_path = "dashboard_profile_img.png"
        self.profile_image = tk.PhotoImage(file=profile_image_path)
        profile_image_obj = canvas.create_image(1360, 4, anchor='nw', image=self.profile_image)
        canvas.tag_bind(profile_image_obj, "<ButtonRelease-1>",
                        lambda event: (flash_hidden(profile_image_obj), controller.show_canvas(Portfolio)))
        
        # Retrieves the images, and configures the left arrow image
        # portfolio_leftArrow_image_path = "portfolio_leftArrow.png"
        # self.portfolio_leftArrow_image = tk.PhotoImage(file = portfolio_leftArrow_image_path)
        # portfolio_image_obj = canvas.create_image(1236, 950, anchor='nw', image=self.portfolio_leftArrow_image)
        # canvas.tag_bind()

        canvas.create_text(1398.5, 68.5, text="John Doe", fill="#ffffff", font=("Rosarivo-Regular", int(12.0)))

        def flash_hidden(image_obj):
            """
            Method sets the state of the object, and hides the buttons when they are interacted with

            :param image_obj: is the image object to hide
            :type : int
            :return: a hidden button when pressed
            """
            set_state(tk.HIDDEN, image_obj)
            canvas.after(flash_delay, set_state, tk.NORMAL, image_obj)

        def set_state(state, image_obj):
            """
            Sets the state of the image object

            :param state: the state to apply to the buttons
            :param image_obj: is the image object to apply a state on
            :return: an image object with a state applied
            """
            canvas.itemconfigure(image_obj, state=state)

        self.settings_image.width(), self.settings_image.height()
        
        canvas.create_text( 274.0, 100.5, text = "$", fill = "#ffffff", font = ("Rosarivo-Regular", int(18.0)))
        
        # Table data
        # Row 1
        canvas.create_text( 303.0, 419.0, text = "Assets 1", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 538.0, 420.0, text = "Balance 1", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 948.0, 421.0, text = "Percent Change  1", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 729.0, 420.0, text = "Currency Price 1", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        
        # Row 2
        canvas.create_text( 303.0, 491.0, text = "Assets 2", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 538.0, 492.0, text = "Balance 2", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 729.0, 492.0, text = "Currency Price 2", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 948.0, 493.0, text = "Percent Change  2", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        
        # Row 3
        canvas.create_text( 303.0, 560.0, text = "Assets 3", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 538.0, 561.0, text = "Balance 3", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 729.0, 561.0, text = "Currency Price 3", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 948.0, 562.0, text = "Percent Change  3", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        
        #Row 4
        canvas.create_text( 303.0, 630.0, text = "Assets 4", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 538.0, 631.0, text = "Balance 4", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 729.0, 631.0, text = "Currency Price 4", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 948.0, 632.0, text = "Percent Change  4", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        
        # Row 5
        canvas.create_text( 303.0, 697.0, text = "Assets 5", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 538.0, 698.0, text = "Balance 5", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 729.0, 698.0, text = "Currency Price 5", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 948.0, 699.0,text = "Percent Change  5", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        
        # Row 6
        canvas.create_text( 303.0, 767.0, text = "Assets 6", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 538.0, 768.0, text = "Balance 6", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text(  729.0, 768.0, text = "Currency Price 6", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 948.0, 769.0, text = "Percent Change  6", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        
        # Row 7
        canvas.create_text( 303.0, 836.0, text = "Assets 7", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 538.0, 837.0, text = "Balance 7", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 729.0, 837.0, text = "Currency Price 7",fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 948.0, 838.0, text = "Percent Change  7", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        
        # Row 8
        canvas.create_text( 303.0, 905.0, text = "Assets 8", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 538.0, 906.0, text = "Balance 8", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 729.0, 906.0, text = "Currency Price 8", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        canvas.create_text( 948.0, 907.0, text = "Percent Change  8", fill = "#ffffff", font = ("Rosarivo-Regular", int(13.0)))
        