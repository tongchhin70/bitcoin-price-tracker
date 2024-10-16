import requests
import tkinter as tk
from datetime import datetime

def TrackBitcoin():
    symbol = 'bitcoin'
    currency = 'usd'
    # Use an f-string to correctly format the URL
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={currency}'
    response = requests.get(url).json()
    price = response[symbol][currency]git init
    current_time = datetime.now().strftime('%H:%M:%S')
    labelPrice.config(text=str(price) + ' $')
    labelTime.config(text="Updated at: " + current_time)
    canvas.after(1000, TrackBitcoin)

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title('Bitcoin Price Tracker App')

f1 =  ('poopins', 24, 'bold')
f2 =  ('poopins', 22, 'bold')
f3 =  ('poopins', 18, 'normal')

label = tk.Label(canvas, text="Bitcoin Price", font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)

TrackBitcoin()

canvas.mainloop()