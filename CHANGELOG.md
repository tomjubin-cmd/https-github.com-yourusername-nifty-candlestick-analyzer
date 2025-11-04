# Changelog

All notable changes to the NIFTY Candlestick Analyzer (nfscan) project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-04

### Added
- Initial release of NIFTY Candlestick Analyzer (nfscan)
- Core Python package with modular architecture:
  - `data_fetcher.py`: Fetch NIFTY index data from Yahoo Finance
  - `pattern_detector.py`: Detect 7+ candlestick patterns
  - `visualizer.py`: Create beautiful candlestick charts
  - `utils.py`: Utility functions for analysis
  - `config.py`: Centralized configuration
- Candlestick pattern detection:
  - Doji
  - Hammer
  - Inverted Hammer
  - Bullish Engulfing
  - Bearish Engulfing
  - Morning Star
  - Evening Star
- Interactive Streamlit web application
- Comprehensive test suite with 11+ unit tests
- Docker and Docker Compose support
- Deployment configurations:
  - Heroku (Procfile, runtime.txt)
  - AWS (Elastic Beanstalk, ECS, EC2)
  - GCP (Cloud Run, App Engine)
  - Azure (Container Instances, App Service)
- Documentation:
  - README.md with quick start guide
  - DEPLOYMENT.md with detailed deployment instructions
  - CONTRIBUTING.md for contributors
  - Example usage script (example.py)
  - Jupyter notebook for exploratory analysis
- Shell scripts for easy deployment:
  - `deploy.sh`: Automated setup script
  - `run.sh`: Quick start script
- GitHub Actions CI/CD pipeline
- MIT License
- .gitignore for Python projects

### Features
- Real-time data fetching from Yahoo Finance
- Support for multiple NIFTY indices (50, BANK, IT, AUTO, PHARMA)
- Pattern summary with counts and percentages
- Multiple chart types:
  - Candlestick charts
  - Charts with pattern markers
  - Price movement charts
  - Pattern distribution charts
  - Volume charts
- Data export to CSV
- Configurable time periods and intervals
- Responsive web interface
- Health check endpoints for containers

### Technical
- Python 3.11+ support
- Dependencies:
  - pandas >= 2.0.0
  - yfinance >= 0.2.28
  - matplotlib >= 3.7.0
  - mplfinance >= 0.12.9b7
  - streamlit >= 1.28.0
- Containerized deployment ready
- Cloud-native architecture
- Modular and extensible design

### Documentation
- Comprehensive README with usage examples
- Deployment guide for multiple platforms
- Contributing guidelines
- Code examples and Jupyter notebook
- Inline code documentation with docstrings

## [Unreleased]

### Planned Features
- Additional candlestick patterns (Shooting Star, Piercing Line, etc.)
- Machine learning-based pattern prediction
- Real-time alerts for pattern detection
- Portfolio tracking
- Historical backtesting
- REST API for programmatic access
- Mobile-responsive design improvements
- Database integration for historical data caching
- Multi-language support
- Advanced technical indicators (RSI, MACD, etc.)

---

## Version History

- **1.0.0** (2025-11-04): Initial release with core features
