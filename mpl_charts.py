from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import matplotlib.patches as mp
from matplotlib.ticker import FormatStrFormatter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplfinance as fplt
import numpy as np

import tkinter as tk
from tkinter import *

from gecko_api import GeckoApi

class MplCharts:
    
    def __init__(self, canvas : tk.Canvas):
        
        self.canvas = canvas
        
        
    def portfolio_hist(self, port_hist : dict):
       
        dates = []
        totals = []
        for date, total in port_hist.items():
            dates.append(date)
            totals.append(total)  
        
        pixels = 1/plt.rcParams['figure.dpi']
        figure = Figure(figsize=(623*pixels, 304*pixels))
        ax = figure.add_subplot(111) 
        
        line, = ax.plot(dates, totals)
        ax.set_xlabel("Date")
        ax.set_ylabel("Total Value")
        
        ax.set_ylim([min(totals) * 0.85, max(totals) * 1.1])
        
        line_canvas = FigureCanvasTkAgg(figure, master=self.canvas)
        line_canvas.draw()
        line_canvas.get_tk_widget().place(x=135, y=672)
        
    def pie_chart(self, portfolio : dict):

        coins = []
        amounts = []
        for coin, amount in portfolio.items():
            coins.append(coin)
            amounts.append(amount)                        
        
        pixels = 1/plt.rcParams['figure.dpi']
        figure = Figure(figsize=(469*pixels,250*pixels))
        ax = figure.add_subplot(111)
        
        ax.pie(amounts)
        ax.legend(coins)
        ax.plot()
        
        circle = mp.Circle((0,0), 0.7, color="white")
        ax.add_artist(circle)
        
        pie_canvas = FigureCanvasTkAgg(figure, master=self.canvas)
        pie_canvas.draw()
        pie_canvas.get_tk_widget().place(x=151, y=390)
        
    def candlestick(self, coin_name : str, days_previous : int):
        
        coin = GeckoApi(coin_name)
        ohlc_data = coin.get_ohlc_data(days_previous)
        pixels = 1/plt.rcParams['figure.dpi']
        
        # x-axis (date) format
        if days_previous == 1:
            dt_format = '%b %d, %H:%M'
        else:
            dt_format = '%b %d'

        # y-axis (price) format
        if ohlc_data["high"][0] > 0.01:
            y_format = '$%.2f'
        else: 
            y_format = '$%.3g'

        if type(ohlc_data) != list:
            
            colors = fplt.make_marketcolors(
                up='tab:blue', down='tab:red',
                edge='lime',
                # wick='inherit', # use up/down colors
                wick={'up':'purple', 'down':'orange'}, 
                # alpha=0.5, # alpha for candlestick face
            )
            
            s = fplt.make_mpf_style(base_mpl_style="seaborn", marketcolors=colors, mavcolors=["red", "orange"])
            
            fig, axlist = fplt.plot(
                ohlc_data,
                type = 'candle',
                xrotation=0,
                
                    # pick a style!
                # style = 'blueskies',
                # style = 'brasil',
                # style = 'charles',
                # style = 'checkers',
                # style = 'default',
                # style = 'mike',
                # style = 'nightclouds',
                # style = 'sas',
                # style = 'starsandstripes',
                style = 'yahoo',
                    # or use custom style
                # style = s, 
                
                datetime_format=dt_format,
                
                # title = coin_name,
                ylabel = "",
                
                # include moving average
                # mav = (2,4),
                
                    # set size
                # figratio=(15, 10),
                # figscale=1.5,
                figsize=(1293*pixels, 609*pixels),

                    # if we include volume data in ohlc,
                    # we can add volume chart underneath
                # volume=True,
                # ylabel_lower="Shares\nTraded",
                
                show_nontrading=True,
                
                # tight_layout=True,
                scale_padding={'left': 0.1, 'top': 0.1, 'right': 0.7, 'bottom': 0.3},
                
                closefig=True,
                returnfig=True
            )
            
            axlist[0].yaxis.set_major_formatter(FormatStrFormatter(y_format)) 
        
            self.close()
            
            self.canvas = FigureCanvasTkAgg(fig)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x=135, y=397)
        
        else: 
            
            print("no data found!")
           
        return ohlc_data
        
    def charts_data(self, coin_name : str):
        
        coin = GeckoApi(coin_name)
        data = coin.get_coin()
        attributes = ["name", "current_price", "market_cap", "fully_diluted_valuation", 
                      "total_volume", "high_24h", "low_24h", "price_change_percentage_24h", 
                      "circulating_supply", "ath", "atl"]
        
        new_data = {key: value for key, value in data.items() if key in attributes}
        return new_data
        
    def close(self):
        try: 
            self.canvas.get_tk_widget().destroy()
        except:
            pass
        
# def main():
    
#     root = tk.Tk()
#     root.geometry("1500x800")
    
#     c = MplCharts(root)
#     c.candlestick("khalifa finance", 14)
    
#     root.mainloop()
    
#     # coin = GeckoApi("bitcoin")
#     # ohlc = coin.get_ohlc_data(14)
#     # print(ohlc["high"][0])


# if __name__ == '__main__':
#     main()
