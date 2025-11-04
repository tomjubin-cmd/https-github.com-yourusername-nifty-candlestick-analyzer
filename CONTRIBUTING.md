# Contributing to NIFTY Candlestick Analyzer (nfscan)

Thank you for your interest in contributing to nfscan! This document provides guidelines for contributing to the project.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [How to Contribute](#how-to-contribute)
4. [Development Guidelines](#development-guidelines)
5. [Testing](#testing)
6. [Submitting Changes](#submitting-changes)

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please be respectful and constructive in all interactions.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/https-github.com-yourusername-nifty-candlestick-analyzer.git
   cd https-github.com-yourusername-nifty-candlestick-analyzer
   ```
3. **Set up development environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## How to Contribute

### Reporting Bugs

- **Check existing issues** to avoid duplicates
- **Use the issue template** if available
- **Provide detailed information**:
  - Steps to reproduce
  - Expected behavior
  - Actual behavior
  - System information (OS, Python version, etc.)
  - Screenshots if applicable

### Suggesting Enhancements

- **Check existing feature requests** first
- **Clearly describe the enhancement** and its benefits
- **Provide use cases** if possible

### Code Contributions

We welcome contributions in the following areas:

1. **New candlestick patterns**: Add detection for additional patterns
2. **Data sources**: Integrate new data providers
3. **Visualizations**: Enhance charts and graphs
4. **Performance improvements**: Optimize algorithms
5. **Documentation**: Improve or translate documentation
6. **Bug fixes**: Fix reported issues
7. **Tests**: Add or improve test coverage

## Development Guidelines

### Code Style

- Follow **PEP 8** style guide for Python code
- Use **meaningful variable names**
- Add **docstrings** to all functions and classes
- Keep functions **focused and small**
- Use **type hints** where appropriate

Example:
```python
def detect_pattern(data: pd.DataFrame, threshold: float = 0.1) -> pd.Series:
    """
    Detect candlestick pattern in the data.
    
    Args:
        data (pd.DataFrame): DataFrame with OHLC data
        threshold (float): Detection threshold (default: 0.1)
        
    Returns:
        pd.Series: Boolean series indicating pattern occurrences
    """
    # Implementation here
    pass
```

### Project Structure

```
nfscan/
├── nfscan/              # Core package
│   ├── __init__.py
│   ├── config.py        # Configuration
│   ├── data_fetcher.py  # Data fetching
│   ├── pattern_detector.py  # Pattern detection
│   ├── visualizer.py    # Visualization
│   └── utils.py         # Utilities
├── tests/               # Test files
├── deploy/              # Deployment files
└── notebooks/           # Jupyter notebooks
```

### Adding New Features

1. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Implement your feature** following the guidelines

3. **Add tests** for your feature

4. **Update documentation** as needed

### Adding New Patterns

To add a new candlestick pattern:

1. **Add detection method** to `pattern_detector.py`:
   ```python
   def detect_your_pattern(self):
       """
       Detect Your Pattern.
       
       Returns:
           pd.Series: Boolean series indicating pattern occurrences
       """
       # Implementation
       result = pd.Series([False] * len(self.data), index=self.data.index)
       # Pattern logic here
       self.patterns['Your Pattern'] = result
       return result
   ```

2. **Update `detect_all_patterns()` method** to include your pattern

3. **Add tests** in `tests/test_pattern_detector.py`

4. **Update documentation** in README.md

## Testing

### Running Tests

```bash
# Run all tests
python -m unittest discover tests/ -v

# Run specific test file
python -m unittest tests/test_pattern_detector.py -v
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Use descriptive test method names
- Test both success and failure cases
- Aim for high code coverage

Example test:
```python
def test_detect_pattern(self):
    """Test pattern detection"""
    detector = PatternDetector(self.test_data)
    result = detector.detect_pattern()
    
    self.assertIsInstance(result, pd.Series)
    self.assertEqual(len(result), len(self.test_data))
    # Add more assertions
```

## Submitting Changes

### Before Submitting

1. **Run all tests** and ensure they pass
2. **Update documentation** if needed
3. **Follow code style guidelines**
4. **Write clear commit messages**

### Commit Messages

Use clear and descriptive commit messages:

```
Add detection for bullish harami pattern

- Implement detection logic in pattern_detector.py
- Add tests for the new pattern
- Update documentation with pattern description
```

Format:
- First line: Brief summary (50 chars or less)
- Blank line
- Detailed description if needed

### Pull Request Process

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub:
   - Use a descriptive title
   - Explain what changes you made and why
   - Reference any related issues
   - Include screenshots for UI changes

3. **Address review comments** if any

4. **Wait for approval** and merge

### Pull Request Checklist

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] PR description is detailed

## Development Tips

### Virtual Environment

Always use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Debugging

Use the example script to test changes:
```bash
python example.py
```

### Interactive Testing

Use the Jupyter notebook for interactive development:
```bash
jupyter notebook notebooks/exploratory.ipynb
```

### Docker Testing

Test Docker deployment locally:
```bash
docker build -t nfscan-test .
docker run -p 8501:8501 nfscan-test
```

## Questions?

If you have questions:
- Check existing issues and discussions
- Open a new issue with the "question" label
- Reach out to maintainers

## Recognition

Contributors will be:
- Listed in the project's contributors
- Credited in release notes for significant contributions
- Acknowledged in the README

Thank you for contributing to nfscan! 🎉
