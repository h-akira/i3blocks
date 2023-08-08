#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 2023-08-08 22:18:26

import os
import json
import subprocess

def parse_args():
  import argparse
  parser = argparse.ArgumentParser(description="""\

""", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--version", action="version", version='%(prog)s 0.0.1')
  parser.add_argument("--encoding", metavar="encoding", default="utf-8", help="encoding")
  parser.add_argument("file", metavar="json-file", help="json file")
  options = parser.parse_args()
  if not os.path.isfile(options.file): 
    raise Exception("The file does not exist.") 
  return options

def check(mac):
  # CMD = "bluetoothctl info 70:74:C9:15:34:30 | grep Connected"
  # CMD = "bluetoothctl info C9:2E:64:7C:40:E0 | grep Connected"
  CMD = f"bluetoothctl info {mac} | grep Connected"
  result = subprocess.run(CMD, shell=True, stdout=subprocess.PIPE)
  output = result.stdout.decode('utf-8').strip() 
  if "yes" in output:
    return True
  else:
    return False

def main():
  options = parse_args()
  info = json.load(open(options.file, mode="r", encoding=options.encoding))
  text = ""
  for key, value in info["bluetooth"].items():
    if check(value):
      text += f"{key}: ON "
    else:
      text += f"{key}: OFF "
  if len(text)>0:
    text = text[:-1]
  print(text)

if __name__ == '__main__':
  main()
