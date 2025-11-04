"""
Example usage of nfscan package
"""

from nfscan import DataFetcher, PatternDetector, Visualizer


def main():
    """Main example function"""
    
    print("NIFTY Candlestick Analyzer - Example Usage")
    print("=" * 50)
    
    # Fetch data
    print("\n1. Fetching NIFTY 50 data...")
    fetcher = DataFetcher("^NSEI")
    data = fetcher.fetch_data(period="3mo", interval="1d")
    print(f"   ✅ Fetched {len(data)} data points")
    
    # Display basic info
    print("\n2. Basic Statistics:")
    print(f"   Latest Close: ₹{data['Close'].iloc[-1]:.2f}")
    print(f"   Period High: ₹{data['High'].max():.2f}")
    print(f"   Period Low: ₹{data['Low'].min():.2f}")
    
    # Detect patterns
    print("\n3. Detecting candlestick patterns...")
    detector = PatternDetector(data)
    patterns = detector.detect_all_patterns()
    
    # Show pattern summary
    print("\n4. Pattern Summary:")
    summary = detector.get_pattern_summary()
    print(summary.to_string(index=False))
    
    # Visualize
    print("\n5. Generating visualizations...")
    visualizer = Visualizer(data)
    
    # Save charts
    print("   Saving candlestick chart...")
    fig = visualizer.plot_candlestick(title="NIFTY 50 Candlestick Chart")
    visualizer.save_figure(fig, "nifty_candlestick.png")
    print("   ✅ Saved to nifty_candlestick.png")
    
    print("   Saving patterns chart...")
    fig = visualizer.plot_with_patterns(patterns, title="NIFTY 50 with Patterns")
    visualizer.save_figure(fig, "nifty_patterns.png")
    print("   ✅ Saved to nifty_patterns.png")
    
    print("   Saving price movement chart...")
    fig = visualizer.plot_price_movement(title="NIFTY 50 Price Movement")
    visualizer.save_figure(fig, "nifty_price_movement.png")
    print("   ✅ Saved to nifty_price_movement.png")
    
    print("\n✅ Example complete! Check the generated PNG files.")


if __name__ == "__main__":
    main()
