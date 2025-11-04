"""
Candlestick pattern detection module
"""

import pandas as pd
from .utils import calculate_body_size, calculate_upper_shadow, calculate_lower_shadow
from .config import DOJI_THRESHOLD, HAMMER_BODY_RATIO, ENGULFING_MIN_BODY_RATIO


class PatternDetector:
    """
    Class for detecting candlestick patterns in stock data.
    """
    
    def __init__(self, data):
        """
        Initialize the PatternDetector.
        
        Args:
            data (pd.DataFrame): DataFrame with OHLC data
        """
        self.data = data.copy()
        self.patterns = {}
    
    def detect_doji(self):
        """
        Detect Doji patterns (open and close are nearly equal).
        
        Returns:
            pd.Series: Boolean series indicating Doji patterns
        """
        body_size = self.data.apply(calculate_body_size, axis=1)
        candle_range = self.data['High'] - self.data['Low']
        
        # Doji: body size is very small relative to the range
        doji = (body_size / candle_range) < DOJI_THRESHOLD
        
        self.patterns['Doji'] = doji
        return doji
    
    def detect_hammer(self):
        """
        Detect Hammer patterns (small body, long lower shadow, small upper shadow).
        
        Returns:
            pd.Series: Boolean series indicating Hammer patterns
        """
        body_size = self.data.apply(calculate_body_size, axis=1)
        lower_shadow = self.data.apply(calculate_lower_shadow, axis=1)
        upper_shadow = self.data.apply(calculate_upper_shadow, axis=1)
        candle_range = self.data['High'] - self.data['Low']
        
        # Hammer: small body, long lower shadow
        hammer = (
            (body_size / candle_range < HAMMER_BODY_RATIO) &
            (lower_shadow > 2 * body_size) &
            (upper_shadow < body_size)
        )
        
        self.patterns['Hammer'] = hammer
        return hammer
    
    def detect_inverted_hammer(self):
        """
        Detect Inverted Hammer patterns (small body, long upper shadow, small lower shadow).
        
        Returns:
            pd.Series: Boolean series indicating Inverted Hammer patterns
        """
        body_size = self.data.apply(calculate_body_size, axis=1)
        lower_shadow = self.data.apply(calculate_lower_shadow, axis=1)
        upper_shadow = self.data.apply(calculate_upper_shadow, axis=1)
        candle_range = self.data['High'] - self.data['Low']
        
        # Inverted Hammer: small body, long upper shadow
        inverted_hammer = (
            (body_size / candle_range < HAMMER_BODY_RATIO) &
            (upper_shadow > 2 * body_size) &
            (lower_shadow < body_size)
        )
        
        self.patterns['Inverted Hammer'] = inverted_hammer
        return inverted_hammer
    
    def detect_bullish_engulfing(self):
        """
        Detect Bullish Engulfing patterns.
        
        Returns:
            pd.Series: Boolean series indicating Bullish Engulfing patterns
        """
        result = pd.Series([False] * len(self.data), index=self.data.index)
        
        for i in range(1, len(self.data)):
            prev = self.data.iloc[i-1]
            curr = self.data.iloc[i]
            
            # Previous candle is bearish (close < open)
            prev_bearish = prev['Close'] < prev['Open']
            
            # Current candle is bullish (close > open)
            curr_bullish = curr['Close'] > curr['Open']
            
            # Current body engulfs previous body
            engulfs = (
                curr['Open'] <= prev['Close'] and
                curr['Close'] >= prev['Open']
            )
            
            result.iloc[i] = prev_bearish and curr_bullish and engulfs
        
        self.patterns['Bullish Engulfing'] = result
        return result
    
    def detect_bearish_engulfing(self):
        """
        Detect Bearish Engulfing patterns.
        
        Returns:
            pd.Series: Boolean series indicating Bearish Engulfing patterns
        """
        result = pd.Series([False] * len(self.data), index=self.data.index)
        
        for i in range(1, len(self.data)):
            prev = self.data.iloc[i-1]
            curr = self.data.iloc[i]
            
            # Previous candle is bullish (close > open)
            prev_bullish = prev['Close'] > prev['Open']
            
            # Current candle is bearish (close < open)
            curr_bearish = curr['Close'] < curr['Open']
            
            # Current body engulfs previous body
            engulfs = (
                curr['Open'] >= prev['Close'] and
                curr['Close'] <= prev['Open']
            )
            
            result.iloc[i] = prev_bullish and curr_bearish and engulfs
        
        self.patterns['Bearish Engulfing'] = result
        return result
    
    def detect_morning_star(self):
        """
        Detect Morning Star patterns (three-candle bullish reversal).
        
        Returns:
            pd.Series: Boolean series indicating Morning Star patterns
        """
        result = pd.Series([False] * len(self.data), index=self.data.index)
        
        for i in range(2, len(self.data)):
            first = self.data.iloc[i-2]
            second = self.data.iloc[i-1]
            third = self.data.iloc[i]
            
            # First candle is bearish with large body
            first_bearish = first['Close'] < first['Open']
            
            # Second candle has small body (star)
            second_body = calculate_body_size(second)
            second_small = second_body < calculate_body_size(first) * 0.3
            
            # Third candle is bullish with large body
            third_bullish = third['Close'] > third['Open']
            
            # Third candle closes above midpoint of first candle
            first_midpoint = (first['Open'] + first['Close']) / 2
            closes_above = third['Close'] > first_midpoint
            
            result.iloc[i] = first_bearish and second_small and third_bullish and closes_above
        
        self.patterns['Morning Star'] = result
        return result
    
    def detect_evening_star(self):
        """
        Detect Evening Star patterns (three-candle bearish reversal).
        
        Returns:
            pd.Series: Boolean series indicating Evening Star patterns
        """
        result = pd.Series([False] * len(self.data), index=self.data.index)
        
        for i in range(2, len(self.data)):
            first = self.data.iloc[i-2]
            second = self.data.iloc[i-1]
            third = self.data.iloc[i]
            
            # First candle is bullish with large body
            first_bullish = first['Close'] > first['Open']
            
            # Second candle has small body (star)
            second_body = calculate_body_size(second)
            second_small = second_body < calculate_body_size(first) * 0.3
            
            # Third candle is bearish with large body
            third_bearish = third['Close'] < third['Open']
            
            # Third candle closes below midpoint of first candle
            first_midpoint = (first['Open'] + first['Close']) / 2
            closes_below = third['Close'] < first_midpoint
            
            result.iloc[i] = first_bullish and second_small and third_bearish and closes_below
        
        self.patterns['Evening Star'] = result
        return result
    
    def detect_all_patterns(self):
        """
        Detect all implemented candlestick patterns.
        
        Returns:
            dict: Dictionary with pattern names as keys and detection results as values
        """
        self.detect_doji()
        self.detect_hammer()
        self.detect_inverted_hammer()
        self.detect_bullish_engulfing()
        self.detect_bearish_engulfing()
        self.detect_morning_star()
        self.detect_evening_star()
        
        return self.patterns
    
    def get_pattern_summary(self):
        """
        Get a summary of detected patterns.
        
        Returns:
            pd.DataFrame: Summary with pattern counts
        """
        if not self.patterns:
            self.detect_all_patterns()
        
        summary = []
        for pattern_name, pattern_series in self.patterns.items():
            count = pattern_series.sum()
            summary.append({
                'Pattern': pattern_name,
                'Count': count,
                'Percentage': f"{(count / len(self.data) * 100):.2f}%"
            })
        
        return pd.DataFrame(summary)
    
    def get_pattern_dates(self, pattern_name):
        """
        Get dates where a specific pattern occurred.
        
        Args:
            pattern_name (str): Name of the pattern
            
        Returns:
            pd.DatetimeIndex: Dates where the pattern occurred
        """
        if pattern_name not in self.patterns:
            raise ValueError(f"Pattern '{pattern_name}' not found. Run detection first.")
        
        return self.data[self.patterns[pattern_name]].index
