# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=","):
    '''
    Parse a csv file into a list of records
    
    :param filename: path to the filename
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        # Read the file headers
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(x) for x in select]
                headers = select
            else:
                indices = []
        records = []
        for row in rows:
            if not row:
                continue
            if select:
                row = [row[i] for i in indices]
            if types:
                row = [func(x) for func, x in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records
