#!/bin/sh
#
# Created:      Oct, 16, 2022 02:38:17
set -eu

COLOR_DOWN=${COLOR_DOWN:-#FF0000}
if [ -e "$(which xkeysnail)" ]; then
  PID=`ps --no-heading -C xkeysnail -o pid | tr -d ' '`
  if [ -n "$PID" ]; then
    echo "xkeysnail: ON"
  else
    echo "xkeysnail: OFF"
    echo "xkeysnail: OFF"
    echo ${COLOR_DOWN}
  fi
else
  echo "xkeysnail: NONE"
fi
