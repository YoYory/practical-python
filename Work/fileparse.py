# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    lines: str,
    select: list = None,
    types: list = None,
    has_headers: bool = True,
    delimiter: str = ",",
    silence_errors: bool = False,
) -> list[dict] | list[tuple]:
    """
    Parse a csv file into a list of records

    :param filename: path to the filename
    """
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    if isinstance(lines, str):
        raise RuntimeError("lines needs to be an iterable other than str")
    rows = csv.reader(lines, delimiter=delimiter)
    # Read the file headers
    if has_headers:
        headers = next(rows)
        if select:
            indices = [headers.index(x) for x in select]
            headers = select
        else:
            indices = []
    records = []
    for i, row in enumerate(rows):
        if not row:
            continue
        if select:
            row = [row[i] for i in indices]
        if types:
            try:
                row = [func(x) for func, x in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f"Row {i}: Reason {e}")
                continue
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    return records
