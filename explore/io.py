from datetime import datetime

def main():
    print('Hi!')

    stock_symbol = raw_input("What stock symbol are you interested in? ")
    start_date = datetime.strptime(raw_input("What start date (yyyy-mm-dd)? "), '%Y-%m-%d')
    end_date = datetime.strptime(raw_input("What end date (yyyy-mm-dd)? "), '%Y-%m-%d')

    print('Lets checkout {} for {} to {} now...'.format(stock_symbol.upper(), start_date.date(), end_date.date()))

if __name__ == '__main__':
    main()
