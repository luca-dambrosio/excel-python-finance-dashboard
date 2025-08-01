import yfinance as yf
import pandas as pd
import argparse
import os

def get_stock_returns(ticker: str, period: str) -> pd.DataFrame:
    """
    Fetch stock data for the given ticker and period, calculate returns, and reorder columns.

    Args:
    ticker (str): Stock ticker symbol.
    period (str): Time period for the stock data.

    Returns:
    pd.DataFrame: Processed DataFrame with returns.
    """
    # Fetch stock data
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)

    # Reset the index to flatten the MultiIndex
    data = data.reset_index()

    # Convert 'Date' to datetime and set it as the index
    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    data = data.set_index('Date')

    # Calculate daily returns based on the 'Close' column
    data['Returns'] = data['Close'].pct_change()

    # Drop rows with NaN values (e.g., first row after calculating returns)
    data = data.dropna(subset=['Returns'])

    # Reorder columns so that 'Return' is the first column
    columns = ['Returns'] + [col for col in data.columns if col != 'Returns']
    data = data[columns]

    return data

script_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":

    # Including dynamically the arguments given from the excel
    parser = argparse.ArgumentParser(
        description="Ticker and Period"
    )
    parser.add_argument("--period", required=True, type=str)
    parser.add_argument("--tickers", required=True, type=str)
    parser.add_argument("--weights", required=True, type=str)
    args = parser.parse_args()

    # Output file to check that that inputs are correct
    output_path = os.path.join(script_dir, "output.txt")
    with open(output_path, "w") as f:
        f.write(f"{args.period}\n")
        f.write(f"{args.tickers}\n")
        f.write(f"{args.weights}\n")

    period = args.period
    # Process input, splitting by "/"
    tickers = args.tickers.split('/')  # List of companies
    weights = [float(x.replace(',', '.')) for x in args.weights.split('/')]
        
    dfs = []
    # Loop over tickers to get stock returns for each ticker and store in the list
    for i, ticker in enumerate(tickers):
        df = get_stock_returns(ticker, period) * weights[i]
        dfs.append(df)

    # Summing element-wise across al dfs
    df_portfolio = sum(dfs)

    # Generating the paths and loading the data as a csv
    path_price = os.path.join(script_dir, "prices_portfolio.csv")
    df_portfolio.to_csv(path_price, encoding = "utf-8")

    # Getting sp500 data as a benchmark
    path_price_sp = os.path.join(script_dir, "prices_sp500.csv")
    get_stock_returns("^GSPC", args.period).to_csv(path_price_sp, encoding = "utf-8")