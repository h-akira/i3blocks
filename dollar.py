#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 2023-05-15 01:42:51

# Import
import os
import sys
# import json
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import traceback
import time

def parse_args():
  import argparse
  parser = argparse.ArgumentParser(description="""\

""", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--version", action="version", version='%(prog)s 0.0.1')
  parser.add_argument("--encoding", metavar="encoding", default="utf-8", help="encoding")
  parser.add_argument(
    "-e", "--error-file", metavar="error-file", 
    default=os.path.join(
      os.path.dirname(__file__), "dollar_error.txt"
    ), 
    help="error file"
  )
  parser.add_argument("-f", "--force", action="store_true", help="force to execute")
  # parser.add_argument("file", metavar="json-file", help="json file")
  options = parser.parse_args()
  # if not os.path.isfile(options.file): 
  #   raise Exception("The file does not exist.") 
  return options

def get_rate():
  URL = "https://www.click-sec.com/corp/guide/fxneo/rate/"
  # CHROMEDRIVER = "/usr/bin/chromedriver"
  options = Options()
  options.add_argument('--headless')
  # driver = webdriver.Chrome(CHROMEDRIVER, options=options)
  driver = webdriver.Chrome(options=options)
  driver.get(URL)
  dollar_yen_buy = driver.find_element(By.ID, "fxneorate_bid_0").text
  driver.quit()
  return dollar_yen_buy

def check_summer_time(now=None):
  if now is None:
    now = datetime.datetime.now()
  if now.month == 3:
    # 第二日曜日以降は夏時間
    if now.day - now.weekday() >= 8:
      return True
    else:
      return False
  elif now.month == 11:
    # 第一日曜日以降は冬時間
    if now.day - now.weekday() <= 1:
      return True
    else:
      return False
  elif 4<= now.month <= 10:
    return True
  else:
    return False
def market_open(now=None, diff_from_utc=0):
  # 年末年始等は非対応
  # ニューヨーク時間にする
  if now is None:
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
  else:
    now = now - datetime.timedelta(hours=diff_from_utc) - datetime.timedelta(hours=5)
  # 夏時間なら1時間進める
  if check_summer_time(now):
    now = now + datetime.timedelta(hours=1)
  # 判定
  if 0 <= now.weekday() <= 3:
    return True
  elif now.weekday() == 6 and now.hour >= 17:  
    return True
  elif now.weekday() == 4 and now.hour < 17:
    return True
  else:
    return False

def main():
  options = parse_args()
  execute = True
  if os.path.isfile(options.error_file):
    if options.force:
      os.remove(options.error_file)
    else:
      print("USD/JPY=NULL")
      sys.exit()
  # info = json.load(open(options.file, mode="r", encoding=options.encoding))
  if market_open():
    try:
      dollar_yen_buy = get_rate()
      if len(dollar_yen_buy)>7:
        dollar_yen_buy = dollar_yen_buy[:7]
      print(f"USD/JPY={dollar_yen_buy}")
    except:
      with open(options.error_file, mode="w", encoding=options.encoding) as f:
        f.write(traceback.format_exc())
      print("USD/JPY=NULL")
  else:
    print("Market is not open")

if __name__ == '__main__':
  main()
