# 📊 Excel–Python Dashboard for Financial Data & Portfolio Analysis

This project builds an integrated Excel dashboard powered by Python to fetch, process, and display historical financial data and portfolio returns. It provides an accessible alternative to tools like Bloomberg by combining VBA macros with Yahoo Finance APIs.

## 📁 Files

- `DASHBOARD.xlsm` – Excel workbook with embedded VBA macros for single stock or portfolio data retrieval  
- `get_data.py` – Downloads stock prices, returns, balance sheets, and financial statements from Yahoo Finance  
- `get_data_portfolio.py` – Computes weighted portfolio returns from user-defined tickers and weights  
- `group13_report.pdf` – Final report describing methodology, integration architecture, and limitations  

## 📊 Summary

### 1. Functionality  
- Fetches daily price data, balance sheets, and financials for any S&P500 stock  
- Users can define a **custom portfolio (max 10 stocks)** with weights and time period  
- Computes and compares portfolio returns vs. the S&P 500 benchmark  
- Data is downloaded and **automatically loaded into Excel** through VBA macros

### 2. Workflow  
- User inputs tickers, weights, and time span in Excel  
- VBA triggers a Python script via PowerShell  
- Python pulls data from Yahoo Finance and stores it as CSVs  
- VBA imports these CSVs into Excel, updating the dashboard

### 3. Key Features  
- Intuitive Excel UI  
- Seamless Excel ⇄ Python communication  
- Portfolio-level aggregation and benchmarking  
- Real-time data retrieval using `yfinance`

## 🔧 Tools & Technologies

- **Excel VBA** for macros and UI interaction  
- **Python** (pandas, yfinance, argparse, os) for backend processing  
- Yahoo Finance API for data retrieval  
- Windows PowerShell for Excel-to-Python integration

## 📌 Notes

- Only tested on **Windows** due to PowerShell dependency  
- Requires user to manually define path to `python.exe` in VBA settings  

---

📈 Completed as part of a course in Applied Numerical Finance.
