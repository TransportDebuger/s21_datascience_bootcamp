#!/bin/bash

if [ $# -ne 3 ]; then
  echo "Error: Requires 3 parameters: <nickname> <ticker> <field>"
  exit 1
fi

NICKNAME=$1
TICKER=$2
FIELD=$3

sudo apt install python3-virtualenv -y

virtualenv --python=python3 $NICKNAME

source $NICKNAME/bin/activate

pip install beautifulsoup4 requests pytest

python3 financial.py "$TICKER" "$FIELD"