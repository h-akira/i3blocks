#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 2023-05-15 01:42:51

# Import
import datetime
import traceback
import os
from contextlib import redirect_stdout

def parse_args():
  import argparse
  parser = argparse.ArgumentParser(description="""\
ticker: https://optrip.xyz/?p=4467
""", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--version", action="version", version='%(prog)s 0.0.1')
  parser.add_argument("-r", "--round", metavar="桁数", type=int, default=3, help="小数点以下の桁数")
  parser.add_argument("-t", "--ticker", metavar="ticker", default="USDJPY=X", help="ticker")
  parser.add_argument("-n", "--name", metavar="name", default="USD/JPY", help="name")
  options = parser.parse_args()
  return options

def main():
  options = parse_args()
  try:
    import pandas_datareader.data as web
    import yfinance as yf
    yf.pdr_override()
    start = datetime.date.today() - datetime.timedelta(days=7)
    with redirect_stdout(open(os.devnull, 'w')):
      df = web.get_data_yahoo(tickers=options.ticker,start=start)
    price = df.iloc[-1]["Close"]
  except Exception:
    if options.error:
      print("=== Error ===")
      traceback.print_exc()
    price = "NULL"
  print(f"USD/JPY={round(price, options.round)}")

if __name__ == '__main__':
  main()
