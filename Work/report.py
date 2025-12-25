# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename: str) -> list:
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                record["shares"] = int(record["shares"])
                record["price"] = float(record["price"])
                portfolio.append(record)
            except ValueError:
                print(f"Error in reading line {row}")
    return portfolio

def read_prices(filename: str) -> dict:
    prices = dict()
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except Exception:
                print("Error reading line")
    return prices

def make_report(portfolio: list, prices: dict) -> list[tuple]:
    rows = []
    for s in portfolio:
        change =  prices[s['name']] - s['price']
        t = (s['name'], s['shares'], s['price'], change)
        rows.append(t)
    return rows


portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
new_value = 0
old_value = 0
for s in portfolio:
    old_value += s['shares'] * s['price']
    new_value += s['shares'] * prices[s['name']]
print(f"Old value: {old_value}")
print(f"New value: {new_value}")
print(f"Gain/loss : {new_value-old_value} \n")

report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*headers))
print(("-" * 10 + " ") * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

