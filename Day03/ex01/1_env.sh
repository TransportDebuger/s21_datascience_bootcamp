#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Error: Wrong parameters count. It must have single parameter."
  exit 1
fi

NICKNAME=$1

sudo apt install python3-virtualenv

virtualenv --python=python3 $NICKNAME

source $NICKNAME/bin/activate

pip install termgraph

# python3 venv.py

# rm -rf $NICKNAME