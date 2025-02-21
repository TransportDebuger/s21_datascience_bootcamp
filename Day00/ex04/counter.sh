#!/bin/sh

inputfile="hh_positions.csv"
outputfile="hh_uniq_positions.csv"

if [ ! -f "$inputfile" ]; then
  echo "Error: Input file $inputfile not found."
  exit 1
fi

{
  echo '"name","count"'
  awk -F, '
    NR > 1 {
      name = $3
      gsub(/"/, "", name)
      count[name]++
    }
    END {
      for (name in count) {
        printf "\"%s\",%d\n", name, count[name]
      }
    }
  ' "$inputfile" | sort -t, -k2,2nr
} > "$outputfile"

if [ -f "$outputfile" ]; then
  echo "Unique positions counted and saved to $outputfile"
else
  echo "Error: Failed to create output CSV file."
  exit 1
fi