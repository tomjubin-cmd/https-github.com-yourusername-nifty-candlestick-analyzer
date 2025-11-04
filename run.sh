#!/bin/bash

# Quick start script for nfscan

echo "🚀 Starting NIFTY Candlestick Analyzer..."

# Check if virtual environment exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the Streamlit app
streamlit run deploy/app.py
