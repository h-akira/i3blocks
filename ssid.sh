#!/bin/sh
#
# Created:      Nov, 04, 2022 14:01:15
set -eu

ssid=$(nmcli dev wifi | grep "*" | awk '{print $3}')

# i3blocks/i3blocks-contrib/wifi/wifiより
COLOR_ON=${COLOR_ON:-#00FF00}
COLOR_DOWN=${COLOR_DOWN:-#FF0000}

if [ -n "$ssid" ]; then
  echo "$ssid"
fi
