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

# 1
# python3 -m cProfile -s tottime financial.py "$TICKER" "$FIELD" > profiling-sleep.txt

# 2
# python -m cProfile -s tottime financial.py MSFT "Total Revenue" > profiling-tottime.txt 

# 3
# python -m cProfile -s tottime financial_enhanced.py MSFT "Total Revenue" > profiling-http.txt

# 4
# python -m cProfile -s ncalls financial.py MSFT "Total Revenue" > profiling-ncalls.txt

# 5
python -m cProfile -o profile.prof financial.py MSFT "Total Revenue"
python -c "import pstats; p = pstats.Stats('profile.prof'); p.sort_stats('cumulative').print_stats(5)" > pstats-cumulative.txt