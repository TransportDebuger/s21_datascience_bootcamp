#!/bin/sh

inputfile="hh_positions.csv"

if [ ! -f "$inputfile" ]; then
  echo "Error: Input file $inputfile not found."
  exit 1
fi

header=$(head -n 1 "$inputfile")

tail -n +2 "$inputfile" | awk -v header="$header" -F, '
  {
    split($2, datetime, "T")
    date = datetime[1]

    gsub(/[^0-9-]/, "", date)

    output_file = date ".csv"

    if (!(date in files)) {
      print header > output_file
      files[date] = 1
    }

    print >> output_file
  }
'

echo "Partitioned CSV files created."