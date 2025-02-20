#!/bin/sh

inputfile="hh.csv"
sortedfile="hh_sorted.csv"

if [ ! -f "$inputfile" ]; then
  echo "Error: Input file $inputfile not found."
  exit 1
fi

head -n 1 "$inputfile" > "$sortedfile"
tail -n +2 "$inputfile" | sort -t, -k2,2 -k1,1 >> "$sortedfile"

if [ -f "$sortedfile" ]; then
  echo "Sorted CSV file saved to $sortedfile"
else
  echo "Error: Failed to create sorted CSV file."
  exit 1
fi