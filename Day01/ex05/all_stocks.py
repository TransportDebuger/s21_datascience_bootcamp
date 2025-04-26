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

    input_str = sys.argv[1]
    parts = input_str.split(',')
    expressions = [p.strip() for p in parts]

    if any(not expr for expr in expressions):
        return

    ticker_to_company = {v: k for k, v in COMPANIES.items()}

    for expr in expressions:
        company_name = expr.title()
        if company_name in COMPANIES:
            ticker = COMPANIES[company_name]
            print(f"{company_name} stock price is {STOCKS[ticker]}")
            continue

        ticker_symbol = expr.upper()
        if ticker_symbol in STOCKS:
            company = ticker_to_company[ticker_symbol]
            print(f"{ticker_symbol} is a ticker symbol for {company}")
            continue

        print(f"{expr} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    main()