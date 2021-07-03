import csv

def _build_rows(format, col_names, data):
    if not format or not col_names:
        return []

    rows = []
    if format[0] == 'i':
        if isinstance(data, list):
            items = enumerate(data)
        elif isinstance(data, dict):
            items = data.items()
        for i, value in items:
            new_rows = _build_rows(format[1:], col_names[1:], value)
            for row in new_rows:
                row[col_names[0]] = i
            rows += new_rows
    elif format[0] == 'f':
        for key, value in data.items():
            new_rows = _build_rows(format[1:], col_names[1:], value)
            for row in new_rows:
                row[col_names[0]] = key
            rows += new_rows
    elif format[0] == 's':
        return [{col_names[0]: data}]
    return rows

def write_csv_data(f, format, col_names, data):
    writer = csv.DictWriter(f, col_names)
    rows = _build_rows(format, col_names, data)
    for row in rows:
        writer.writerow(row)
