#!/bin/sh

outputfile="hh_concatenated.csv"

files=$(ls *.csv | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}\.csv$')

if [ -z "$files" ]; then
  echo "Error: No partitioned CSV files found."
  exit 1
fi

{
  head -n 1 $(echo "$files" | head -n 1)

  for file in $files; do
    tail -n +2 "$file"
  done
} > "$outputfile"

echo "Concatenated CSV file saved to $outputfile"