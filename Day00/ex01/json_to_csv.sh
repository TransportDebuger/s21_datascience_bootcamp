#!/bin/sh

json_file="hh.json"
jq_filter="filter.jq"
csv_file="hh.csv"

if [ ! -f "$json_file" ]; then
  echo "Error: Input file $json_file not found."
  exit 1
fi

jq -r -f "$jq_filter" "$json_file" > "$csv_file"

if [ -f "$csv_file" ]; then
  echo "CSV file saved to $csv_file"
else
  echo "Error: Failed to create CSV file."
  exit 1
fi