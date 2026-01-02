# report.py
#
# Exercise 2.4
import sys
from fileparse import parse_csv
from stock import Stock
import tableformat
from portfolio import Portfolio


def read_portfolio(filename: str, **options) -> Portfolio:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as f:
        return Portfolio.from_csv(f, **options)


def read_prices(filename: str) -> dict:
    """
    Read a prices file into a dict with the names as the keys and the the
    prices as the values
    """
    with open(filename) as f:
        return dict(parse_csv(f, has_headers=False, types=[str, float]))


def make_report(portfolio: list[Stock], prices: dict) -> list[tuple]:
    rows = []
    for s in portfolio:
        newprice = prices[s.name]
        change = newprice - s.price
        t = (s.name, s.shares, newprice, change)
        rows.append(t)
    return rows


def print_gain_loss(portfolio: list[Stock], prices: dict):
    new_value = 0
    old_value = 0
    for s in portfolio:
        old_value += s.shares * s.price
        new_value += s.shares * prices[s.name]
    print(f"Old value: {old_value}")
    print(f"New value: {new_value}")
    print(f"Gain/loss : {new_value - old_value} \n")


def print_report(reportdata: list[tuple], formatter: tableformat.TableFormatter):
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:.2f}", f"{change:.2f}"]
        formatter.row(rowdata)


def portfolio_report(port_path: str, prices_path: str, fmt="txt"):
    portfolio = read_portfolio(port_path)
    prices = read_prices(prices_path)
    report = make_report(portfolio, prices)
    print_report(report, tableformat.create_formatter(fmt))


def main(argv):
    if len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])
    else:
        portfolio_report("Data/portfolio.csv", "Data/prices.csv")


if __name__ == "__main__":
    main(sys.argv)
