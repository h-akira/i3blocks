#!/bin/sh
#
# Created:      2023-02-25 13:32:43
set -eu

state=${HOME}/.local/opt/SharePhoto/secret/state.txt

if [ -e $state ]; then
  STATE="`cat $state`"
  if [ "${STATE}" != "Updated" ]; then
    COLOR_DOWN=${COLOR_DOWN:-#FF0000}
    echo "Photo: ${STATE}"
    echo "Photo: ${STATE}"
    echo ${COLOR_DOWN}
  else
    echo "Photo: ${STATE}"
  fi
fi
