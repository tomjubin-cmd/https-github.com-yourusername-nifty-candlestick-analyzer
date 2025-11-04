"""
NIFTY Candlestick Analyzer (nfscan)
A Python package for analyzing NIFTY stock market candlestick patterns.
"""

__version__ = "1.0.0"
__author__ = "NIFTY Candlestick Analyzer Team"

from .data_fetcher import DataFetcher
from .pattern_detector import PatternDetector
from .visualizer import Visualizer

__all__ = ["DataFetcher", "PatternDetector", "Visualizer"]
