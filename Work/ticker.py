import csv
import report
from follow import follow
from tableformat import create_formatter

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(item) for func, item in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = (dict(zip(["name", "price", "change"], row)) for row in rows)
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row["name"] in portfolio)
    formatter = create_formatter(fmt)
    formatter.headings(["name", "price", "change"])
    for row in rows:
        formatter.row([row["name"], f"{row["price"]:.2f}", f"{row["change"]:.2f}"])

if __name__ == '__main__':
    portfolio = report.read_portfolio("Data/portfolio.csv")
    rows = parse_stock_data(follow("Data/stocklog.csv"))
    rows = (row for row in rows if row["name"] in portfolio)
    for row in rows:
        print(row)

