class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Emit a table in csv format
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Emit a table in HTML format
    """

    def headings(self, headers):
        print("<tr>", end="")
        for h in headers:
            print(f"<th>{h}<th>", end="")
        print("<tr>")

    def row(self, rowdata):
        print("<tr>", end="")
        for r in rowdata:
            print(f"<td>{r}<td>", end="")
        print("<tr>")


def create_formatter(name: str) -> TableFormatter:
    if name == "txt":
        return TextTableFormatter()
    elif name == "csv":
        return CSVTableFormatter()
    elif name == "HTML":
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f"Unknown format {name}")
