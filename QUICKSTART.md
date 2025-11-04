# Quick Start Guide - NIFTY Candlestick Analyzer (nfscan)

This guide will help you get the NIFTY Candlestick Analyzer up and running in under 5 minutes.

## 🚀 Fastest Way to Deploy

### Option 1: One-Command Local Setup (Recommended for Development)

```bash
git clone https://github.com/tomjubin-cmd/https-github.com-yourusername-nifty-candlestick-analyzer.git
cd https-github.com-yourusername-nifty-candlestick-analyzer
./deploy.sh && ./run.sh
```

That's it! The app will open at `http://localhost:8501`

### Option 2: Docker (Recommended for Production)

```bash
git clone https://github.com/tomjubin-cmd/https-github.com-yourusername-nifty-candlestick-analyzer.git
cd https-github.com-yourusername-nifty-candlestick-analyzer
docker-compose up -d
```

Access at `http://localhost:8501`

### Option 3: Heroku (Recommended for Cloud)

```bash
git clone https://github.com/tomjubin-cmd/https-github.com-yourusername-nifty-candlestick-analyzer.git
cd https-github.com-yourusername-nifty-candlestick-analyzer
heroku create your-nfscan-app
git push heroku main
heroku open
```

## 📋 Prerequisites

Choose based on your deployment method:

**Local Setup:**
- Python 3.11+
- pip

**Docker:**
- Docker
- Docker Compose (optional)

**Cloud (Heroku/AWS/GCP/Azure):**
- Account on the platform
- CLI tool installed (optional but recommended)

## 🎯 What You Get

- **Web Interface**: Beautiful, interactive Streamlit app
- **Real-time Data**: Fetch live NIFTY index data
- **Pattern Detection**: 7+ candlestick patterns automatically detected
- **Visualizations**: Professional charts with pattern markers
- **Multiple Indices**: NIFTY 50, BANK, IT, AUTO, PHARMA

## 📊 Using the Application

1. **Select Index**: Choose from NIFTY 50, BANK, IT, AUTO, or PHARMA
2. **Set Parameters**: Pick time period (1mo - 5y) and interval (daily/weekly/monthly)
3. **Click Analyze**: Application fetches data and detects patterns
4. **Explore Results**: View charts, pattern summaries, and recent patterns

## 🔧 Basic Commands

```bash
# Local development
python example.py                    # Run example script
streamlit run deploy/app.py          # Start web app
python -m unittest discover tests/   # Run tests

# Docker
docker build -t nfscan .             # Build image
docker run -p 8501:8501 nfscan       # Run container
docker-compose up -d                 # Start with compose
docker-compose logs -f               # View logs
docker-compose down                  # Stop

# Package installation
pip install -e .                     # Install as package
```

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [README.md](README.md) | Complete project overview and features |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Detailed deployment guide for all platforms |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Guidelines for contributing |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [example.py](example.py) | Usage examples |
| [notebooks/exploratory.ipynb](notebooks/exploratory.ipynb) | Interactive analysis |

## 🐛 Troubleshooting

**Port 8501 already in use:**
```bash
lsof -ti:8501 | xargs kill -9
```

**Module import errors:**
```bash
pip install -r requirements.txt --force-reinstall
```

**Docker issues:**
```bash
docker system prune -a
```

## 📞 Getting Help

- 📖 Read the [full documentation](README.md)
- 🔍 Check [deployment guide](DEPLOYMENT.md)
- 🐛 Report issues on [GitHub Issues](https://github.com/tomjubin-cmd/https-github.com-yourusername-nifty-candlestick-analyzer/issues)

## ⚡ Advanced Usage

### Python API

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

### Command Line

```bash
# Run example with output
python example.py

# Start web server on custom port
streamlit run deploy/app.py --server.port=8080
```

## 🌟 Next Steps

1. ✅ Get the app running (you're here!)
2. 📖 Read the full [README.md](README.md)
3. 🚀 Check [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment
4. 🤝 See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
5. 📊 Try the Jupyter notebook for analysis

## ⚠️ Disclaimer

This tool is for educational and informational purposes only. Not financial advice. Always do your own research before making investment decisions.

---

**Ready to analyze? Run `./deploy.sh && ./run.sh` and start analyzing! 🚀**
