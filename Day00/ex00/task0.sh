#!/bin/bash

# Check if the vacancy name is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <vacancy_name>"
  exit 1
fi

# URL-encode the vacancy name to handle spaces and special characters
VACANCY_NAME=$(echo "$1" | jq -sRr @uri)

# API endpoint for vacancies search
API_URL="https://api.hh.ru/vacancies?text=${VACANCY_NAME}&per_page=20"

# Fetch the data using curl
curl -s "$API_URL" -o hh.json

# Check if the file was created successfully
if [ -f "hh.json" ]; then
  echo "Data saved to hh.json"
else
  echo "Failed to fetch data from the API."
  exit 1
fi