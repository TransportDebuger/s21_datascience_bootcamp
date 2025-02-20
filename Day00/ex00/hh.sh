#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <vacancy_name>"
  exit 1
fi

VACANCY_NAME=$(echo "$1" | jq -sRr @uri)
API_URL="https://api.hh.ru/vacancies?text=${VACANCY_NAME}&per_page=20"
curl -s "$API_URL" | jq '.' > hh.json
if [ -f "hh.json" ]; then
  echo "Data saved to hh.json"
else
  echo "Failed to fetch data from the API."
  exit 1
fi