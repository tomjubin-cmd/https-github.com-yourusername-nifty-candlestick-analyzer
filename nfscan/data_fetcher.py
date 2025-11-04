"""
Data fetcher module for retrieving NIFTY stock data
"""

import pandas as pd
import yfinance as yf
from datetime import datetime
from .config import DEFAULT_PERIOD, DEFAULT_INTERVAL
from .utils import validate_dataframe


class DataFetcher:
    """
    Class for fetching NIFTY stock market data.
    """
    
    def __init__(self, symbol="^NSEI"):
        """
        Initialize the DataFetcher.
        
        Args:
            symbol (str): The stock symbol to fetch (default: ^NSEI for NIFTY 50)
        """
        self.symbol = symbol
        self.data = None
    
    def fetch_data(self, period=DEFAULT_PERIOD, interval=DEFAULT_INTERVAL):
        """
        Fetch historical data for the symbol.
        
        Args:
            period (str): Period for which to fetch data (e.g., '1y', '6mo')
            interval (str): Data interval (e.g., '1d', '1h')
            
        Returns:
            pd.DataFrame: DataFrame with OHLC data
        """
        try:
            ticker = yf.Ticker(self.symbol)
            self.data = ticker.history(period=period, interval=interval)
            
            if self.data.empty:
                raise ValueError(f"No data fetched for symbol {self.symbol}")
            
            # Validate the dataframe
            if not validate_dataframe(self.data):
                raise ValueError("Fetched data does not contain required OHLC columns")
            
            return self.data
        
        except Exception as e:
            raise Exception(f"Error fetching data: {str(e)}")
    
    def fetch_data_range(self, start_date, end_date, interval=DEFAULT_INTERVAL):
        """
        Fetch historical data for a specific date range.
        
        Args:
            start_date (str or datetime): Start date
            end_date (str or datetime): End date
            interval (str): Data interval (e.g., '1d', '1h')
            
        Returns:
            pd.DataFrame: DataFrame with OHLC data
        """
        try:
            ticker = yf.Ticker(self.symbol)
            self.data = ticker.history(start=start_date, end=end_date, interval=interval)
            
            if self.data.empty:
                raise ValueError(f"No data fetched for symbol {self.symbol}")
            
            return self.data
        
        except Exception as e:
            raise Exception(f"Error fetching data: {str(e)}")
    
    def get_latest_price(self):
        """
        Get the latest closing price.
        
        Returns:
            float: Latest closing price
        """
        if self.data is None or self.data.empty:
            self.fetch_data(period="1d")
        
        return self.data['Close'].iloc[-1]
    
    def save_data(self, filename):
        """
        Save fetched data to a CSV file.
        
        Args:
            filename (str): Path to save the CSV file
        """
        if self.data is None or self.data.empty:
            raise ValueError("No data to save. Fetch data first.")
        
        self.data.to_csv(filename)
    
    def load_data(self, filename):
        """
        Load data from a CSV file.
        
        Args:
            filename (str): Path to the CSV file
            
        Returns:
            pd.DataFrame: Loaded DataFrame
        """
        self.data = pd.read_csv(filename, index_col=0, parse_dates=True)
        return self.data
