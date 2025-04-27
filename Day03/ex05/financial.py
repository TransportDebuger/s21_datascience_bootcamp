import sys
import time
import requests
import re
from bs4 import BeautifulSoup

def fetch_financial_page(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_financial_data(html, field):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('div', attrs={"class": "row"})
    for row in rows:
        title_span = row.find('div', string=field)
        if title_span:
            value_divs = row.find_all('div', class_="column")
            values = [div.get_text(strip=True) for div in value_divs]
            return tuple(values)

    raise Exception(f"Field '{field}' not found in financial table")

def get_financial_data(ticker, field):
    time.sleep(5)
    html = fetch_financial_page(ticker)
    result = parse_financial_data(html, field)
    return result

def main():
    if len(sys.argv) != 3:
        raise ValueError("Requires two arguments: ticker and field")
    ticker, field = sys.argv[1], sys.argv[2]
    data = get_financial_data(ticker, field)
    print(data)

if __name__ == "__main__":
    main()