# pcost.py
#
# Exercise 1.27
import sys
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return sum(d["shares"] * d["price"] for d in portfolio)


def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print(f"Total : {cost}")


if __name__ == "__main__":
    main(sys.argv)
    
