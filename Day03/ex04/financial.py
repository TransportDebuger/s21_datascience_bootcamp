import sys
import time
import requests
# import httpx
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) != 3:
        raise Exception("Requires two arguments: ticker and field")

    ticker, field = sys.argv[1], sys.argv[2]
    # time.sleep(5)

    url = f'https://finance.yahoo.com/quote/{ticker}/financials'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # try:
    #     with httpx.Client() as client:  # Using httpx
    #         response = client.get(url, headers=headers)
    #         response.raise_for_status()
    # except httpx.HTTPError:
    #     raise Exception("Failed to fetch data")
    try:
       response = requests.get(url, headers=headers)
       response.raise_for_status()
    except requests.exceptions.RequestException:
       raise Exception("Failed to fetch data: invalid ticker or network error")

    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('div', attrs={"class": "row"})

    for row in rows:
        title_span = row.find('div', string=field)
        if title_span:
            value_divs = row.find_all('div', class_="column")
            values = [div.get_text(strip=True) for div in value_divs]
            return tuple(values)

    raise Exception(f"Field '{field}' not found in financial table")

if __name__ == "__main__":
    try:
        result = main()
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)