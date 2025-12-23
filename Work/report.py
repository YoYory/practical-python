# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                portfolio.append({"name": row[0], "shares": int(row[1]), "price": float(row[2])})
            except ValueError:
                print(f"Error in reading line {row}")
    return portfolio

def read_prices(filename):
    prices = dict()
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                print("Error reading line")
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
new_value = 0
old_value = 0
for s in portfolio:
    old_value += s['shares'] * s['price']
    new_value += s['shares'] * prices[s['name']]

print(f"Old value: {old_value}")
print(f"New value: {new_value}")
print(f"Gain/loss : {new_value-old_value}")

