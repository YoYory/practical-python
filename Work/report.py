# report.py
#
# Exercise 2.4
import sys
from fileparse import parse_csv


def read_portfolio(filename: str) -> list:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    return parse_csv(
        filename, select=["name", "shares", "price"], types=[str, int, float]
    )


def read_prices(filename: str) -> dict:
    """
    Read a prices file into a dict with the names as the keys and the the
    prices as the values
    """
    return dict(parse_csv(filename, has_headers=False, types=[str, float]))


def make_report(portfolio: list, prices: dict) -> list[tuple]:
    rows = []
    for s in portfolio:
        newprice = prices[s["name"]]
        change = newprice - s["price"]
        t = (s["name"], s["shares"], newprice, change)
        rows.append(t)
    return rows


def print_gain_loss(portfolio: list, prices: dict):
    new_value = 0
    old_value = 0
    for s in portfolio:
        old_value += s["shares"] * s["price"]
        new_value += s["shares"] * prices[s["name"]]
    print(f"Old value: {old_value}")
    print(f"New value: {new_value}")
    print(f"Gain/loss : {new_value - old_value} \n")


def print_report(report: list[tuple]):
    headers = ("Name", "Shares", "Price", "Change")
    print("{:>10s} {:>10s} {:>10s} {:>10s}".format(*headers))
    print(("-" * 10 + " ") * len(headers))
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")


def portfolio_report(port_path: str, prices_path: str):
    portfolio = read_portfolio(port_path)
    prices = read_prices(prices_path)
    # print_gain_loss(portfolio, prices)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv):
    if len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    else:
        portfolio_report("Data/portfolio.csv", "Data/prices.csv")

if __name__ == "__main__":
    main(sys.argv)
