# Bitcoin Price Tracker

This Python project is a simple **Bitcoin Price Tracker** that uses the CoinGecko API to fetch the current price of Bitcoin in USD and display it using a Tkinter-based GUI (Graphical User Interface).

## Features
- **Fetch Real-Time Bitcoin Price**: The app pulls live Bitcoin price data in USD from the CoinGecko API.
- **Auto Update**: The price and the last updated time are displayed and can be manually refreshed.
- **Tkinter GUI**: The app uses Tkinter to display the Bitcoin price and update time in a clean, user-friendly interface.

## Prerequisites
Before running the application, make sure you have the following installed:
- Python 3.x
- The `requests` library for making HTTP requests
- Tkinter (comes pre-installed with Python)

### Install the `requests` module
If you do not have `requests` installed, you can install it via `pip`:

```bash
pip install requests
```

### Usage
To clone the repository and run the project locally:

```bash
git clone https://github.com/tongchhin70/bitcoin-price-tracker.git
cd bitcoin-price-tracker
```
## Run the Python Script
You can run the script using the following command:
``` bash
python bitcoin_price_tracker.py
```
# Code Explanation
## How it works
-** The app sends an HTTP GET request to the CoinGecko API to fetch the current Bitcoin price in USD.
-** The price and the last updated time are displayed on the Tkinter window.
-**  You can see the price of Bitcoin and the time when the last data was fetched.

# API
This app uses the CoinGecko API to fetch the current price of Bitcoin.
- `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd`
```
{
  "bitcoin": {
    "usd": 50000
  }
}
```
