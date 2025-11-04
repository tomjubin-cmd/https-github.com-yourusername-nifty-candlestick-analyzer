"""
Configuration settings for NIFTY Candlestick Analyzer
"""

# NIFTY symbols
NIFTY_SYMBOLS = [
    "NIFTY 50",
    "NIFTY BANK",
    "NIFTY IT",
    "NIFTY AUTO",
    "NIFTY PHARMA",
]

# Default symbol
DEFAULT_SYMBOL = "NIFTY 50"

# Data fetching settings
DEFAULT_PERIOD = "1y"  # 1 year
DEFAULT_INTERVAL = "1d"  # Daily

# Candlestick pattern thresholds
DOJI_THRESHOLD = 0.1
HAMMER_BODY_RATIO = 0.3
ENGULFING_MIN_BODY_RATIO = 0.6

# Visualization settings
CHART_WIDTH = 12
CHART_HEIGHT = 6
CHART_STYLE = "charles"

# API settings (if using external APIs)
API_BASE_URL = "https://api.example.com"
API_TIMEOUT = 30
