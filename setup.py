"""
Setup script for nfscan package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="nfscan",
    version="1.0.0",
    author="NIFTY Candlestick Analyzer Team",
    author_email="tomjubin@gmail.com",
    description="A Python package for analyzing NIFTY stock market candlestick patterns",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomjubin-cmd/https-github.com-yourusername-nifty-candlestick-analyzer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
)
