"""
Utility functions for NIFTY Candlestick Analyzer
"""

import pandas as pd
from datetime import datetime, timedelta


def validate_dataframe(df):
    """
    Validate that the dataframe has required OHLC columns.
    
    Args:
        df (pd.DataFrame): The dataframe to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    required_columns = ['Open', 'High', 'Low', 'Close']
    return all(col in df.columns for col in required_columns)


def calculate_body_size(row):
    """
    Calculate the body size of a candlestick.
    
    Args:
        row (pd.Series): A row with OHLC data
        
    Returns:
        float: The absolute difference between open and close
    """
    return abs(row['Close'] - row['Open'])


def calculate_upper_shadow(row):
    """
    Calculate the upper shadow of a candlestick.
    
    Args:
        row (pd.Series): A row with OHLC data
        
    Returns:
        float: The upper shadow length
    """
    return row['High'] - max(row['Open'], row['Close'])


def calculate_lower_shadow(row):
    """
    Calculate the lower shadow of a candlestick.
    
    Args:
        row (pd.Series): A row with OHLC data
        
    Returns:
        float: The lower shadow length
    """
    return min(row['Open'], row['Close']) - row['Low']


def get_date_range(period):
    """
    Get start and end dates for a given period.
    
    Args:
        period (str): Period string (e.g., '1y', '6mo', '3mo')
        
    Returns:
        tuple: (start_date, end_date) as datetime objects
    """
    end_date = datetime.now()
    
    if period == '1y':
        start_date = end_date - timedelta(days=365)
    elif period == '6mo':
        start_date = end_date - timedelta(days=180)
    elif period == '3mo':
        start_date = end_date - timedelta(days=90)
    elif period == '1mo':
        start_date = end_date - timedelta(days=30)
    else:
        start_date = end_date - timedelta(days=365)
    
    return start_date, end_date


def format_currency(value):
    """
    Format a number as Indian currency.
    
    Args:
        value (float): The value to format
        
    Returns:
        str: Formatted currency string
    """
    return f"₹{value:,.2f}"
