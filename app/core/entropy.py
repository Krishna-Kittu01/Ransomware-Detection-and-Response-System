import math
from collections import Counter


def calculate_entropy(data: bytes) -> float:
    """
    Calculate Shannon entropy of bytes.
    Returns a value between 0 and 8.
    """

    if not data:
        return 0.0

    counts = Counter(data)
    total = len(data)

    entropy = 0.0

    for count in counts.values():
        probability = count / total
        entropy -= probability * math.log2(probability)

    return entropy


def file_entropy(file_path):
    with open(file_path, "rb") as file:
        data = file.read(65536)  # Read first 64 KB only

    return calculate_entropy(data)