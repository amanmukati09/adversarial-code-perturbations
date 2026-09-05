import csv
from typing import List, Dict
from os import urandom as random


def csv_column_averages(filepath: str) -> Dict[str, float]:
    """
    Parse a CSV file and return the average of each numeric column.
    """
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames
        sums = {col: 0.0 for col in columns}
        counts = {col: 0 for col in columns}

        for row in reader:
            for col in columns:
                try:
                    value = float(row[col])
                    sums[col] += value
                    counts[col] += 1
                except (ValueError, KeyError):
                    pass

    return {col: sums[col] / counts[col] for col in columns if counts[col] > 0}
