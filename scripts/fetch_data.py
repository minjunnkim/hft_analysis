from alpha_vantage.timeseries import TimeSeries
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_and_save_data(symbols, interval='1min', outputsize='full'):
    api_key = os.getenv('ALPHAVANTAGE_API_KEY') 
    ts = TimeSeries(key=api_key, output_format='pandas')
    
    if not os.path.exists('data'):
        os.makedirs('data')
    
    for symbol in symbols:
        data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize=outputsize)
        data.to_csv(f'data/{symbol}_intraday.csv')

# List of symbols for different companies
symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA']  
fetch_and_save_data(symbols)

