# 📈 NIFTY Candlestick Analyzer (nfscan)

A comprehensive Python application for analyzing NIFTY stock market candlestick patterns with deployment-ready configurations.

## Features

- 📊 **Real-time Data Fetching**: Fetch NIFTY index data using yfinance
- 🔍 **Pattern Detection**: Detect 7+ common candlestick patterns
  - Doji
  - Hammer
  - Inverted Hammer
  - Bullish Engulfing
  - Bearish Engulfing
  - Morning Star
  - Evening Star
- 📈 **Visualization**: Beautiful candlestick charts with pattern markers
- 🌐 **Web Interface**: Interactive Streamlit web application
- 🐳 **Docker Ready**: Containerized deployment with Docker and Docker Compose
- ☁️ **Cloud Deployment**: Ready for Heroku, AWS, GCP, and other platforms

## Quick Start

### Prerequisites

- Python 3.11+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/tomjubin-cmd/https-github.com-yourusername-nifty-candlestick-analyzer.git
cd https-github.com-yourusername-nifty-candlestick-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run deploy/app.py
```

4. Open your browser to `http://localhost:8501`

## Deployment Options

### Option 1: Docker

Build and run using Docker:

```bash
docker build -t nfscan .
docker run -p 8501:8501 nfscan
```

### Option 2: Docker Compose

```bash
docker-compose up -d
```

### Option 3: Heroku

1. Create a Heroku app:
```bash
heroku create your-app-name
```

2. Deploy:
```bash
git push heroku main
```

### Option 4: Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run deploy/app.py
```

## Usage

### Command Line

```python
from nfscan import DataFetcher, PatternDetector, Visualizer

# Fetch data
fetcher = DataFetcher("^NSEI")
data = fetcher.fetch_data(period="1y")

# Detect patterns
detector = PatternDetector(data)
patterns = detector.detect_all_patterns()
summary = detector.get_pattern_summary()

# Visualize
visualizer = Visualizer(data)
fig = visualizer.plot_with_patterns(patterns)
visualizer.show_figure(fig)
```

### Web Interface

1. Select an index (NIFTY 50, NIFTY BANK, etc.)
2. Choose time period and interval
3. Click "Analyze" to fetch data and detect patterns
4. Explore interactive charts and pattern summaries

## Project Structure

```
nfscan/
├── nfscan/                  # Core Python package
│   ├── __init__.py
│   ├── config.py            # Configuration settings
│   ├── data_fetcher.py      # Data fetching module
│   ├── pattern_detector.py  # Pattern detection logic
│   ├── visualizer.py        # Visualization module
│   └── utils.py             # Utility functions
├── tests/                   # Unit tests
│   ├── __init__.py
│   ├── test_utils.py
│   └── test_pattern_detector.py
├── deploy/                  # Deployment files
│   └── app.py               # Streamlit web application
├── data/                    # Data directory
├── notebooks/               # Jupyter notebooks
├── .streamlit/              # Streamlit configuration
│   └── config.toml
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── Procfile                 # Heroku configuration
├── runtime.txt              # Python version for Heroku
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md
```

## Running Tests

```bash
python -m pytest tests/
```

Or run individual test files:
```bash
python -m unittest tests/test_utils.py
python -m unittest tests/test_pattern_detector.py
```

## Environment Variables

No environment variables are required for basic usage. For production deployment, you may want to configure:

- `PORT`: Server port (default: 8501)
- `API_KEY`: If using external APIs for data

## Supported Indices

- NIFTY 50 (^NSEI)
- NIFTY BANK (^NSEBANK)
- NIFTY IT (^CNXIT)
- NIFTY AUTO (^CNXAUTO)
- NIFTY PHARMA (NIFTYPHARMA.NS)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for educational and informational purposes only. It should not be considered as financial advice. Always do your own research and consult with financial advisors before making investment decisions.

## Support

For issues and questions, please open an issue on GitHub.

## Acknowledgments

- Data provided by Yahoo Finance via yfinance
- Built with Streamlit, pandas, and mplfinance
