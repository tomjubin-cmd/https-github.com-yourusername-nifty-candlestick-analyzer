"""
Visualization module for candlestick charts and patterns
"""

import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
from .config import CHART_WIDTH, CHART_HEIGHT, CHART_STYLE


class Visualizer:
    """
    Class for visualizing candlestick data and patterns.
    """
    
    def __init__(self, data):
        """
        Initialize the Visualizer.
        
        Args:
            data (pd.DataFrame): DataFrame with OHLC data
        """
        self.data = data.copy()
    
    def plot_candlestick(self, title="Candlestick Chart", style=CHART_STYLE, volume=True):
        """
        Plot a candlestick chart.
        
        Args:
            title (str): Chart title
            style (str): Chart style
            volume (bool): Whether to show volume
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        kwargs = {
            'type': 'candle',
            'style': style,
            'title': title,
            'volume': volume,
            'figsize': (CHART_WIDTH, CHART_HEIGHT),
        }
        
        fig, axes = mpf.plot(self.data, **kwargs, returnfig=True)
        return fig
    
    def plot_with_patterns(self, patterns, title="Candlestick Chart with Patterns"):
        """
        Plot candlestick chart with pattern markers.
        
        Args:
            patterns (dict): Dictionary of pattern names and detection results
            title (str): Chart title
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        # Prepare marker data
        markers = []
        
        for pattern_name, pattern_series in patterns.items():
            if pattern_series.sum() > 0:
                # Create markers for this pattern
                marker_data = pd.Series(index=self.data.index, dtype=float)
                
                # Set marker positions at the low of detected patterns
                for idx in self.data[pattern_series].index:
                    marker_data.loc[idx] = self.data.loc[idx, 'Low'] * 0.98
                
                markers.append(
                    mpf.make_addplot(marker_data, type='scatter', markersize=100, 
                                   marker='^', color='green' if 'Bullish' in pattern_name or 'Hammer' in pattern_name or 'Morning' in pattern_name else 'red')
                )
        
        kwargs = {
            'type': 'candle',
            'style': CHART_STYLE,
            'title': title,
            'volume': True,
            'figsize': (CHART_WIDTH, CHART_HEIGHT),
        }
        
        if markers:
            kwargs['addplot'] = markers
        
        fig, axes = mpf.plot(self.data, **kwargs, returnfig=True)
        return fig
    
    def plot_price_movement(self, title="Price Movement"):
        """
        Plot closing price movement over time.
        
        Args:
            title (str): Chart title
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        fig, ax = plt.subplots(figsize=(CHART_WIDTH, CHART_HEIGHT))
        
        ax.plot(self.data.index, self.data['Close'], label='Close Price', linewidth=2)
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.set_title(title)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    def plot_volume(self, title="Trading Volume"):
        """
        Plot trading volume over time.
        
        Args:
            title (str): Chart title
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        if 'Volume' not in self.data.columns:
            raise ValueError("Volume data not available")
        
        fig, ax = plt.subplots(figsize=(CHART_WIDTH, CHART_HEIGHT))
        
        ax.bar(self.data.index, self.data['Volume'], label='Volume', alpha=0.7)
        ax.set_xlabel('Date')
        ax.set_ylabel('Volume')
        ax.set_title(title)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    def plot_pattern_distribution(self, pattern_summary, title="Pattern Distribution"):
        """
        Plot a bar chart of pattern distribution.
        
        Args:
            pattern_summary (pd.DataFrame): Pattern summary dataframe
            title (str): Chart title
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        fig, ax = plt.subplots(figsize=(CHART_WIDTH, CHART_HEIGHT))
        
        ax.bar(pattern_summary['Pattern'], pattern_summary['Count'], alpha=0.7)
        ax.set_xlabel('Pattern')
        ax.set_ylabel('Count')
        ax.set_title(title)
        ax.grid(True, alpha=0.3, axis='y')
        plt.xticks(rotation=45, ha='right')
        
        plt.tight_layout()
        return fig
    
    def save_figure(self, fig, filename):
        """
        Save a figure to a file.
        
        Args:
            fig (matplotlib.figure.Figure): The figure to save
            filename (str): Output filename
        """
        fig.savefig(filename, dpi=300, bbox_inches='tight')
    
    def show_figure(self, fig):
        """
        Display a figure.
        
        Args:
            fig (matplotlib.figure.Figure): The figure to display
        """
        plt.show()
