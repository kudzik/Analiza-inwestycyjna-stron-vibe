"""Konfiguracja pakietu inwestor-pro."""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="inwestor-pro",
    version="1.0.0",
    author="Inwestor Pro Team",
    author_email="team@inwestor-pro.com",
    description="Narzędzie do automatycznej analizy stron internetowych i generowania perswazyjnych broszur inwestycyjnych",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/inwestor-pro",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "inwestor-pro=inwestor_pro:main",
        ],
    },
    keywords="investment analysis, web scraping, financial tools, AI",
    project_urls={
        "Bug Reports": "https://github.com/your-username/inwestor-pro/issues",
        "Source": "https://github.com/your-username/inwestor-pro",
    },
)
