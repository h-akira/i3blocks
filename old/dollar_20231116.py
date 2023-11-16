#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 2023-05-15 01:42:51

# Import
import os
import json
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import traceback

def parse_args():
  import argparse
  parser = argparse.ArgumentParser(description="""\

""", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--version", action="version", version='%(prog)s 0.0.1')
  parser.add_argument("--encoding", metavar="encoding", default="utf-8", help="encoding")
  parser.add_argument("-e", "--error", action="store_true", help="print error message")
  parser.add_argument("file", metavar="json-file", help="json file")
  options = parser.parse_args()
  if not os.path.isfile(options.file): 
    raise Exception("The file does not exist.") 
  return options

# def get_rate():
#   URL = "https://www.click-sec.com/corp/guide/fxneo/rate/"
#   CHROMEDRIVER = "/usr/bin/chromedriver"
#   options = Options()
#   options.add_argument('--headless')
#   driver = webdriver.Chrome(CHROMEDRIVER, options=options)
#   driver.get(URL)
#   dollar_yen_buy = driver.find_element_by_id("fxneorate_bid_0").text
#   driver.quit()
#   return dollar_yen_buy

def get_rate_AlphaVantage(KEY):
  url = 'https://www.alphavantage.co/query'
  params = {
    'function': 'CURRENCY_EXCHANGE_RATE',
    'from_currency': 'USD',
    'to_currency': 'JPY',
    'apikey': KEY
  }
  response = requests.get(url, params=params)
  data = response.json()
  return float(data["Realtime Currency Exchange Rate"]["8. Bid Price"])

def market_open():
  DIFF_JST_FROM_UTC = 9
  now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
  num = now.weekday()
  if 1 <= num <= 4:
    return True
  elif num == 0 and now.hour >= 7:  
    return True
  elif num == 5 and now.hour < 7:
    return True
  else:
    return False

def main():
  options = parse_args()
  info = json.load(open(options.file, mode="r", encoding=options.encoding))
  if market_open():
    try:
      # dollar_yen_buy = get_rate()
      dollar_yen_buy = str(get_rate_AlphaVantage(info["dollar"]["KEY"]))
      if len(dollar_yen_buy)>7:
        dollar_yen_buy = dollar_yen_buy[:7]
    except Exception:
      if options.error:
        print("=== Error ===")
        traceback.print_exc()
      dollar_yen_buy = "NULL"
    print(f"USD/JPY={dollar_yen_buy}")
  else:
    print("Market is not open")

if __name__ == '__main__':
  main()
