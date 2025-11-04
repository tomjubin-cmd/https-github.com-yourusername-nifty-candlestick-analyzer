"""
Streamlit web application for NIFTY Candlestick Analyzer
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import sys
import os

# Add parent directory to path to import nfscan
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nfscan import DataFetcher, PatternDetector, Visualizer
from nfscan.config import NIFTY_SYMBOLS


def main():
    """Main application function"""
    
    st.set_page_config(
        page_title="NIFTY Candlestick Analyzer",
        page_icon="📈",
        layout="wide"
    )
    
    st.title("📈 NIFTY Candlestick Analyzer (nfscan)")
    st.markdown("Analyze NIFTY stock market candlestick patterns")
    
    # Sidebar configuration
    st.sidebar.header("Configuration")
    
    # Symbol selection
    symbol_map = {
        "NIFTY 50": "^NSEI",
        "NIFTY BANK": "^NSEBANK",
        "NIFTY IT": "^CNXIT",
        "NIFTY AUTO": "^CNXAUTO",
        "NIFTY PHARMA": "NIFTYPHARMA.NS",
    }
    
    selected_symbol_name = st.sidebar.selectbox(
        "Select Index",
        list(symbol_map.keys())
    )
    symbol = symbol_map[selected_symbol_name]
    
    # Period selection
    period = st.sidebar.selectbox(
        "Select Period",
        ["1mo", "3mo", "6mo", "1y", "2y", "5y"],
        index=3  # Default to 1y
    )
    
    # Interval selection
    interval = st.sidebar.selectbox(
        "Select Interval",
        ["1d", "1wk", "1mo"],
        index=0  # Default to 1d
    )
    
    if st.sidebar.button("Analyze", type="primary"):
        with st.spinner("Fetching data..."):
            try:
                # Fetch data
                fetcher = DataFetcher(symbol)
                data = fetcher.fetch_data(period=period, interval=interval)
                
                st.success(f"Successfully fetched {len(data)} data points")
                
                # Display basic statistics
                st.header("📊 Market Overview")
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Latest Close", f"₹{data['Close'].iloc[-1]:.2f}")
                
                with col2:
                    change = data['Close'].iloc[-1] - data['Close'].iloc[-2]
                    change_pct = (change / data['Close'].iloc[-2]) * 100
                    st.metric("Daily Change", f"₹{change:.2f}", f"{change_pct:.2f}%")
                
                with col3:
                    st.metric("Period High", f"₹{data['High'].max():.2f}")
                
                with col4:
                    st.metric("Period Low", f"₹{data['Low'].min():.2f}")
                
                # Detect patterns
                st.header("🔍 Pattern Detection")
                with st.spinner("Detecting patterns..."):
                    detector = PatternDetector(data)
                    patterns = detector.detect_all_patterns()
                    pattern_summary = detector.get_pattern_summary()
                
                # Display pattern summary
                st.subheader("Pattern Summary")
                st.dataframe(pattern_summary, use_container_width=True)
                
                # Visualizations
                st.header("📈 Charts")
                
                tab1, tab2, tab3, tab4 = st.tabs([
                    "Candlestick Chart",
                    "Patterns Chart",
                    "Price Movement",
                    "Pattern Distribution"
                ])
                
                visualizer = Visualizer(data)
                
                with tab1:
                    st.subheader("Candlestick Chart")
                    fig = visualizer.plot_candlestick(
                        title=f"{selected_symbol_name} Candlestick Chart"
                    )
                    st.pyplot(fig)
                
                with tab2:
                    st.subheader("Candlestick Chart with Detected Patterns")
                    fig = visualizer.plot_with_patterns(
                        patterns,
                        title=f"{selected_symbol_name} with Patterns"
                    )
                    st.pyplot(fig)
                
                with tab3:
                    st.subheader("Price Movement")
                    fig = visualizer.plot_price_movement(
                        title=f"{selected_symbol_name} Price Movement"
                    )
                    st.pyplot(fig)
                
                with tab4:
                    st.subheader("Pattern Distribution")
                    fig = visualizer.plot_pattern_distribution(
                        pattern_summary,
                        title="Detected Pattern Distribution"
                    )
                    st.pyplot(fig)
                
                # Recent patterns
                st.header("🎯 Recent Patterns")
                recent_days = st.slider("Show patterns from last N days", 1, 30, 7)
                recent_date = data.index[-1] - timedelta(days=recent_days)
                
                recent_patterns = []
                for pattern_name, pattern_series in patterns.items():
                    pattern_dates = data[pattern_series].index
                    recent_pattern_dates = pattern_dates[pattern_dates > recent_date]
                    
                    if len(recent_pattern_dates) > 0:
                        for date in recent_pattern_dates:
                            recent_patterns.append({
                                'Date': date.strftime('%Y-%m-%d'),
                                'Pattern': pattern_name,
                                'Close': f"₹{data.loc[date, 'Close']:.2f}"
                            })
                
                if recent_patterns:
                    recent_df = pd.DataFrame(recent_patterns)
                    st.dataframe(recent_df, use_container_width=True)
                else:
                    st.info(f"No patterns detected in the last {recent_days} days")
                
                # Data table
                st.header("📋 Raw Data")
                with st.expander("Show Raw Data"):
                    st.dataframe(data.tail(50), use_container_width=True)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Please try again with different parameters")
    
    else:
        st.info("👈 Configure your analysis in the sidebar and click 'Analyze'")
        
        # Show information
        st.markdown("""
        ### About NIFTY Candlestick Analyzer
        
        This application helps you analyze NIFTY index candlestick patterns. It detects common patterns including:
        
        - **Doji**: Indecision pattern where open and close are nearly equal
        - **Hammer**: Bullish reversal pattern with long lower shadow
        - **Inverted Hammer**: Bullish pattern with long upper shadow
        - **Bullish Engulfing**: Strong bullish reversal pattern
        - **Bearish Engulfing**: Strong bearish reversal pattern
        - **Morning Star**: Three-candle bullish reversal pattern
        - **Evening Star**: Three-candle bearish reversal pattern
        
        ### How to Use
        
        1. Select an index from the sidebar
        2. Choose the time period and interval
        3. Click "Analyze" to fetch data and detect patterns
        4. Explore the charts and pattern summary
        
        ### Note
        
        This tool is for educational purposes only. Always do your own research before making investment decisions.
        """)


if __name__ == "__main__":
    main()
