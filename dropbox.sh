#!/bin/sh
#
# Created:      2023-03-11 23:44:23
set -eu

if [ -n "$(ps -C dropbox -o pid --no-heading)" ]; then
  echo "Dropbox: ON"
else
  COLOR_DOWN=${COLOR_DOWN:-#FF0000}
  echo "Dropbox: OFF"
  echo "Dropbox: OFF"
  echo ${COLOR_DOWN}
fi
