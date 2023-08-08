#!/bin/sh
#
# Created:      Nov, 04, 2022 14:01:15
set -eu

signal=$(nmcli dev wifi | grep "*" | awk '{print $8}')
bar=$(nmcli dev wifi | grep "*" | awk '{print $9}')

# i3blocks/i3blocks-contrib/wifi/wifiより
COLOR_GE80=${COLOR_GE80:-#00FF00}
COLOR_GE60=${COLOR_GE60:-#FFF600}
COLOR_GE40=${COLOR_GE40:-#FFAE00}
COLOR_LOWR=${COLOR_LOWR:-#FF0000}
COLOR_DOWN=${COLOR_DOWN:-#FF0000}

if [ -z "$signal" ]; then
  echo "Disconnected"
  echo "Disconnected"
  echo $COLOR_DOWN
else
  echo "$bar $signal%"
  echo "$bar $signal%"
  if [ $signal -ge 80 ]; then
    echo $COLOR_GE80
  elif [ $signal -ge 60 ]; then
    echo $COLOR_GE60
  elif [ $signal -ge 40 ]; then
    echo $COLOR_GE40
  else
    echo $COLOR_LOWR
  fi
fi
