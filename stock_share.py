#!/usr/bin/env python3
"""Stock data sharing script.
Fetches historical price data for given tickers and saves to CSV.
"""

import argparse
from datetime import datetime

import yfinance as yf


def parse_args():
    parser = argparse.ArgumentParser(description="Fetch stock data and save to CSV")
    parser.add_argument("tickers", nargs="+", help="Stock ticker symbols")
    parser.add_argument("--start", default="2023-01-01", help="Start date YYYY-MM-DD")
    parser.add_argument("--end", default=datetime.now().strftime("%Y-%m-%d"),
                        help="End date YYYY-MM-DD")
    parser.add_argument("--output", default="stock_data.csv", help="Output CSV file")
    return parser.parse_args()


def main():
    args = parse_args()
    data = yf.download(args.tickers, start=args.start, end=args.end)
    data.to_csv(args.output)
    print(f"Saved data to {args.output}")


if __name__ == "__main__":
    main()
