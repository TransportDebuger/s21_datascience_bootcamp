import sys

def main():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    
    if len(sys.argv) != 2:
        return
    
    input_ticker = sys.argv[1].upper()
    ticker_to_company = {v: k for k, v in COMPANIES.items()}
    
    if input_ticker in ticker_to_company:
        company_name = ticker_to_company[input_ticker]
        stock_price = STOCKS[input_ticker]
        print(f"{company_name} {stock_price}")
    else:
        print("Unknown ticker")

if __name__ == '__main__':
    main()