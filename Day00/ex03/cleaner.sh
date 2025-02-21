#!/bin/sh

inputfile="hh_sorted.csv"
outputfile="hh_positions.csv"

if [ ! -f "$inputfile" ]; then
  echo "Error: Input file $inputfile not found."
  exit 1
fi

{
  head -n 1 "$inputfile"
  tail -n +2 "$inputfile" | awk '
    BEGIN {
      FPAT = "([^,]+)|(\"[^\"]+\")"
    }
    {
      name = $3
      gsub(/"/, "", name)
      level = "-"
      if (name ~ /Junior|Middle|Senior/) {
        level = ""
        if (match(name, /(Junior|Middle|Senior)(\/[^ ]+)*/)) {
          level = substr(name, RSTART, RLENGTH)
        }
      }

      $3 = "\"" level "\""

      for (i = 1; i <= NF; i++) {
        if (i > 1) printf ","
        printf "%s", $i
      }
      printf "\n"
    }
  '
} > "$outputfile"

if [ -f "$outputfile" ]; then
  echo "Processed CSV file saved to $outputfile"
else
  echo "Error: Failed to create processed CSV file."
  exit 1
fi